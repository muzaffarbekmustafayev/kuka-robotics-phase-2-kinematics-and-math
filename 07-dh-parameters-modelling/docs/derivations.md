# Denavit-Hartenberg (DH) Parametrlari va KUKA KR 6 R900-2 Modeli

## 1. Standart Denavit-Hartenberg Qoidalari
Standart DH konvensiyasiga ko'ra $i-1$ koordinata tizimidan $i$ koordinata tizimiga o'tish 4 ta ketma-ket elementar harakatdan iborat:

1. $Z_{i-1}$ o'qi atrofida $\theta_i$ burchakka burish;
2. $Z_{i-1}$ o'qi bo'ylab $d_i$ masofaga siljitish;
3. $X_i$ o'qi bo'ylab $a_i$ masofaga siljitish;
4. $X_i$ o'qi atrofida $\alpha_i$ burchakka burish.

Bir jinsli transformatsiya matritsasi:
$$T_i^{i-1} = \text{Rot}_z(\theta_i) \text{Trans}_z(d_i) \text{Trans}_x(a_i) \text{Rot}_x(\alpha_i)$$

$$T_i^{i-1} = \begin{bmatrix}
\cos\theta_i & -\sin\theta_i \cos\alpha_i & \sin\theta_i \sin\alpha_i & a_i \cos\theta_i \\
\sin\theta_i & \cos\theta_i \cos\alpha_i & -\sin\theta_i \sin\alpha_i & a_i \sin\theta_i \\
0 & \sin\alpha_i & \cos\alpha_i & d_i \\
0 & 0 & 0 & 1
\end{bmatrix}$$

---

## 2. KUKA KR 6 R900-2 (KR AGILUS-2) DH Parametrlar Jadvali

| O'q (i) | $\theta_i$ (offset) | $d_i$ (mm) | $a_i$ (mm) | $\alpha_i$ (gradus) |
|---|---|---|---|---|
| 1 | $\theta_1 + 0^\circ$ | 400.0 | 25.0 | $-90^\circ$ |
| 2 | $\theta_2 - 90^\circ$ | 0.0 | 455.0 | $0^\circ$ |
| 3 | $\theta_3 + 0^\circ$ | 0.0 | 35.0 | $+90^\circ$ |
| 4 | $\theta_4 + 0^\circ$ | 420.0 | 0.0 | $-90^\circ$ |
| 5 | $\theta_5 + 0^\circ$ | 0.0 | 0.0 | $+90^\circ$ |
| 6 | $\theta_6 + 0^\circ$ | 80.0 | 0.0 | $180^\circ$ |

Robot bazasidan so'nggi zvenogacha to'liq transformatsiya:
$$T_0^6 = T_1^0 \cdot T_2^1 \cdot T_3^2 \cdot T_4^3 \cdot T_5^4 \cdot T_6^5$$
