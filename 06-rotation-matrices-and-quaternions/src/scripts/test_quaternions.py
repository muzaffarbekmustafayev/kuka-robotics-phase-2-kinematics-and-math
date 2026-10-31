"""Unit tests for Euler ZYX, Quaternion transforms, and SLERP."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from quaternion_slerp import (
    euler_zyx_to_matrix,
    matrix_to_euler_zyx,
    matrix_to_quaternion,
    quaternion_to_matrix,
    quaternion_multiply,
    slerp,
)


def test_euler_to_matrix_and_back():
    orig_a, orig_b, orig_c = 45.0, 30.0, -60.0
    R = euler_zyx_to_matrix(orig_a, orig_b, orig_c)

    # SO(3) checks
    assert np.allclose(R.T @ R, np.eye(3), atol=1e-6)
    assert np.isclose(np.linalg.det(R), 1.0, atol=1e-6)

    rec_a, rec_b, rec_c = matrix_to_euler_zyx(R)
    assert np.isclose(rec_a, orig_a, atol=1e-5)
    assert np.isclose(rec_b, orig_b, atol=1e-5)
    assert np.isclose(rec_c, orig_c, atol=1e-5)


def test_matrix_quaternion_roundtrip():
    R = euler_zyx_to_matrix(15.0, -40.0, 75.0)
    q = matrix_to_quaternion(R)

    # Unit quaternion check
    assert np.isclose(np.linalg.norm(q), 1.0, atol=1e-7)

    R_rec = quaternion_to_matrix(q)
    assert np.allclose(R, R_rec, atol=1e-6)


def test_quaternion_multiplication():
    # Rotate 90 deg around Z, then 90 deg around X
    Rz = euler_zyx_to_matrix(90.0, 0.0, 0.0)
    Rx = euler_zyx_to_matrix(0.0, 0.0, 90.0)
    R_combined = Rz @ Rx

    qz = matrix_to_quaternion(Rz)
    qx = matrix_to_quaternion(Rx)
    q_prod = quaternion_multiply(qz, qx)

    R_from_prod = quaternion_to_matrix(q_prod)
    assert np.allclose(R_combined, R_from_prod, atol=1e-6)


def test_slerp_endpoints_and_midpoint():
    q1 = np.array([1.0, 0.0, 0.0, 0.0])  # Identity
    # 90 deg rotation around Z: w = cos(45) = sqrt(2)/2, z = sin(45) = sqrt(2)/2
    q2 = np.array([np.sqrt(0.5), 0.0, 0.0, np.sqrt(0.5)])

    # At t=0
    assert np.allclose(slerp(q1, q2, 0.0), q1)
    # At t=1
    assert np.allclose(slerp(q1, q2, 1.0), q2)

    # At t=0.5: should be 45 deg rotation around Z
    q_mid = slerp(q1, q2, 0.5)
    expected_mid = np.array([np.cos(np.pi / 8), 0.0, 0.0, np.sin(np.pi / 8)])
    assert np.allclose(q_mid, expected_mid, atol=1e-6)
