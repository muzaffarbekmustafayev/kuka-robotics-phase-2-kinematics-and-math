# Denavit-Hartenberg (DH) Theorem for Serial Chains & KR 6 R900-2 Parameter Derivation
## Matematik Isbot va KUKA KR 6 R900-2 uchun Hisoblash

### Asosiy Formula:
$$A_i = \text{Rot}(z, \theta_i) \text{Trans}(z, d_i) \text{Trans}(x, a_i) \text{Rot}(x, \alpha_i)$$

---

### 1. Nazariy Asos va Teorema (Denavit-Hartenberg Teoremasi)
Ixtiyoriy ochiq kinematik zanjirda ketma-ket joylashgan ikkita bo'g'in koordinatalar tizimini bog'lash uchun quyidagi teorema o'rinli:

> **Teorema (Denavit-Hartenberg):**
> Agar $\{i-1\}$ va $\{i\}$ koordinatalar tizimlari quyidagi ikki shartni qanoatlantirsa:
> 1. $x_i$ o'qi $z_{i-1}$ o'qiga perpendikulyar: $x_i \perp z_{i-1}$
> 2. $x_i$ o'qi $z_{i-1}$ o'qi bilan kesishadi
> U holda $\{i-1\}$ tizimdan $\{i\}$ tizimga o'tish to'rtta parametr ($a_i, \alpha_i, d_i, \theta_i$) orqali bir qiymatli ifodalanadi:
> $$A_i = \text{Rot}(z, \theta_i) \cdot \text{Trans}(z, d_i) \cdot \text{Trans}(x, a_i) \cdot \text{Rot}(x, \alpha_i)$$
> $$A_i = \begin{bmatrix}
> \cos\theta_i & -\sin\theta_i \cos\alpha_i & \sin\theta_i \sin\alpha_i & a_i \cos\theta_i \\
> \sin\theta_i & \cos\theta_i \cos\alpha_i & -\cos\theta_i \sin\alpha_i & a_i \sin\theta_i \\
> 0 & \sin\alpha_i & \cos\alpha_i & d_i \\
> 0 & 0 & 0 & 1
> \end{bmatrix}$$

### 2. KUKA KR 6 R900-2 Rasmiy DH Parametrlarining Keltirib Chiqarilishi
KUKA KR AGILUS (KR 6 R900-2) zavod chizmalaridan olingan o'lchamlar:
* Asos balandligi: $d_1 = 400.0\text{ mm}$
* Yelka ofseti: $a_1 = 25.0\text{ mm}$, burilish burchagi $\alpha_1 = -90^\circ$ ($-\pi/2$)
* Yuqori qo'l uzunligi: $a_2 = 455.0\text{ mm}$, $\alpha_2 = 0^\circ$
* Tirsak ofseti: $a_3 = 35.0\text{ mm}$, bilak masofasi: $d_4 = 420.0\text{ mm}$, $\alpha_3 = +90^\circ$ ($+\pi/2$)
* Bilak kesishmasi: $a_4 = 0, \alpha_4 = -90^\circ$, $a_5 = 0, d_5 = 0, \alpha_5 = +90^\circ$
* Flanets masofasi: $d_6 = 80.0\text{ mm}$ (sferik bilak markazidan mexanik flanetsgacha)

| Bo'g'in $i$ | $\theta_i$ | $d_i\text{ [mm]}$ | $a_i\text{ [mm]}$ | $\alpha_i$ | Cheklovlar |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $q_1$ | $400.0$ | $25.0$ | $-\pi/2$ | $\pm 170^\circ$ |
| **2** | $q_2 - \pi/2$ | $0.0$ | $455.0$ | $0$ | $-190^\circ / +45^\circ$ |
| **3** | $q_3$ | $0.0$ | $35.0$ | $+\pi/2$ | $-120^\circ / +156^\circ$ |
| **4** | $q_4$ | $420.0$ | $0.0$ | $-\pi/2$ | $\pm 185^\circ$ |
| **5** | $q_5$ | $0.0$ | $0.0$ | $+\pi/2$ | $\pm 120^\circ$ |
| **6** | $q_6 + \pi$ | $80.0$ | $0.0$ | $\pi$ | $\pm 350^\circ$ |

