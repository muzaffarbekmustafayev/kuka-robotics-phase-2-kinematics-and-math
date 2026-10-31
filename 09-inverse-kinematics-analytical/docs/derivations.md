# Pieper's Closed-Form Inverse Kinematics Theorem for Spherical Wrists
## Matematik Isbot va KUKA KR 6 R900-2 uchun Hisoblash

### Asosiy Formula:
$$\vec{p}_{wc} = \vec{p}_e - d_6 \vec{a}, \quad R_3^6 = (R_0^3)^T R_{target}$$

---

### 1. Nazariy Asos va Teorema (Pieper Kriteriyasi)
6 erkinlik darajali robot manipulyatorlari uchun umumiy holda teskari kinematika 16-darajali polinomial tenglamaga olib keladi.

> **Teorema (Pieper Kriteriyasi):**
> Agar manipulyatorning oxirgi uchta bo'g'in o'qi ($A_4, A_5, A_6$) bitta umumiy nuqtada (sferik bilak markazi — Wrist Center $\vec{p}_{wc}$) kesishsa, 6-DoF teskari kinematika masalasi to'liq analitik (yopiq shaklda) ikkita mustaqil qismga ajraladi (decoupling):
> 1. **Pozitsiyani ajratish:** Birinchi 3 ta bo'g'in ($q_1, q_2, q_3$) faqat bilak markazi pozitsiyasini $\vec{p}_{wc}$ ta'minlaydi.
> 2. **Orientatsiyani ajratish:** Qolgan 3 ta bilak bo'g'ini ($q_4, q_5, q_6$) faqat effektor yo'nalishini ta'minlaydi.

### 2. Qadam-baqadam Matematik Keltirib Chiqarilishi
#### 2.1 Bilak Markazini Topish:
Effektorning maqsadli holati berilgan: $T_{target} = \begin{bmatrix} R_{target} & \vec{p}_e \\ \vec{0}^T & 1 \end{bmatrix}$.
Effektorning yaqinlashish vektori (approach vector) $\vec{a} = R_{target}[:, 2]$ (3-ustun).
Sferik bilak markazi $\vec{p}_{wc}$:
$$\vec{p}_{wc} = \vec{p}_e - d_6 \vec{a}$$

#### 2.2 Birinchi Bo'g'in Burchagi $q_1$:
$$\theta_1 = \text{atan2}(p_{wc, y}, p_{wc, x})$$
Ikkinchi yechim: $q_1' = q_1 + \pi$ (orqaga burilish).

#### 2.3 $q_2$ va $q_3$ Burchaklari (Tirsak baland/past):
Planar 2 zvenoli geometriyada kosinuslar teoremasidan:
$$r^2 = p_{wc, x}^2 + p_{wc, y}^2 - a_1^2, \quad s = p_{wc, z} - d_1$$
$$D = \frac{r^2 + s^2 - a_2^2 - (a_3^2 + d_4^2)}{2 a_2 \sqrt{a_3^2 + d_4^2}}$$
$$q_3 = \text{atan2}(\pm \sqrt{1 - D^2}, D) - \text{atan2}(a_3, d_4)$$
Bu 2 ta yechim beradi: **Elbow Up** va **Elbow Down**.
So'ngra $q_2$ trigonometrik tarzda aniqlanadi.

#### 2.4 Bilak Burchaklari ($q_4, q_5, q_6$):
Birinchi uchta bo'g'in burchaklari ma'lum bo'lgach, $R_0^3(q_1, q_2, q_3)$ matritsasi hisoblanadi:
$$R_3^6 = (R_0^3)^T \cdot R_{target}$$
$R_3^6$ sferik bilakning $Z-Y-Z$ yoki $X-Y-X$ ekvivalent aylanishi bo'lgani sababli:
$$q_5 = \pm \arccos(R_{33}^{36})$$
$$q_4 = \text{atan2}(R_{23}^{36}, R_{13}^{36}), \quad q_6 = \text{atan2}(R_{32}^{36}, -R_{31}^{36})$$
Bu 2 ta yechim beradi: **Wrist Flip** ($q_5 > 0$) va **Wrist No-Flip** ($q_5 < 0$).

### 3. Jami 8 Ta Yechim va KUKA Status ($S$) hamda Turn ($T$)
Jami analitik yechimlar soni: $2 (q_1) \times 2 (q_3) \times 2 (q_5) = 8$ ta.
KUKA KSS tizimida ushbu yechimlardan aynan qaysi birini tanlash **Status ($S$)** butun sonining 3 ta biti orqali boshqariladi:
* **Bit 0:** $p_{wc, z} < \text{shoulder level}$ (overhead)
* **Bit 1:** $q_3$ Elbow Up / Down
* **Bit 2:** $q_5$ Wrist Flip / No-flip
**Turn ($T$)** esa har bir o'qning manfiy diapazonda ekanligini bildiradi ($q_i < 0$).

