import numpy as np

def skew(k: np.ndarray) -> np.ndarray:
    return np.array([
        [0.0, -k[2], k[1]],
        [k[2], 0.0, -k[0]],
        [-k[1], k[0], 0.0]
    ])

def rodrigues_forward(k: np.ndarray, theta: float) -> np.ndarray:
    k = k / np.linalg.norm(k)
    K = skew(k)
    I = np.eye(3)
    R = I + np.sin(theta) * K + (1.0 - np.cos(theta)) * (K @ K)
    return R

def rodrigues_inverse(R: np.ndarray) -> tuple[np.ndarray, float]:
    tr = np.trace(R)
    cos_theta = np.clip((tr - 1.0) / 2.0, -1.0, 1.0)
    theta = np.arccos(cos_theta)
    if np.isclose(theta, 0.0):
        return np.array([1.0, 0.0, 0.0]), 0.0
    k = np.array([
        R[2, 1] - R[1, 2],
        R[0, 2] - R[2, 0],
        R[1, 0] - R[0, 1]
    ]) / (2.0 * np.sin(theta))
    return k / np.linalg.norm(k), theta

def test_rodrigues():
    k_true = np.array([1.0, 2.0, 3.0]) / np.linalg.norm([1.0, 2.0, 3.0])
    theta_true = 1.25  # radians
    
    R = rodrigues_forward(k_true, theta_true)
    assert np.allclose(R @ R.T, np.eye(3))
    assert np.isclose(np.linalg.det(R), 1.0)
    
    k_rec, theta_rec = rodrigues_inverse(R)
    assert np.isclose(theta_true, theta_rec)
    assert np.allclose(k_true, k_rec)
    print("[SUCCESS] Rodrigues forward and inverse theorems numerically verified!")

if __name__ == "__main__":
    test_rodrigues()
