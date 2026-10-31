# KUKA Z-Y-X Euler burchaklari, Kvaternionlar va SLERP interpolyatsiyasi

## 1. KUKA Intrinsic Euler burchaklari (A, B, C)
KUKA tizimida fazoviy yo'nalish $Z-Y'-X''$ ketma-ketlikdagi burilishlar bilan ifodalanadi:
$$R = R_z(A) R_y(B) R_x(C)$$

bu yerda:
- $A$ (Z o'qi atrofida yaw / kurs burchagi);
- $B$ (Yangi $Y'$ o'qi atrofida pitch / tangaj burchagi);
- $C$ (Yangi $X''$ o'qi atrofida roll / kren burchagi).

Matritsa ko'rinishi:
$$R = \begin{bmatrix}
\cos A \cos B & \cos A \sin B \sin C - \sin A \cos C & \cos A \sin B \cos C + \sin A \sin C \\
\sin A \cos B & \sin A \sin B \sin C + \cos A \cos C & \sin A \sin B \cos C - \cos A \sin C \\
-\sin B & \cos B \sin C & \cos B \cos C
\end{bmatrix}$$

### Gimbal Lock singulyarligi:
Agar $\cos B = 0$ bo'lsa ($B = \pm 90^\circ$), $Z$ va $X''$ o'qlari kollinear bo'lib qoladi va bitta erkinlik darajasi yo'qoladi (Gimbal Lock).

---

## 2. Birlik kvaternionlar ($\mathbb{S}^3$) va Shepperd algoritmi
Birlik kvaternion $\mathbf{q} = [w, x, y, z]^T \in \mathbb{S}^3$:
$$\|\mathbf{q}\|^2 = w^2 + x^2 + y^2 + z^2 = 1$$
$$w = \cos\frac{\theta}{2}, \quad [x, y, z]^T = \mathbf{k} \sin\frac{\theta}{2}$$

Kvaterniondan $SO(3)$ ga o'tish:
$$R(\mathbf{q}) = \begin{bmatrix}
1 - 2(y^2+z^2) & 2(xy - zw) & 2(xz + yw) \\
2(xy + zw) & 1 - 2(x^2+z^2) & 2(yz - xw) \\
2(xz - yw) & 2(yz + xw) & 1 - 2(x^2+y^2)
\end{bmatrix}$$

---

## 3. SLERP (Spherical Linear Interpolation) teoremasi

Ikki birlik kvaternion $\mathbf{q}_1$ va $\mathbf{q}_2$ orasidagi 4D giperfaza bo'yicha doimiy burchak tezlikli silliq interpolyatsiya:

$$\text{SLERP}(\mathbf{q}_1, \mathbf{q}_2, t) = \frac{\sin((1-t)\Omega)}{\sin\Omega}\mathbf{q}_1 + \frac{\sin(t\Omega)}{\sin\Omega}\mathbf{q}_2$$

bu yerda:
$$\cos\Omega = \mathbf{q}_1 \cdot \mathbf{q}_2 = w_1 w_2 + x_1 x_2 + y_1 y_2 + z_1 z_2$$

Agar $\mathbf{q}_1 \cdot \mathbf{q}_2 < 0$ bo'lsa, antipodal nuqta orqali eng qisqa aylanish masofasi (geodesic distance) tanlanadi: $\mathbf{q}_2 \to -\mathbf{q}_2$.
