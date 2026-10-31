"""Unit tests for Forward Kinematics (FK) solver."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from forward_kinematics import ForwardKinematicsKR6


def test_fk_zero_configuration():
    solver = ForwardKinematicsKR6()
    res = solver.solve_fk([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Position check at zero configuration
    # d1 = 400, a1 = 25, a2 = 455, d4 = 420, d6 = 80
    assert np.isclose(res["y_mm"], 0.0, atol=1e-4)
    # Z coordinate should equal d1 + a2 + d6
    assert np.isclose(res["z_mm"], 890.0, atol=1e-4)
    # Matrix determinant is 1
    assert np.isclose(np.linalg.det(res["rot"]), 1.0, atol=1e-6)


def test_fk_symmetry_in_yaw():
    solver = ForwardKinematicsKR6()
    # A1 rotation by +90 and -90 should produce symmetric Y and equal Z
    res_pos = solver.solve_fk([90.0, -90.0, 90.0, 0.0, 0.0, 0.0])
    res_neg = solver.solve_fk([-90.0, -90.0, 90.0, 0.0, 0.0, 0.0])

    assert np.isclose(res_pos["z_mm"], res_neg["z_mm"], atol=1e-4)
    assert np.isclose(res_pos["y_mm"], -res_neg["y_mm"], atol=1e-4)
    assert np.isclose(res_pos["x_mm"], res_neg["x_mm"], atol=1e-4)


def test_invalid_input_length():
    solver = ForwardKinematicsKR6()
    with pytest.raises(ValueError):
        solver.solve_fk([0.0, 0.0, 0.0])
