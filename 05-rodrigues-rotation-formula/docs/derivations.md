# Rodrigues Rotation Theorem & Matrix Exponential on SO(3)
## Matematik Isbot va KUKA KR 6 R900-2 uchun Hisoblash

### Asosiy Formula:
$$R(\vec{k}, \theta) = I + \sin(\theta) K + (1 - \cos(\theta)) K^2, \quad \text{where } K = [\vec{k}]_\times$$

---

### 1. Nazariy Asos va Teorema (Euler-Rodrigues Rotation Theorem)
Fazoda ixtiyoriy yo'nalgan birlik vektor $\vec{k} = [k_x, k_y, k_z]^T$ ($\|\vec{k}\|=1$) o'qi atrofida $\theta$ burchakka burishni ko'ramiz.

> **Teorema (Euler-Rodrigues):** 
> Ixtiyoriy $\vec{v} \in \mathbb{R}^3$ vektorining $\vec{k}$ o'qi atrofida $\theta$ burchakka burilgan $\vec{v}_{rot}$ vektori quyidagi qonuniyat bilan aniqlanadi:
> $$\vec{v}_{rot} = \vec{v}\cos\theta + (\vec{k} \times \vec{v})\sin\theta + \vec{k}(\vec{k} \cdot \vec{v})(1 - \cos\theta)$$
> Matritsaviy ko'rinishda bu burilish Maxsus Ortogonal Guruh $SO(3)$ elementi $R(\vec{k}, \theta)$ orqali ifodalanadi:
> $$R(\vec{k}, \theta) = \exp(\theta K) = I + \sin(\theta) K + (1 - \cos(\theta)) K^2$$
> bu yerda $K = [\vec{k}]_\times \in \mathfrak{so}(3)$ — qiya-simmetrik matritsadir.

### 2. Formulaning Qadam-baqadam Keltirib Chiqarilishi va Isboti
#### 2.1 Geometrik Vektorli Isbot:
1. $\vec{v}$ vektorini $\vec{k}$ ga parallel va perpendikulyar tashkil etuvchilarga ajratamiz:
   $$\vec{v}_\parallel = (\vec{k} \cdot \vec{v})\vec{k}, \quad \vec{v}_\perp = \vec{v} - \vec{v}_\parallel = \vec{v} - (\vec{k} \cdot \vec{v})\vec{k}$$
2. Burilish tekisligida ikkita ortogonal bazis vektor yasaymiz:
   * Birinchi bazis vektor: $\vec{v}_\perp$
   * Ikkinchi bazis vektor ($+90^\circ$ burilgan): $\vec{w} = \vec{k} \times \vec{v}_\perp = \vec{k} \times \vec{v}$
3. Perpendikulyar komponentaning burilgan ko'rinishi:
   $$\vec{v}_{\perp, rot} = \vec{v}_\perp \cos\theta + \vec{w} \sin\theta = (\vec{v} - (\vec{k} \cdot \vec{v})\vec{k})\cos\theta + (\vec{k} \times \vec{v})\sin\theta$$
4. Parallel komponenta burilish o'qi bo'ylab joylashgani uchun o'zgarmaydi: $\vec{v}_{\parallel, rot} = \vec{v}_\parallel = (\vec{k} \cdot \vec{v})\vec{k}$.
5. Umumiy burilgan vektor:
   $$\vec{v}_{rot} = \vec{v}_{\parallel, rot} + \vec{v}_{\perp, rot} = \vec{v}\cos\theta + (\vec{k} \times \vec{v})\sin\theta + \vec{k}(\vec{k} \cdot \vec{v})(1 - \cos\theta) \quad \blacksquare$$

#### 2.2 Lie Algebrasi va Matritsaviy Eksponensial Isboti:
$K = [\vec{k}]_\times$ matritsasining darajalarini qaraymiz. Vektorli ko'paytmaning $K^2 = \vec{k}\vec{k}^T - I$ xossasidan:
$$K^3 = -K, \quad K^4 = -K^2, \quad K^5 = K, \quad \dots$$
Matritsaviy eksponensial Teylor qatoriga yoyiladi:
$$\exp(\theta K) = \sum_{n=0}^{\infty} \frac{(\theta K)^n}{n!} = I + \left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \dots\right) K + \left(\frac{\theta^2}{2!} - \frac{\theta^4}{4!} + \dots\right) K^2$$
Sinus va kosinus Makloren qatorlarini qo'yib:
$$R = I + \sin(\theta) K + (1 - \cos(\theta)) K^2 \quad \blacksquare$$

### 3. Teskari Rodrig Transformatsiyasi (Matrix Logarithm)
Berilgan $R \in SO(3)$ matritsadan $\theta$ va $\vec{k}$ ni ajratish:
$$\text{tr}(R) = 1 + 2\cos\theta \implies \theta = \arccos\left(\frac{\text{tr}(R) - 1}{2}\right)$$
$$\vec{k} = \frac{1}{2\sin\theta} \begin{bmatrix} R_{32} - R_{23} \\ R_{13} - R_{31} \\ R_{21} - R_{12} \end{bmatrix} \quad (\text{agar } \theta \neq 0, \pi)$$

### 4. KUKA KSS va OpenCV Integratsiyasi
* OpenCV muhitidagi `cv2.Rodrigues()` aynan ushbu formulani hisoblaydi.
* KUKA KSS kontrolleri SLIN va SCIRC rejimlarida boshlang'ich orientatsiyadan yakuniy orientatsiyaga eng qisqa yo'l bilan burilishda ushbu $\vec{k}$ o'qi atrofida burchakni interpolatsiya qiladi.

