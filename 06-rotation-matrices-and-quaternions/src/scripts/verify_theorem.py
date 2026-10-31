import numpy as np

def euler_kuka_to_matrix(A: float, B: float, C: float) -> np.ndarray:
    cA, sA = np.cos(A), np.sin(A)
    cB, sB = np.cos(B), np.sin(B)
    cC, sC = np.cos(C), np.sin(C)
    
    Rz = np.array([[cA, -sA, 0], [sA, cA, 0], [0, 0, 1]])
    Ry = np.array([[cB, 0, sB], [0, 1, 0], [-sB, 0, cB]])
    Rx = np.array([[1, 0, 0], [0, cC, -sC], [0, sC, cC]])
    return Rz @ Ry @ Rx

def matrix_to_euler_kuka(R: np.ndarray) -> tuple[float, float, float]:
    B = np.arctan2(-R[2, 0], np.sqrt(R[0, 0]**2 + R[1, 0]**2))
    if not np.isclose(np.cos(B), 0.0):
        A = np.arctan2(R[1, 0], R[0, 0])
        C = np.arctan2(R[2, 1], R[2, 2])
    else:
        # Gimbal lock: set C = 0
        C = 0.0
        A = np.arctan2(-R[0, 1], R[1, 1])
    return A, B, C

def test_kuka_euler():
    A_in, B_in, C_in = np.radians(45.0), np.radians(30.0), np.radians(-60.0)
    R = euler_kuka_to_matrix(A_in, B_in, C_in)
    A_out, B_out, C_out = matrix_to_euler_kuka(R)
    assert np.allclose([A_in, B_in, C_in], [A_out, B_out, C_out])
    print("[SUCCESS] KUKA Euler Z-Y'-X' conversion verified!")

if __name__ == "__main__":
    test_kuka_euler()
