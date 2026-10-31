"""Unit tests for DH kinematic model of KUKA KR 6 R900-2."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from dh_model_kr6 import KukaKR6DHModel, DHParameter


def test_dh_table_dimensions():
    robot = KukaKR6DHModel()
    assert len(robot.dh_table) == 6
    # Verify link lengths
    assert robot.dh_table[0].d_mm == 400.0
    assert robot.dh_table[0].a_mm == 25.0
    assert robot.dh_table[1].a_mm == 455.0
    assert robot.dh_table[2].a_mm == 35.0
    assert robot.dh_table[3].d_mm == 420.0
    assert robot.dh_table[5].d_mm == 80.0


def test_single_dh_matrix_orthogonality():
    robot = KukaKR6DHModel()
    T = robot.standard_dh_matrix(theta_deg=37.0, d=150.0, a=50.0, alpha_deg=-90.0)
    R = T[:3, :3]
    assert np.allclose(R.T @ R, np.eye(3), atol=1e-6)
    assert np.isclose(np.linalg.det(R), 1.0, atol=1e-6)
    assert np.allclose(T[3, :], [0.0, 0.0, 0.0, 1.0])


def test_home_position_forward_kinematics():
    robot = KukaKR6DHModel()
    # At XHOME = [0, -90, 90, 0, 0, 0]:
    # A1 = 0, A2 = -90 (effective -180), A3 = 90 (effective 90)
    q_home = [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]
    T_home = robot.forward_flange(q_home)

    # Robot arm is symmetric in Y: Y = 0 mm
    assert np.isclose(T_home[1, 3], 0.0, atol=1e-5)
    # Z coordinate must be positive and substantial
    assert T_home[2, 3] > 400.0
    # Homogeneous bottom row
    assert np.allclose(T_home[3, :], [0.0, 0.0, 0.0, 1.0])
