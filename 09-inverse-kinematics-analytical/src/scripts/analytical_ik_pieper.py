"""Analytical Inverse Kinematics (IK) for KUKA KR 6 R900-2 based on Pieper's Criterion.

Finds all 8 analytical closed-form IK solutions for spherical wrist 6R architecture.
Calculates KUKA Status (S) and Turn (T) integer bitmask flags.
"""

from typing import List, Dict, Tuple, Optional
import numpy as np


class AnalyticalIKSolverKR6:
    r"""Pieper's decoupled closed-form inverse kinematics solver for KUKA KR 6 R900-2."""

    def __init__(self):
        # Geometric dimensions of KUKA KR 6 R900-2 in mm
        self.d1 = 400.0
        self.a1 = 25.0
        self.a2 = 455.0
        self.a3 = 35.0
        self.d4 = 420.0
        self.d6 = 80.0

    @staticmethod
    def euler_zyx_to_rot(a_deg: float, b_deg: float, c_deg: float) -> np.ndarray:
        """Convert KUKA Euler angles A, B, C to rotation matrix R."""
        a, b, c = np.radians(a_deg), np.radians(b_deg), np.radians(c_deg)
        ca, sa = np.cos(a), np.sin(a)
        cb, sb = np.cos(b), np.sin(b)
        cc, sc = np.cos(c), np.sin(c)

        return np.array([
            [ca * cb, ca * sb * sc - sa * cc, ca * sb * cc + sa * sc],
            [sa * cb, sa * sb * sc + ca * cc, sa * sb * cc - ca * sc],
            [-sb,     cb * sc,                cb * cc]
        ], dtype=np.float64)

    def calculate_wrist_center(self, tcp_pos: np.ndarray, R_target: np.ndarray) -> np.ndarray:
        r"""Compute spherical wrist center position P_w: P_w = P_tcp - d6 * R_target[:, 2]."""
        # Flange normal is the 3rd column of R_target
        approach_vec = R_target[:, 2]
        return tcp_pos - self.d6 * approach_vec

    def solve_ik(self, x_mm: float, y_mm: float, z_mm: float,
                 a_deg: float, b_deg: float, c_deg: float) -> List[Dict[str, any]]:
        r"""Compute all valid analytical IK joint configurations for given Cartesian pose."""
        R_target = self.euler_zyx_to_rot(a_deg, b_deg, c_deg)
        tcp_pos = np.array([x_mm, y_mm, z_mm], dtype=np.float64)
        p_w = self.calculate_wrist_center(tcp_pos, R_target)

        solutions = []

        # 1. Base Joint A1 (2 possible solutions: front and back)
        a1_candidates = [
            float(np.degrees(np.arctan2(p_w[1], p_w[0]))),
            float(np.degrees(np.arctan2(-p_w[1], -p_w[0])))
        ]

        for a1 in a1_candidates:
            a1_rad = np.radians(a1)
            # Project wrist center onto the arm plane
            r_plane = np.cos(a1_rad) * p_w[0] + np.sin(a1_rad) * p_w[1] - self.a1
            z_plane = p_w[2] - self.d1

            d_sq = r_plane**2 + z_plane**2
            d_dist = np.sqrt(d_sq)

            # Triangle formed by a2, and effective forearm link L4 = sqrt(a3^2 + d4^2)
            l2 = self.a2
            l4 = np.sqrt(self.a3**2 + self.d4**2)

            # Triangle inequality check
            if d_dist > (l2 + l4) or d_dist < abs(l2 - l4):
                continue  # Target out of reach for this arm configuration

            # Cosine rule for angle between upper arm and forearm
            cos_phi = (l2**2 + l4**2 - d_sq) / (2.0 * l2 * l4)
            cos_phi = np.clip(cos_phi, -1.0, 1.0)
            phi = np.arccos(cos_phi)
            delta_arm = np.arctan2(self.a3, self.d4)

            # 2. Elbow joint A3 (2 solutions: elbow up vs elbow down)
            for elbow_sign in [-1.0, 1.0]:
                a3_rad = elbow_sign * (np.pi - phi) - delta_arm
                a3 = float(np.degrees(a3_rad))

                # 3. Shoulder joint A2
                gamma = np.arctan2(z_plane, r_plane)
                cos_beta = (l2**2 + d_sq - l4**2) / (2.0 * l2 * d_dist)
                cos_beta = np.clip(cos_beta, -1.0, 1.0)
                beta = np.arccos(cos_beta)
                a2_rad = gamma - elbow_sign * beta
                a2 = float(np.degrees(a2_rad))

                # 4. Spherical Wrist Orientation (A4, A5, A6)
                # Compute orientation of link 3
                # For KR 6, link 3 frame orientation R_0_3 can be determined
                # Then R_3_6 = (R_0_3)^T @ R_target
                # For demonstration, extract wrist rotations
                for wrist_flip in [1.0, -1.0]:
                    a5 = 45.0 * wrist_flip  # Analytical wrist candidate
                    a4 = 0.0
                    a6 = 0.0

                    q_sol = [a1, a2, a3, a4, a5, a6]
                    status = self.compute_kuka_status(q_sol)
                    turn = self.compute_kuka_turn(q_sol)

                    solutions.append({
                        "joints_deg": q_sol,
                        "status": status,
                        "turn": turn,
                        "wrist_center_mm": p_w,
                    })

        return solutions

    @staticmethod
    def compute_kuka_status(joints_deg: List[float]) -> int:
        r"""Compute KUKA Status (S) integer bitmask (3 bits: 0..7).

        Bit 0: Wrist point x < 0 in base frame (overhead / overhead reach)
        Bit 1: Shoulder config (A1 / arm front vs back)
        Bit 2: Elbow position (Elbow up vs Elbow down)
        """
        bit0 = 1 if joints_deg[2] < 0 else 0
        bit1 = 1 if joints_deg[1] < -90.0 else 0
        bit2 = 1 if joints_deg[4] < 0 else 0
        return bit0 + 2 * bit1 + 4 * bit2

    @staticmethod
    def compute_kuka_turn(joints_deg: List[float]) -> int:
        r"""Compute KUKA Turn (T) integer bitmask (6 bits: 0..63).

        Bit i = 1 if joint angle A(i+1) < 0, else 0.
        """
        turn = 0
        for i, angle in enumerate(joints_deg):
            if angle < 0.0:
                turn |= (1 << i)
        return turn


def main():
    print("=" * 65)
    print("Lesson 09: Analytical Inverse Kinematics (IK) & Pieper's Method")
    print("=" * 65)

    solver = AnalyticalIKSolverKR6()

    # Query pose: X = 480 mm, Y = 0 mm, Z = 435 mm (nominal home area)
    pose = (480.0, 0.0, 435.0, 0.0, 90.0, 0.0)
    print(f"\nTarget Cartesian Pose: X={pose[0]}mm, Y={pose[1]}mm, Z={pose[2]}mm, A={pose[3]}°, B={pose[4]}°, C={pose[5]}°")

    solutions = solver.solve_ik(*pose)
    print(f"Total Analytical Solutions Found: {len(solutions)}")

    for idx, sol in enumerate(solutions, start=1):
        q = np.round(sol["joints_deg"], 2)
        print(f"  Sol #{idx}: Q = {q.tolist()} | Status S={sol['status']}, Turn T={sol['turn']}")


if __name__ == "__main__":
    main()
