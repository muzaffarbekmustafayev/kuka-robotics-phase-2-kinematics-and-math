# Rodrigues formulasi va so(3) Lie algebrasining matematik isboti

## 1. Qiyshiq simmetrik (Skew-symmetric) operatorlar va xossalari
Birlik vektor $\mathbf{k} = [k_x, k_y, k_z]^T$ ($\|\mathbf{k}\| = 1$) uchun vektor ko'paytmasi operatori:
$$K = [\mathbf{k}]_\times = \begin{bmatrix} 0 & -k_z & k_y \\ k_z & 0 & -k_x \\ -k_y & k_x & 0 \end{bmatrix} \in \mathfrak{so}(3)$$

Ixtiyoriy $\mathbf{v} \in \mathbb{R}^3$ uchun:
$$K \mathbf{v} = \mathbf{k} \times \mathbf{v}$$

### Lemma 1 (K darajalari rekkurentligi):
$$K^2 = \mathbf{k} \mathbf{k}^T - I$$
$$K^3 = K^2 K = (\mathbf{k} \mathbf{k}^T - I) K = \mathbf{k} (\mathbf{k}^T K) - K = -K$$
Chunki $\mathbf{k}^T K = (\mathbf{k} \times \mathbf{k})^T = \mathbf{0}^T$.
Demak, ixtiyoriy $n \ge 1$ uchun:
$$K^{2n+1} = (-1)^n K$$
$$K^{2n+2} = (-1)^n K^2$$

---

## 2. Teorema: Matritsaviy eksponenta orqali Rodrigues formulasini keltirib chiqarish

Aylanish matritsasi Lie algebrasi generatorining eksponentasi sifatida aniqlanadi:
$$R(\mathbf{k}, \theta) = \exp(\theta K) = \sum_{m=0}^{\infty} \frac{(\theta K)^m}{m!} = I + \theta K + \frac{\theta^2 K^2}{2!} + \frac{\theta^3 K^3}{3!} + \frac{\theta^4 K^4}{4!} + \dots$$

Juft va toq darajalarni ajratamiz:
$$\exp(\theta K) = I + \left( \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \dots \right) K + \left( \frac{\theta^2}{2!} - \frac{\theta^4}{4!} + \frac{\theta^6}{6!} - \dots \right) K^2$$

Meyklorin qatorlariga binoan:
$$\sin\theta = \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \dots$$
$$1 - \cos\theta = \frac{\theta^2}{2!} - \frac{\theta^4}{4!} + \frac{\theta^6}{6!} - \dots$$

Natijada:
$$\mathbf{R(\mathbf{k}, \theta) = I + (\sin\theta) K + (1 - \cos\theta) K^2}$$
Isbot yakunlandi. $\blacksquare$

---

## 3. Logarifmik akslantirish (Inverse Rodrigues / Log Map)
Berilgan $R \in SO(3)$ matritsasidan o'q $\mathbf{k}$ va burchak $\theta$ ni tiklash:

$$\text{Tr}(R) = 1 + 2\cos\theta \implies \cos\theta = \frac{\text{Tr}(R) - 1}{2}$$
$$\theta = \arccos\left(\frac{\text{Tr}(R) - 1}{2}\right)$$
Agar $\theta \neq 0$ va $\theta \neq \pi$:
$$R - R^T = 2\sin\theta K \implies \mathbf{k} = \frac{1}{2\sin\theta} \begin{bmatrix} R_{32} - R_{23} \\ R_{13} - R_{31} \\ R_{21} - R_{12} \end{bmatrix}$$
