# KUKA Tait-Bryan Z-Y'-X'' Intrinsic Rotation & Gimbal Lock Singularity Theorem
## Matematik Isbot va KUKA KR 6 R900-2 uchun Hisoblash

### Asosiy Formula:
$$R_{KUKA}(A, B, C) = R_z(A) R_y(B) R_x(C), \quad \text{Gimbal Lock at } B = \pm 90^\circ$$

---

### 1. Nazariy Asos va Teorema (KUKA Euler Z-Y'-X'' Konventsiyasi)
KUKA robot boshqaruv tizimida fazoviy orientatsiya uchta ichki (intrinsic) Tait-Bryan burchaklari orqali belgilanadi:
* **$A$ (Yaw):** Joriy $Z$ o'qi atrofida burilish burchagi.
* **$B$ (Pitch):** Hosil bo'lgan yangi $Y'$ o'qi atrofida burilish burchagi.
* **$C$ (Roll):** Hosil bo'lgan yakuniy $X''$ o'qi atrofida burilish burchagi.

> **Teorema (KUKA Orientatsiya Matritsasi Teoremasi):**
> KUKA ning $A, B, C$ burchaklari bo'yicha to'liq aylanish matritsasi quyidagi matritsalar ko'paytmasiga teng:
> $$R_{KUKA}(A, B, C) = R_z(A) \cdot R_y(B) \cdot R_x(C)$$
> $$R_{KUKA} = \begin{bmatrix}
> \cos A \cos B & \cos A \sin B \sin C - \sin A \cos C & \cos A \sin B \cos C + \sin A \sin C \\
> \sin A \cos B & \sin A \sin B \sin C + \cos A \cos C & \sin A \sin B \cos C - \cos A \sin C \\
> -\sin B & \cos B \sin C & \cos B \cos C
> \end{bmatrix}$$

### 2. Burchaklarni Ajratib Olish (Inverse Euler Extraction)
Berilgan $R \in SO(3)$ matritsadan $A, B, C$ burchaklarini topish:
1. $R_{31} = -\sin B$ dan:
   $$B = \text{atan2}\left(-R_{31}, \sqrt{R_{11}^2 + R_{21}^2}\right)$$
2. Agar $\cos B \neq 0$ ($B \neq \pm 90^\circ$) bo'lsa:
   $$A = \text{atan2}(R_{21}, R_{11}), \quad C = \text{atan2}(R_{32}, R_{33})$$

### 3. Gimbal Lock (Gimbal Qulflanishi) Teoremasi
> **Teorema (Gimbal Lock):**
> Agar $B = +90^\circ$ bo'lsa ($\,\cos B = 0, \sin B = 1\,$), aylanish matritsasi quyidagi degenerat shaklga keladi:
> $$R_{KUKA} = \begin{bmatrix} 0 & \sin(C - A) & \cos(C - A) \\ 0 & \cos(C - A) & -\sin(C - A) \\ -1 & 0 & 0 \end{bmatrix}$$
> Bu holatda $A$ va $C$ burchaklari bitta erkinlik darajasiga birlashadi (faqat ularning ayirmasi $C - A$ fizik ma'noga ega bo'ladi). Bir erkinlik darajasi butunlay yo'qoladi.

### 4. Kvaternionlar Orqali Bartaraf Etish (Unit Quaternions $\mathbb{H}$)
Gimbal Lock muammosini bartaraf etish uchun to'rt o'lchamli Hamilton birlik kvaternionlaridan $\mathbf{q} = [w, x, y, z]$ foydalaniladi:
$$w = \cos(\theta/2), \quad [x, y, z]^T = \vec{k} \sin(\theta/2)$$
Ikki kvaternion oralig'ida silliq burilish SLERP (Spherical Linear Interpolation) orqali hisoblanadi:
$$\text{slerp}(\mathbf{q}_1, \mathbf{q}_2; t) = \frac{\sin((1-t)\Omega)}{\sin\Omega} \mathbf{q}_1 + \frac{\sin(t\Omega)}{\sin\Omega} \mathbf{q}_2, \quad \cos\Omega = \mathbf{q}_1 \cdot \mathbf{q}_2$$

