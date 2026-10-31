"""Rodrigues' Rotation Formula & SO(3) Lie Algebra Solvers.

Implements spatial rotations about an arbitrary unit axis k by angle theta,
proving the isomorphism between the Lie algebra so(3) and the Lie group SO(3).
Used extensively for KUKA robot orientation interpolation and joint axis rotations.
"""

from typing import Tuple
import numpy as np


def skew_symmetric(axis: np.ndarray) -> np.ndarray:
    r"""Compute 3x3 skew-symmetric matrix [k]_x from 3D unit axis vector k.

    [k]_x = [[  0, -kz,  ky],
             [ kz,   0, -kx],
             [-ky,  kx,   0]]
    """
    k = np.asarray(axis, dtype=np.float64).flatten()
    if k.shape != (3,):
        raise ValueError("Axis vector must have 3 elements.")
    return np.array([
        [0.0, -k[2], k[1]],
        [k[2], 0.0, -k[0]],
        [-k[1], k[0], 0.0]
    ], dtype=np.float64)


def rodrigues_formula(axis: np.ndarray, theta_rad: float) -> np.ndarray:
    r"""Compute SO(3) rotation matrix using Rodrigues' rotation formula.

    R(k, theta) = I + sin(theta) * K + (1 - cos(theta)) * K^2
    where K = [k]_x and ||k|| = 1.
    """
    k = np.asarray(axis, dtype=np.float64).flatten()
    norm_k = np.linalg.norm(k)
    if np.isclose(norm_k, 0.0):
        raise ValueError("Rotation axis cannot be a zero vector.")
    k_unit = k / norm_k

    K = skew_symmetric(k_unit)
    I = np.eye(3, dtype=np.float64)

    R = I + np.sin(theta_rad) * K + (1.0 - np.cos(theta_rad)) * (K @ K)
    return R


def logarithmic_map_so3(R: np.ndarray) -> Tuple[np.ndarray, float]:
    r"""Extract equivalent rotation axis k and angle theta from SO(3) matrix R.

    Inverse Rodrigues transformation:
        theta = arccos((trace(R) - 1) / 2)
        k = (1 / (2 * sin(theta))) * [R32 - R23, R13 - R31, R21 - R12]^T
    """
    R_mat = np.asarray(R, dtype=np.float64)
    if R_mat.shape != (3, 3):
        raise ValueError("Input must be a 3x3 matrix.")

    # Numerical safety for trace
    tr = np.clip((np.trace(R_mat) - 1.0) / 2.0, -1.0, 1.0)
    theta = float(np.arccos(tr))

    if np.isclose(theta, 0.0):
        # Zero rotation: axis can be arbitrarily chosen (e.g., z-axis)
        return np.array([0.0, 0.0, 1.0]), 0.0

    if np.isclose(theta, np.pi):
        # 180 degree rotation singularity
        # R - I = 2 * K^2 => diagonal terms help determine axis
        diag = np.diag(R_mat)
        k_sq = (diag + 1.0) / 2.0
        k_sq = np.maximum(k_sq, 0.0)
        k = np.sqrt(k_sq)
        # Signs from off-diagonals
        if R_mat[0, 1] < 0:
            k[1] = -k[1]
        if R_mat[0, 2] < 0:
            k[2] = -k[2]
        norm = np.linalg.norm(k)
        if norm > 1e-6:
            k = k / norm
        return k, np.pi

    rx = R_mat[2, 1] - R_mat[1, 2]
    ry = R_mat[0, 2] - R_mat[2, 0]
    rz = R_mat[1, 0] - R_mat[0, 1]
    k = (1.0 / (2.0 * np.sin(theta))) * np.array([rx, ry, rz])
    return k / np.linalg.norm(k), theta


def rotate_vector(v: np.ndarray, axis: np.ndarray, theta_rad: float) -> np.ndarray:
    r"""Rotate 3D vector v about axis k by angle theta directly using vector Rodrigues form:

    v_rot = v * cos(theta) + (k x v) * sin(theta) + k * (k . v) * (1 - cos(theta))
    """
    k = np.asarray(axis, dtype=np.float64).flatten()
    k_unit = k / np.linalg.norm(k)
    v_vec = np.asarray(v, dtype=np.float64).flatten()

    term1 = v_vec * np.cos(theta_rad)
    term2 = np.cross(k_unit, v_vec) * np.sin(theta_rad)
    term3 = k_unit * np.dot(k_unit, v_vec) * (1.0 - np.cos(theta_rad))
    return term1 + term2 + term3


def is_valid_so3(R: np.ndarray, tol: float = 1e-6) -> bool:
    """Verify SO(3) properties: R^T * R == I and det(R) == +1."""
    I = np.eye(3)
    orthogonal = np.allclose(R.T @ R, I, atol=tol)
    unit_det = np.isclose(np.linalg.det(R), 1.0, atol=tol)
    return bool(orthogonal and unit_det)


def main():
    print("=" * 65)
    print("Lesson 05: Rodrigues Rotation Formula & SO(3) Lie Algebra")
    print("=" * 65)

    # Example: Rotate around diagonal axis [1, 1, 1] by 60 degrees
    axis = np.array([1.0, 1.0, 1.0])
    theta_deg = 60.0
    theta_rad = np.radians(theta_deg)

    R = rodrigues_formula(axis, theta_rad)
    print(f"\nRotation Matrix R for axis {axis} by {theta_deg}°:")
    print(np.round(R, 4))
    print(f"Is valid SO(3) matrix: {is_valid_so3(R)}")

    # Vector rotation comparison
    v = np.array([1.0, 0.0, 0.0])
    v_rot_matrix = R @ v
    v_rot_formula = rotate_vector(v, axis, theta_rad)

    print(f"\nOriginal vector v: {v}")
    print(f"Rotated via Matrix R @ v:       {np.round(v_rot_matrix, 4)}")
    print(f"Rotated via Vector Formula:      {np.round(v_rot_formula, 4)}")
    print(f"Match: {np.allclose(v_rot_matrix, v_rot_formula)}")

    # Inverse Logarithmic map
    k_rec, th_rec = logarithmic_map_so3(R)
    print(f"\nInverse Logarithmic Map Recovered:")
    print(f"  Axis: {np.round(k_rec, 4)} (Original: {np.round(axis / np.linalg.norm(axis), 4)})")
    print(f"  Angle: {np.degrees(th_rec):.2f}° (Original: {theta_deg:.2f}°)")


if __name__ == "__main__":
    main()
