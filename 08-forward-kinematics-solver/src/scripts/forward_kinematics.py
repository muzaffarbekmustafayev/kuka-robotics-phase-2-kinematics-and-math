"""Forward Kinematics (FK) Solver for KUKA KR 6 R900-2 (Agilus).

Computes end-effector Cartesian pose {X, Y, Z, A, B, C} from joint angles q = [A1, A2, A3, A4, A5, A6].
Supports tool and base coordinate transformations.
"""

from typing import List, Dict, Tuple
import numpy as np


class ForwardKinematicsKR6:
    """Industrial Forward Kinematics Engine for KUKA KR 6 R900-2."""

    def __init__(self):
        # DH Parameters: (theta_offset_deg, d_mm, a_mm, alpha_deg)
        self.dh_params = [
            (0.0,   400.0, 25.0,  -90.0),
            (-90.0, 0.0,   455.0, 0.0),
            (0.0,   0.0,   35.0,  90.0),
            (0.0,   420.0, 0.0,   -90.0),
            (0.0,   0.0,   0.0,   90.0),
            (0.0,   80.0,  0.0,   180.0),
        ]

    @staticmethod
    def dh_transform(theta_deg: float, d: float, a: float, alpha_deg: float) -> np.ndarray:
        """Compute standard 4x4 DH transformation matrix."""
        th = np.radians(theta_deg)
        al = np.radians(alpha_deg)

        ct, st = np.cos(th), np.sin(th)
        ca, sa = np.cos(al), np.sin(al)

        return np.array([
            [ct, -st * ca,  st * sa, a * ct],
            [st,  ct * ca, -ct * sa, a * st],
            [0.0, sa,       ca,      d],
            [0.0, 0.0,      0.0,     1.0]
        ], dtype=np.float64)

    @staticmethod
    def matrix_to_kuka_angles(R: np.ndarray) -> Tuple[float, float, float]:
        """Extract KUKA Euler angles (A, B, C) in degrees from 3x3 rotation matrix."""
        sb = -R[2, 0]
        sb = np.clip(sb, -1.0, 1.0)
        b_rad = np.arcsin(sb)
        cb = np.cos(b_rad)

        if np.abs(cb) > 1e-6:
            a_rad = np.arctan2(R[1, 0], R[0, 0])
            c_rad = np.arctan2(R[2, 1], R[2, 2])
        else:
            c_rad = 0.0
            a_rad = np.arctan2(R[0, 1], R[1, 1]) if sb > 0 else -np.arctan2(R[0, 1], R[1, 1])

        return float(np.degrees(a_rad)), float(np.degrees(b_rad)), float(np.degrees(c_rad))

    def solve_fk(self, joints_deg: List[float]) -> Dict[str, any]:
        """Compute complete forward kinematics forward transformation and KUKA pose."""
        if len(joints_deg) != 6:
            raise ValueError("Forward kinematics requires 6 axis angles [A1..A6].")

        T = np.eye(4, dtype=np.float64)
        for q, (offset, d, a, alpha) in zip(joints_deg, self.dh_params):
            A_i = self.dh_transform(q + offset, d, a, alpha)
            T = T @ A_i

        x, y, z = T[0, 3], T[1, 3], T[2, 3]
        a, b, c = self.matrix_to_kuka_angles(T[:3, :3])

        return {
            "transform_matrix": T,
            "x_mm": float(x),
            "y_mm": float(y),
            "z_mm": float(z),
            "a_deg": float(a),
            "b_deg": float(b),
            "c_deg": float(c),
            "pos": np.array([x, y, z]),
            "rot": T[:3, :3],
        }


def main():
    print("=" * 65)
    print("Lesson 08: Forward Kinematics (FK) Solver for KUKA KR 6 R900-2")
    print("=" * 65)

    solver = ForwardKinematicsKR6()

    # Test configuration: XHOME = [0, -90, 90, 0, 0, 0]
    q_home = [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]
    res_home = solver.solve_fk(q_home)

    print(f"\nJoint Configuration: {q_home}")
    print(f"KUKA Cartesian Pose:")
    print(f"  X = {res_home['x_mm']:8.2f} mm")
    print(f"  Y = {res_home['y_mm']:8.2f} mm")
    print(f"  Z = {res_home['z_mm']:8.2f} mm")
    print(f"  A = {res_home['a_deg']:8.2f}°")
    print(f"  B = {res_home['b_deg']:8.2f}°")
    print(f"  C = {res_home['c_deg']:8.2f}°")


if __name__ == "__main__":
    main()
