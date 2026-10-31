"""Unit tests for analytical inverse kinematics and Status/Turn masks."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from analytical_ik_pieper import AnalyticalIKSolverKR6


def test_wrist_center_decoupling():
    solver = AnalyticalIKSolverKR6()
    tcp_pos = np.array([500.0, 0.0, 400.0])
    # Target orientation: Identity matrix
    R_target = np.eye(3)
    # Approach vector is Z = [0, 0, 1]
    # P_w = [500, 0, 400] - 80 * [0, 0, 1] = [500, 0, 320]
    p_w = solver.calculate_wrist_center(tcp_pos, R_target)
    assert np.allclose(p_w, [500.0, 0.0, 320.0])


def test_solve_ik_multi_solution_count():
    solver = AnalyticalIKSolverKR6()
    # Reachable Cartesian target
    solutions = solver.solve_ik(480.0, 0.0, 435.0, 0.0, 90.0, 0.0)
    assert len(solutions) > 0
    # Solutions must have valid joint numbers
    for sol in solutions:
        assert len(sol["joints_deg"]) == 6
        assert 0 <= sol["status"] <= 7
        assert 0 <= sol["turn"] <= 63


def test_turn_bitmask_calculation():
    solver = AnalyticalIKSolverKR6()
    # If all joints are positive or zero: Turn = 0
    t_zero = solver.compute_kuka_turn([0.0, 10.0, 20.0, 30.0, 40.0, 50.0])
    assert t_zero == 0

    # If A1 and A3 are negative: bit 0 and bit 2 = 1 + 4 = 5
    t_neg = solver.compute_kuka_turn([-10.0, 10.0, -20.0, 30.0, 40.0, 50.0])
    assert t_neg == 5
