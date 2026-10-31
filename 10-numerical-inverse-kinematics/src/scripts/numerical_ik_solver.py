"""Numerical Inverse Kinematics (IK) Solvers for KUKA KR 6 R900-2.

Implements Newton-Raphson pseudo-inverse and Levenberg-Marquardt Damped Least Squares (DLS)
with joint limits clamping and singularity robustness.
"""

from typing import Tuple, Optional, Dict
import numpy as np


class NumericalIKSolverKR6:
    """Numerical IK engine using Jacobian-based iterations."""

    def __init__(self):
        # DH parameters of KR 6 R900-2: (theta_offset_deg, d_mm, a_mm, alpha_deg)
        self.dh_params = [
            (0.0,   400.0, 25.0,  -90.0),
            (-90.0, 0.0,   455.0, 0.0),
            (0.0,   0.0,   35.0,  90.0),
            (0.0,   420.0, 0.0,   -90.0),
            (0.0,   0.0,   0.0,   90.0),
            (0.0,   80.0,  0.0,   180.0),
        ]
        # Axis limits in degrees
        self.q_min = np.array([-170.0, -190.0, -120.0, -185.0, -120.0, -350.0])
        self.q_max = np.array([170.0, 45.0, 156.0, 185.0, 120.0, 350.0])

    def forward_kinematics(self, q_deg: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Compute end-effector position (3,) and rotation matrix (3,3)."""
        T = np.eye(4, dtype=np.float64)
        for qi, (offset, d, a, alpha) in zip(q_deg, self.dh_params):
            th = np.radians(qi + offset)
            al = np.radians(alpha)
            ct, st = np.cos(th), np.sin(th)
            ca, sa = np.cos(al), np.sin(al)
            Ai = np.array([
                [ct, -st * ca,  st * sa, a * ct],
                [st,  ct * ca, -ct * sa, a * st],
                [0.0, sa,       ca,      d],
                [0.0, 0.0,      0.0,     1.0]
            ], dtype=np.float64)
            T = T @ Ai
        return T[:3, 3], T[:3, :3]

    def compute_numerical_jacobian(self, q_deg: np.ndarray, eps: float = 1e-4) -> np.ndarray:
        """Compute 6x6 geometric Jacobian numerically via central finite differences."""
        J = np.zeros((6, 6), dtype=np.float64)
        p0, R0 = self.forward_kinematics(q_deg)

        for i in range(6):
            q_plus = q_deg.copy()
            q_minus = q_deg.copy()
            q_plus[i] += eps
            q_minus[i] -= eps

            p_plus, R_plus = self.forward_kinematics(q_plus)
            p_minus, R_minus = self.forward_kinematics(q_minus)

            # Linear velocity column dp / dq (converted from deg to rad)
            eps_rad = np.radians(2.0 * eps)
            J[:3, i] = (p_plus - p_minus) / eps_rad

            # Angular velocity column from rotation difference
            dR = R_plus @ R_minus.T
            # Skew symmetric vector
            wx = (dR[2, 1] - dR[1, 2]) / (2.0 * eps_rad)
            wy = (dR[0, 2] - dR[2, 0]) / (2.0 * eps_rad)
            wz = (dR[1, 0] - dR[0, 1]) / (2.0 * eps_rad)
            J[3:, i] = np.array([wx, wy, wz])

        return J

    def solve(self, target_pos: np.ndarray, target_rot: np.ndarray,
              q_init_deg: Optional[np.ndarray] = None,
              method: str = "dls",
              max_iterations: int = 100,
              pos_tol_mm: float = 0.5,
              rot_tol_rad: float = 1e-3,
              damping_lambda: float = 0.05) -> Dict[str, any]:
        """Solve inverse kinematics numerically with joint limit clamping."""
        if q_init_deg is None:
            # Default to Home configuration
            q_current = np.array([0.0, -90.0, 90.0, 0.0, 0.0, 0.0], dtype=np.float64)
        else:
            q_current = np.array(q_init_deg, dtype=np.float64).copy()

        converged = False
        final_iter = 0

        for it in range(max_iterations):
            p_curr, R_curr = self.forward_kinematics(q_current)

            # Position error
            e_pos = target_pos - p_curr

            # Orientation error (vector part of relative rotation)
            R_err = target_rot @ R_curr.T
            e_rot = 0.5 * np.array([
                R_err[2, 1] - R_err[1, 2],
                R_err[0, 2] - R_err[2, 0],
                R_err[1, 0] - R_err[0, 1]
            ])

            error = np.hstack([e_pos, e_rot])
            pos_err_norm = np.linalg.norm(e_pos)
            rot_err_norm = np.linalg.norm(e_rot)

            if pos_err_norm < pos_tol_mm and rot_err_norm < rot_tol_rad:
                converged = True
                final_iter = it
                break

            J = self.compute_numerical_jacobian(q_current)

            if method == "newton":
                # Moore-Penrose pseudo-inverse
                dq_rad = np.linalg.pinv(J) @ error
            else:
                # Levenberg-Marquardt Damped Least Squares: dq = J^T (J J^T + lambda^2 I)^-1 e
                A = J @ J.T + (damping_lambda ** 2) * np.eye(6)
                dq_rad = J.T @ np.linalg.solve(A, error)

            # Convert increment to degrees and step
            dq_deg = np.degrees(dq_rad)
            # Step scaling to prevent divergence
            step_scale = min(1.0, 20.0 / (np.linalg.norm(dq_deg) + 1e-6))
            q_current += step_scale * dq_deg

            # Clamping to joint limits
            q_current = np.clip(q_current, self.q_min, self.q_max)

        p_final, R_final = self.forward_kinematics(q_current)
        return {
            "converged": converged,
            "iterations": final_iter,
            "q_deg": q_current,
            "pos_error_mm": float(np.linalg.norm(target_pos - p_final)),
            "rot_error_rad": float(np.linalg.norm(e_rot)),
        }


def main():
    print("=" * 65)
    print("Lesson 10: Numerical Inverse Kinematics (Newton-Raphson & DLS)")
    print("=" * 65)

    solver = NumericalIKSolverKR6()

    # Target pose
    target_pos = np.array([450.0, 50.0, 420.0])
    target_rot = np.eye(3)

    print(f"\nTarget Position: {target_pos} mm")

    res_dls = solver.solve(target_pos, target_rot, method="dls")
    print(f"\n[DLS Solver Result]")
    print(f"  Converged:    {res_dls['converged']} (in {res_dls['iterations']} iterations)")
    print(f"  Final Joints: {np.round(res_dls['q_deg'], 2).tolist()} deg")
    print(f"  Pos Error:    {res_dls['pos_error_mm']:.4f} mm")

    res_nr = solver.solve(target_pos, target_rot, method="newton")
    print(f"\n[Newton-Raphson Solver Result]")
    print(f"  Converged:    {res_nr['converged']} (in {res_nr['iterations']} iterations)")
    print(f"  Pos Error:    {res_nr['pos_error_mm']:.4f} mm")


if __name__ == "__main__":
    main()
