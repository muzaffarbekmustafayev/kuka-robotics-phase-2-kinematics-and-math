"""Unit tests for Numerical Inverse Kinematics solver."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from numerical_ik_solver import NumericalIKSolverKR6


def test_numerical_jacobian_shape_and_finite():
    solver = NumericalIKSolverKR6()
    q = np.array([0.0, -90.0, 90.0, 0.0, 0.0, 0.0])
    J = solver.compute_numerical_jacobian(q)
    assert J.shape == (6, 6)
    assert np.all(np.isfinite(J))


def test_dls_solver_reaches_target():
    solver = NumericalIKSolverKR6()
    # Choose known reachable point from FK
    q_known = np.array([10.0, -80.0, 85.0, 5.0, 15.0, 0.0])
    target_pos, target_rot = solver.forward_kinematics(q_known)

    # Initialize from slightly perturbed position
    q_init = q_known + np.array([5.0, -5.0, 5.0, -5.0, 5.0, -5.0])
    res = solver.solve(target_pos, target_rot, q_init_deg=q_init, method="dls")

    assert res["converged"] is True
    assert res["pos_error_mm"] < 1.0


def test_joint_limits_enforcement():
    solver = NumericalIKSolverKR6()
    # Target positioned far away
    target_pos = np.array([1500.0, 0.0, 400.0])
    target_rot = np.eye(3)
    res = solver.solve(target_pos, target_rot, max_iterations=20)

    # Solver should enforce axis limits
    q_res = res["q_deg"]
    assert np.all(q_res >= solver.q_min - 1e-4)
    assert np.all(q_res <= solver.q_max + 1e-4)
