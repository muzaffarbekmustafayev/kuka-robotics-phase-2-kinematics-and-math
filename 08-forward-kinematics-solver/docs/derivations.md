# To'g'ri kinematika masalasi (FK) va KUKA Euler burchaklari

## 1. Zanjirli bir jinsli matritsalar ko'paytmasi
Berilgan bo'g'in burchaklari vektori $\mathbf{q} = [A_1, A_2, A_3, A_4, A_5, A_6]^T$ uchun robot bazasidan asbob flanetsigacha bo'lgan to'liq transformatsiya:

$$T_0^6(\mathbf{q}) = A_1(A_1) \cdot A_2(A_2) \cdot A_3(A_3) \cdot A_4(A_4) \cdot A_5(A_5) \cdot A_6(A_6)$$

bu yerda $T_0^6 \in SE(3)$ quyidagi blok strukturasiga ega:
$$T_0^6 = \begin{bmatrix}
r_{11} & r_{12} & r_{13} & P_x \\
r_{21} & r_{22} & r_{23} & P_y \\
r_{31} & r_{32} & r_{33} & P_z \\
0 & 0 & 0 & 1
\end{bmatrix}$$

---

## 2. KUKA Kartesian burchaklarini $(A, B, C)$ ajratib olish (Extraction)
KUKA $Z-Y'-X''$ tizimi bo'yicha:
$$r_{31} = -\sin B \implies B = \arcsin(-r_{31}) = \text{atan2}\left(-r_{31}, \sqrt{r_{11}^2 + r_{21}^2}\right)$$

Agar $\cos B \neq 0$:
$$A = \text{atan2}(r_{21}, r_{11})$$
$$C = \text{atan2}(r_{32}, r_{33})$$

Singulyarlik holatida ($B = \pm 90^\circ$):
$$C = 0^\circ, \quad A = \text{atan2}(r_{12}, r_{22}) \quad (\text{yoki } \text{atan2}(-r_{12}, r_{22}))$$

---

## 3. Asbob (Tool) va Baza (Base) kengaytmasi
Robotga ishchi asbob ($T_{flange}^{tool}$) va ishchi stol bazasi ($T_{world}^{base}$) biriktirilganda:
$$T_{world}^{tcp} = T_{world}^{base} \cdot T_{base}^{flange}(\mathbf{q}) \cdot T_{flange}^{tool}$$
KRL da bu geometrik operator `:` orqali yoziladi: `$POS_ACT = BASE : T_0_6 : TOOL`.
