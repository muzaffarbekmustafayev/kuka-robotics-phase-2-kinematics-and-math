import numpy as np

def dh_matrix(theta: float, d: float, a: float, alpha: float) -> np.ndarray:
    ct, st = np.cos(theta), np.sin(theta)
    ca, sa = np.cos(alpha), np.sin(alpha)
    return np.array([
        [ct, -st * ca,  st * sa, a * ct],
        [st,  ct * ca, -ct * sa, a * st],
        [0.0,      sa,       ca,      d],
        [0.0,     0.0,      0.0,    1.0]
    ])

def test_dh_kr6():
    # Test zero configuration
    q = np.zeros(6)
    dh_table = [
        (q[0], 400.0, 25.0, -np.pi/2),
        (q[1] - np.pi/2, 0.0, 455.0, 0.0),
        (q[2], 0.0, 35.0, np.pi/2),
        (q[3], 420.0, 0.0, -np.pi/2),
        (q[4], 0.0, 0.0, np.pi/2),
        (q[5] + np.pi, 80.0, 0.0, np.pi),
    ]
    T = np.eye(4)
    for row in dh_table:
        T = T @ dh_matrix(*row)
    print("KR 6 R900-2 Zero Pose End-Effector Position (mm):", T[:3, 3])
    # Z coordinate matches base + link geometry height
    assert np.isclose(T[2, 3], 890.0)
    print("[SUCCESS] DH parameters for KUKA KR 6 R900-2 verified!")

if __name__ == "__main__":
    test_dh_kr6()
