"""Unit tests for Rodrigues' rotation formula and SO(3) matrix properties."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from rodrigues_rotations import (
    skew_symmetric,
    rodrigues_formula,
    logarithmic_map_so3,
    rotate_vector,
    is_valid_so3,
)


def test_skew_symmetric_properties():
    k = np.array([1.0, 2.0, 3.0])
    K = skew_symmetric(k)
    # Skew symmetry: K^T = -K
    assert np.allclose(K.T, -K)
    # Zero diagonal
    assert np.allclose(np.diag(K), [0.0, 0.0, 0.0])
    # Cross product equivalence: K @ v == cross(k, v)
    v = np.array([4.0, 5.0, 6.0])
    assert np.allclose(K @ v, np.cross(k, v))


def test_rodrigues_elementary_rotations():
    # 90 degrees around Z axis
    z_axis = np.array([0.0, 0.0, 1.0])
    R_z_90 = rodrigues_formula(z_axis, np.pi / 2.0)
    expected_R_z = np.array([
        [0.0, -1.0, 0.0],
        [1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0]
    ])
    assert np.allclose(R_z_90, expected_R_z, atol=1e-6)
    assert is_valid_so3(R_z_90)


def test_rodrigues_and_vector_rotation_equivalence():
    axis = np.array([0.57735, 0.57735, 0.57735])
    theta = np.radians(45.0)
    v = np.array([10.0, -5.0, 2.0])

    R = rodrigues_formula(axis, theta)
    v_rot_mat = R @ v
    v_rot_vec = rotate_vector(v, axis, theta)
    assert np.allclose(v_rot_mat, v_rot_vec, atol=1e-6)


def test_logarithmic_map_inverse():
    axis = np.array([0.0, 1.0, 0.0])  # Y axis
    angle = np.radians(35.0)

    R = rodrigues_formula(axis, angle)
    recovered_axis, recovered_angle = logarithmic_map_so3(R)

    assert np.isclose(recovered_angle, angle, atol=1e-5)
    assert np.allclose(recovered_axis, axis, atol=1e-5)


def test_identity_rotation():
    axis = np.array([0.0, 0.0, 1.0])
    R_zero = rodrigues_formula(axis, 0.0)
    assert np.allclose(R_zero, np.eye(3))
    rec_axis, rec_angle = logarithmic_map_so3(R_zero)
    assert np.isclose(rec_angle, 0.0)
