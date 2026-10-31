# Pieper Kriteriyasi Asosida Analitik Teskari Kinematika (IK)

## 1. Kinematik ajratish (Kinematic Decoupling)
Pieper teoremasiga muvofiq, agar 6R manipulyatorning so'nggi 3 ta aylanma o'qlari ($A_4, A_5, A_6$) bitta sferik nuqtada (bilak markazi $P_w$) kesishsa, robotning teskari kinematikasi ikkita mustaqil sub-muammoga ajraladi:
1. Pozitsion qism: $A_1, A_2, A_3$ yordamida bilak markazi $P_w$ koordinatasini ta'minlash.
2. Orientatsion qism: $A_4, A_5, A_6$ yordamida asbob flanetsining talab qilingan orientatsiyasini ta'minlash.

Bilak markazi formulasi:
$$P_w = P_{tcp} - d_6 \cdot \mathbf{a}$$
bu yerda $\mathbf{a} = R_{target} \cdot [0, 0, 1]^T$ — flanetsning normal vektori.

---

## 2. Pozitsion qismni yechish ($A_1, A_2, A_3$)
1. **$A_1$ burchagi:**
   $$A_1 = \text{atan2}(P_{wy}, P_{wx}) \quad \text{yoki} \quad A_1 = \text{atan2}(-P_{wy}, -P_{wx}) \quad (2\text{ ta yechim})$$
2. **$A_3$ tirsak burchagi (Kosinuslar teoremasi):**
   $$r = \sqrt{P_{wx}^2 + P_{wy}^2} - a_1, \quad z = P_{wz} - d_1$$
   $$D = \frac{r^2 + z^2 - a_2^2 - L_4^2}{2 a_2 L_4}$$
   bu yerda $L_4 = \sqrt{a_3^2 + d_4^2}$.
   $$A_3 = \pm \arccos(D) - \delta \quad (2\text{ ta yechim: tirsak tepada / pastda})$$
3. **$A_2$ yelka burchagi:**
   $$A_2 = \text{atan2}(z, r) - \text{atan2}(L_4 \sin(A_3 + \delta), a_2 + L_4 \cos(A_3 + \delta))$$

---

## 3. Sferik bilak orientatsiyasi ($A_4, A_5, A_6$)
$$R_3^6 = (R_0^3)^T \cdot R_{target}$$
$Z-Y-Z$ yoki mos Euler dekompozitsiyasi orqali:
$$A_5 = \pm \arccos(R_{33}^{3\to 6}) \quad (2\text{ ta yechim: wrist flip / non-flip})$$
$$A_4 = \text{atan2}(R_{23}^{3\to 6}, R_{13}^{3\to 6})$$
$$A_6 = \text{atan2}(R_{32}^{3\to 6}, -R_{31}^{3\to 6})$$

Umumiy yechimlar soni: $2 \times 2 \times 2 = 8$ ta analitik konfiguratsiya.

---

## 4. KUKA Status (S) va Turn (T) Bitmasklari
KUKA kontrollerida fazodagi bitta kartesian nuqtaga bir nechta konfiguratsiyadan qaysi biri mos kelishini aniqlash uchun Status va Turn ishlatiladi:
- **Status (S, 3 bit):**
  - Bit 0: Bilak markazi z-o'qiga nisbatan holati
  - Bit 1: Yelka holati ($A_2$)
  - Bit 2: Tirsak holati ($A_3$)
- **Turn (T, 6 bit):**
  - Bit $i = 1$ agar $A_{i+1} < 0^\circ$, aks holda $0$.
