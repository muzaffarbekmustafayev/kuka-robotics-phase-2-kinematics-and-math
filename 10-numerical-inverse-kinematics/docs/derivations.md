# Sonli teskari kinematika (Numerical Inverse Kinematics) va DLS usuli

## 1. Yechish Formulirovkasi
To'g'ri kinematika akslantirishi $f: \mathbb{R}^6 \to SE(3)$ chiziqsiz funksiya hisoblanadi:
$$\mathbf{x} = f(\mathbf{q})$$

Fazodagi berilgan maqsad $\mathbf{x}_{target}$ uchun xatolik funksiyasi:
$$\mathbf{e}(\mathbf{q}) = \begin{bmatrix} \mathbf{p}_{target} - \mathbf{p}(\mathbf{q}) \\ \mathbf{e}_{rot}(\mathbf{q}) \end{bmatrix} \in \mathbb{R}^6$$

bu yerda orientatsiya xatosi:
$$\mathbf{e}_{rot} = \frac{1}{2} \left( \mathbf{n} \times \mathbf{n}_d + \mathbf{s} \times \mathbf{s}_d + \mathbf{a} \times \mathbf{a}_d \right)$$

---

## 2. Newton-Raphson usuli va Yaqobi matritsasi
Teylor qatoriga yoyish orqali:
$$\mathbf{e}(\mathbf{q} + \Delta \mathbf{q}) \approx \mathbf{e}(\mathbf{q}) - J(\mathbf{q}) \Delta \mathbf{q} = \mathbf{0}$$
$$J(\mathbf{q}) \Delta \mathbf{q} = \mathbf{e}(\mathbf{q})$$

Agar $J$ kvadrat va maxsusmas bo'lsa:
$$\Delta \mathbf{q} = J^{-1} \mathbf{e}$$
Umumiy holda Mur-Penrouz psevdo-teskarisi:
$$J^\dagger = J^T (J J^T)^{-1}$$
$$\mathbf{q}_{k+1} = \mathbf{q}_k + \alpha J^\dagger \mathbf{e}(\mathbf{q}_k)$$

---

## 3. Levenberg-Marquardt Damped Least Squares (DLS)
Singulyarlik ($\det(J) \approx 0$) yaqinida $J^\dagger$ cheksizlikka intilib, robot bo'g'inlarida keskin tebranishlar va buzilishlarga olib keladi. Buni bartaraf qilish uchun Damped Least Squares minimallashtirish mezonidan foydalaniladi:

$$\min_{\Delta \mathbf{q}} \left( \|J \Delta \mathbf{q} - \mathbf{e}\|^2 + \lambda^2 \|\Delta \mathbf{q}\|^2 \right)$$

Ushbu optimallash masalasining analitik yechimi:
$$\mathbf{\Delta q = J^T (J J^T + \lambda^2 I)^{-1} e}$$

bu yerda $\lambda > 0$ — so'ndirish (damping) koeffitsienti.
- Singulyarlikdan uzoqda ($\sigma_{min} \gg 0$): $\lambda \to 0$ bo'lib, standart Nyuton konvergentsiyasi ta'minlanadi.
- Singulyarlik yaqinida: $\lambda$ qadami cheklab, bo'g'in tezliklarining sakrab ketishini oldini oladi.
