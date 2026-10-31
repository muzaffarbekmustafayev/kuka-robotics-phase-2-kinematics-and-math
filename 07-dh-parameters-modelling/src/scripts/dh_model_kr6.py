"""Denavit-Hartenberg (DH) Kinematic Model for KUKA KR 6 R900-2 (KR AGILUS-2).

Calculates standard DH transformation matrices A_i^(i-1) and cumulative base-to-link transforms
for all 6 joints of the industrial manipulator.
"""

from dataclasses import dataclass
from typing import List, Tuple
import numpy as np


@dataclass
class DHParameter:
    """Standard DH parameters for a single revolute joint."""
    theta_offset_deg: float
    d_mm: float
    a_mm: float
    alpha_deg: float


class KukaKR6DHModel:
    r"""Denavit-Hartenberg parameter table and transformation engine for KUKA KR 6 R900-2.

    Manufacturer Specs (KR 6 R900-2):
        d1 = 400.0 mm
        a1 = 25.0 mm,  alpha1 = -90 deg
        a2 = 455.0 mm, alpha2 = 0 deg (joint 2 has -90 deg zero offset)
        a3 = 35.0 mm,  alpha3 = 90 deg
        d4 = 420.0 mm, a4 = 0 mm, alpha4 = -90 deg
        d5 = 0.0 mm,   a5 = 0 mm, alpha5 = 90 deg
        d6 = 80.0 mm,  a6 = 0 mm, alpha6 = 180 deg (flange normal alignment)
    """

    def __init__(self):
        self.dh_table = [
            DHParameter(theta_offset_deg=0.0,   d_mm=400.0, a_mm=25.0,  alpha_deg=-90.0),
            DHParameter(theta_offset_deg=-90.0, d_mm=0.0,   a_mm=455.0, alpha_deg=0.0),
            DHParameter(theta_offset_deg=0.0,   d_mm=0.0,   a_mm=35.0,  alpha_deg=90.0),
            DHParameter(theta_offset_deg=0.0,   d_mm=420.0, a_mm=0.0,   alpha_deg=-90.0),
            DHParameter(theta_offset_deg=0.0,   d_mm=0.0,   a_mm=0.0,   alpha_deg=90.0),
            DHParameter(theta_offset_deg=0.0,   d_mm=80.0,  a_mm=0.0,   alpha_deg=180.0),
        ]

    @staticmethod
    def standard_dh_matrix(theta_deg: float, d: float, a: float, alpha_deg: float) -> np.ndarray:
        r"""Compute 4x4 standard DH transformation matrix.

        T = Rot_z(theta) * Trans_z(d) * Trans_x(a) * Rot_x(alpha)
        """
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

    def compute_link_transforms(self, joint_angles_deg: List[float]) -> List[np.ndarray]:
        """Compute relative transformation matrices A_i^(i-1) for given joint angles."""
        if len(joint_angles_deg) != 6:
            raise ValueError("Exactly 6 joint angles required.")

        matrices = []
        for q, dh in zip(joint_angles_deg, self.dh_table):
            effective_theta = q + dh.theta_offset_deg
            T_i = self.standard_dh_matrix(effective_theta, dh.d_mm, dh.a_mm, dh.alpha_deg)
            matrices.append(T_i)
        return matrices

    def compute_all_frames(self, joint_angles_deg: List[float]) -> List[np.ndarray]:
        """Compute cumulative transformation matrices T_0^i for each link i in {1..6}."""
        relative_mats = self.compute_link_transforms(joint_angles_deg)
        cumulative = []
        T_curr = np.eye(4, dtype=np.float64)
        for rel in relative_mats:
            T_curr = T_curr @ rel
            cumulative.append(T_curr.copy())
        return cumulative

    def forward_flange(self, joint_angles_deg: List[float]) -> np.ndarray:
        """Compute final base-to-flange transformation matrix T_0^6."""
        frames = self.compute_all_frames(joint_angles_deg)
        return frames[-1]


def main():
    print("=" * 65)
    print("Lesson 07: Denavit-Hartenberg (DH) Model for KUKA KR 6 R900-2")
    print("=" * 65)

    robot = KukaKR6DHModel()

    # Configuration 1: Zero Position [0, 0, 0, 0, 0, 0]
    q_zero = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    T_zero = robot.forward_flange(q_zero)
    print(f"\nFlange Pose at Zero Configuration {q_zero}:")
    print(f"  Position (X, Y, Z) mm: [{T_zero[0, 3]:.2f}, {T_zero[1, 3]:.2f}, {T_zero[2, 3]:.2f}]")

    # Configuration 2: Home Position XHOME [0, -90, 90, 0, 0, 0]
    q_home = [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]
    T_home = robot.forward_flange(q_home)
    print(f"\nFlange Pose at XHOME Configuration {q_home}:")
    print(f"  Position (X, Y, Z) mm: [{T_home[0, 3]:.2f}, {T_home[1, 3]:.2f}, {T_home[2, 3]:.2f}]")


if __name__ == "__main__":
    main()
