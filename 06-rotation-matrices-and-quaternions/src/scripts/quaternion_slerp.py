"""Quaternion & Euler Angle Transforms with SLERP Trajectory Interpolator.

Implements KUKA Z-Y'-X'' (A, B, C) Euler rotations, SO(3) matrices, unit quaternions (S^3),
and Spherical Linear Interpolation (SLERP) to prevent Gimbal Lock during robot motions.
"""

from typing import Tuple, List
import numpy as np


def euler_zyx_to_matrix(a_deg: float, b_deg: float, c_deg: float) -> np.ndarray:
    r"""Convert KUKA Euler angles A, B, C (degrees) to 3x3 rotation matrix R.

    KUKA convention is intrinsic Z-Y'-X'':
        R = Rz(A) @ Ry(B) @ Rx(C)
    where A is rotation about Z, B about Y, C about X.
    """
    a = np.radians(a_deg)
    b = np.radians(b_deg)
    c = np.radians(c_deg)

    ca, sa = np.cos(a), np.sin(a)
    cb, sb = np.cos(b), np.sin(b)
    cc, sc = np.cos(c), np.sin(c)

    R = np.array([
        [ca * cb, ca * sb * sc - sa * cc, ca * sb * cc + sa * sc],
        [sa * cb, sa * sb * sc + ca * cc, sa * sb * cc - ca * sc],
        [-sb,     cb * sc,                cb * cc]
    ], dtype=np.float64)
    return R


def matrix_to_euler_zyx(R: np.ndarray) -> Tuple[float, float, float]:
    r"""Extract KUKA Euler angles (A, B, C in degrees) from SO(3) rotation matrix.

    Handles Gimbal lock pitch singularity where B = +/- 90 degrees.
    """
    R_mat = np.asarray(R, dtype=np.float64)
    sb = -R_mat[2, 0]
    sb_clamped = np.clip(sb, -1.0, 1.0)
    b_rad = np.arcsin(sb_clamped)
    cb = np.cos(b_rad)

    if np.abs(cb) > 1e-6:
        # Standard non-singular case
        a_rad = np.arctan2(R_mat[1, 0], R_mat[0, 0])
        c_rad = np.arctan2(R_mat[2, 1], R_mat[2, 2])
    else:
        # Gimbal Lock: B = +90 deg or -90 deg
        c_rad = 0.0  # Set roll arbitrarily
        if sb > 0:  # B = +90 deg
            a_rad = np.arctan2(R_mat[0, 1], R_mat[1, 1])
        else:       # B = -90 deg
            a_rad = -np.arctan2(R_mat[0, 1], R_mat[1, 1])

    return float(np.degrees(a_rad)), float(np.degrees(b_rad)), float(np.degrees(c_rad))


def matrix_to_quaternion(R: np.ndarray) -> np.ndarray:
    r"""Convert 3x3 rotation matrix to unit quaternion q = [w, x, y, z].

    Uses Shepperd's algorithm for numerical robustness against small traces.
    """
    R_mat = np.asarray(R, dtype=np.float64)
    tr = np.trace(R_mat)

    if tr > 0.0:
        s = np.sqrt(tr + 1.0) * 2.0  # s = 4 * w
        w = 0.25 * s
        x = (R_mat[2, 1] - R_mat[1, 2]) / s
        y = (R_mat[0, 2] - R_mat[2, 0]) / s
        z = (R_mat[1, 0] - R_mat[0, 1]) / s
    elif (R_mat[0, 0] > R_mat[1, 1]) and (R_mat[0, 0] > R_mat[2, 2]):
        s = np.sqrt(1.0 + R_mat[0, 0] - R_mat[1, 1] - R_mat[2, 2]) * 2.0  # s = 4 * x
        w = (R_mat[2, 1] - R_mat[1, 2]) / s
        x = 0.25 * s
        y = (R_mat[0, 1] + R_mat[1, 0]) / s
        z = (R_mat[0, 2] + R_mat[2, 0]) / s
    elif R_mat[1, 1] > R_mat[2, 2]:
        s = np.sqrt(1.0 + R_mat[1, 1] - R_mat[0, 0] - R_mat[2, 2]) * 2.0  # s = 4 * y
        w = (R_mat[0, 2] - R_mat[2, 0]) / s
        x = (R_mat[0, 1] + R_mat[1, 0]) / s
        y = 0.25 * s
        z = (R_mat[1, 2] + R_mat[2, 1]) / s
    else:
        s = np.sqrt(1.0 + R_mat[2, 2] - R_mat[0, 0] - R_mat[1, 1]) * 2.0  # s = 4 * z
        w = (R_mat[1, 0] - R_mat[0, 1]) / s
        x = (R_mat[0, 2] + R_mat[2, 0]) / s
        y = (R_mat[1, 2] + R_mat[2, 1]) / s
        z = 0.25 * s

    q = np.array([w, x, y, z], dtype=np.float64)
    return q / np.linalg.norm(q)


def quaternion_to_matrix(q: np.ndarray) -> np.ndarray:
    r"""Convert unit quaternion q = [w, x, y, z] to 3x3 SO(3) rotation matrix."""
    q_norm = q / np.linalg.norm(q)
    w, x, y, z = q_norm

    return np.array([
        [1.0 - 2.0 * (y**2 + z**2), 2.0 * (x * y - z * w),       2.0 * (x * z + y * w)],
        [2.0 * (x * y + z * w),       1.0 - 2.0 * (x**2 + z**2), 2.0 * (y * z - x * w)],
        [2.0 * (x * z - y * w),       2.0 * (y * z + x * w),       1.0 - 2.0 * (x**2 + y**2)]
    ], dtype=np.float64)


def quaternion_multiply(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
    r"""Compute Hamilton quaternion product q = q1 (x) q2."""
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2

    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
    z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
    return np.array([w, x, y, z], dtype=np.float64)


def slerp(q1: np.ndarray, q2: np.ndarray, t: float) -> np.ndarray:
    r"""Spherical Linear Interpolation (SLERP) between unit quaternions q1 and q2.

    t in [0.0, 1.0]. Guarantees constant angular velocity trajectory along the 4D sphere.
    """
    t = float(np.clip(t, 0.0, 1.0))
    q1_n = q1 / np.linalg.norm(q1)
    q2_n = q2 / np.linalg.norm(q2)

    dot = float(np.dot(q1_n, q2_n))

    # Shortest path: if dot < 0, invert q2
    if dot < 0.0:
        q2_n = -q2_n
        dot = -dot

    # If quaternions are very close, perform normalized linear interpolation (NLERP)
    if dot > 0.9995:
        res = q1_n + t * (q2_n - q1_n)
        return res / np.linalg.norm(res)

    omega = np.arccos(dot)
    sin_omega = np.sin(omega)

    scale1 = np.sin((1.0 - t) * omega) / sin_omega
    scale2 = np.sin(t * omega) / sin_omega

    q_interp = scale1 * q1_n + scale2 * q2_n
    return q_interp / np.linalg.norm(q_interp)


def interpolate_euler_trajectory(euler_start: Tuple[float, float, float],
                                 euler_end: Tuple[float, float, float],
                                 steps: int = 5) -> List[Tuple[float, float, float]]:
    """Interpolate smoothly between two KUKA orientations via SLERP."""
    R_start = euler_zyx_to_matrix(*euler_start)
    R_end = euler_zyx_to_matrix(*euler_end)

    q_start = matrix_to_quaternion(R_start)
    q_end = matrix_to_quaternion(R_end)

    traj = []
    for step in range(steps):
        t = step / (steps - 1) if steps > 1 else 0.0
        q_t = slerp(q_start, q_end, t)
        R_t = quaternion_to_matrix(q_t)
        euler_t = matrix_to_euler_zyx(R_t)
        traj.append(euler_t)
    return traj


def main():
    print("=" * 65)
    print("Lesson 06: Rotation Matrices, Quaternions & SLERP Interpolation")
    print("=" * 65)

    euler_a = (30.0, 45.0, -20.0)
    euler_b = (120.0, -15.0, 60.0)

    print(f"\nStart Euler (A, B, C): {euler_a}")
    print(f"End Euler   (A, B, C): {euler_b}")

    R_a = euler_zyx_to_matrix(*euler_a)
    q_a = matrix_to_quaternion(R_a)
    print(f"\nQuaternion Start q_A: {np.round(q_a, 4)}")

    traj = interpolate_euler_trajectory(euler_a, euler_b, steps=5)
    print("\nSLERP Trajectory (5 Waypoints):")
    for idx, pt in enumerate(traj):
        print(f"  Step {idx} (t={idx/4:.2f}): A={pt[0]:6.2f}°, B={pt[1]:6.2f}°, C={pt[2]:6.2f}°")


if __name__ == "__main__":
    main()
