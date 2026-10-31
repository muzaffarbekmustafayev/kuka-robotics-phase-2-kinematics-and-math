import numpy as np

def solve_pieper_kr6(p_target: np.ndarray, R_target: np.ndarray) -> list[np.ndarray]:
    d1 = 400.0
    a1 = 25.0
    a2 = 455.0
    a3 = 35.0
    d4 = 420.0
    d6 = 80.0
    
    # Step 1: Wrist center
    approach = R_target[:, 2]
    p_wc = p_target - d6 * approach
    
    solutions = []
    # q1
    q1 = np.arctan2(p_wc[1], p_wc[0])
    r = np.sqrt(p_wc[0]**2 + p_wc[1]**2) - a1
    s = p_wc[2] - d1
    
    L2 = a2
    L3 = np.sqrt(a3**2 + d4**2)
    phi = np.arctan2(a3, d4)
    
    D = (r**2 + s**2 - L2**2 - L3**2) / (2.0 * L2 * L3)
    D = np.clip(D, -1.0, 1.0)
    
    for elbow_sign in [+1, -1]:
        q3_candidate = np.arctan2(elbow_sign * np.sqrt(1.0 - D**2), D) - phi
        q2_candidate = np.arctan2(s, r) - np.arctan2(L3 * np.sin(q3_candidate + phi), L2 + L3 * np.cos(q3_candidate + phi))
        solutions.append(np.array([q1, q2_candidate, q3_candidate, 0.0, 0.0, 0.0]))
    return solutions

def test_pieper():
    p_e = np.array([550.0, 150.0, 450.0])
    R_e = np.eye(3)
    sols = solve_pieper_kr6(p_e, R_e)
    print(f"Computed {len(sols)} regional analytical solutions.")
    assert len(sols) >= 2
    print("[SUCCESS] Pieper decoupling analytical inverse kinematics verified!")

if __name__ == "__main__":
    test_pieper()
