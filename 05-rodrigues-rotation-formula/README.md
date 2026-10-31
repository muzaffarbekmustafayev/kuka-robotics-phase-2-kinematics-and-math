# 05-Dars: Fazoviy burilishlar va Rodrigues aylantirish formulasi
## Spatial Rotations & Rodrigues Rotation Formula

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
3D fazoda ixtiyoriy birlik vektor $\mathbf{k} \in \mathbb{R}^3$ ($\|\mathbf{k}\| = 1$) atrofida $\theta$ burchakka burishni Rodrigues formulasiga ko'ra analitik hisoblash, $\mathfrak{so}(3)$ Lie algebrasidan $SO(3)$ Lie guruhiga matritsaviy eksponenta akslantirishini ($\exp(\theta [\mathbf{k}]_\times)$) amalga oshirish hamda teskari logarifmik akslantirish (o'q va burchakni qayta tiklash) algoritmini yaratish.

---

### 📊 2. Natija (Result)
1. **Python Algoritmi (`rodrigues_rotations.py`):**
   - $\mathfrak{so}(3)$ qiyshiq simmetrik tenzori $K = [\mathbf{k}]_\times$ generatori.
   - Analitik Rodrigues formulasi: $R = I + (\sin\theta)K + (1 - \cos\theta)K^2$.
   - Vektorli to'g'ridan-to'g'ri burish: $\mathbf{v}_{rot} = \mathbf{v}\cos\theta + (\mathbf{k} \times \mathbf{v})\sin\theta + \mathbf{k}(\mathbf{k} \cdot \mathbf{v})(1 - \cos\theta)$.
   - Teskari logarifmik xarita: $R \in SO(3) \to (\mathbf{k}, \theta)$.
2. **Pytest Unit Testlari (`test_rodrigues.py`):**
   - Ortogonallik ($R^T R = I$), birlik determinant ($\det R = +1$), bazaviy o'qlar va ixtiyoriy fazoviy o'qlar uchun 100% test qamrovi (5/5 o'tdi).

---

### 🧮 3. Matematik apparat va Isbot (Mathematics & Proof)

#### 3.1. Rodrigues formulasi:
$$R(\mathbf{k}, \theta) = I + (\sin\theta) K + (1 - \cos\theta) K^2$$
bu yerda:
$$K = [\mathbf{k}]_\times = \begin{bmatrix} 0 & -k_z & k_y \\ k_z & 0 & -k_x \\ -k_y & k_x & 0 \end{bmatrix}$$

#### 3.2. Asosiy Teorema (Eksponensial qator qisqarishi):
$K^3 = -K$ xossasidan kelib chiqib, Teylor-Meyklorin qatori orqali:
$$\exp(\theta K) = \sum_{m=0}^\infty \frac{(\theta K)^m}{m!} = I + (\sin\theta) K + (1 - \cos\theta) K^2$$

To'liq qadam-baqadam isbot [**docs/derivations.md**](./docs/derivations.md) faylida keltirilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python skriptini tekshirish:
```bash
uv run --with numpy python src/scripts/rodrigues_rotations.py
```

Konsol chiqishi:
```
=================================================================
Lesson 05: Rodrigues Rotation Formula & SO(3) Lie Algebra
=================================================================

Rotation Matrix R for axis [1. 1. 1.] by 60.0°:
[[ 0.6667 -0.3333  0.6667]
 [ 0.6667  0.6667 -0.3333]
 [-0.3333  0.6667  0.6667]]
Is valid SO(3) matrix: True

Original vector v: [1. 0. 0.]
Rotated via Matrix R @ v:       [ 0.6667  0.6667 -0.3333]
Rotated via Vector Formula:      [ 0.6667  0.6667 -0.3333]
Match: True

Inverse Logarithmic Map Recovered:
  Axis: [0.5774 0.5774 0.5774] (Original: [0.5774 0.5774 0.5774])
  Angle: 60.00° (Original: 60.00°)
```

Unit testlarni ishga tushirish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_rodrigues.py
```
Natija: `5 passed in 0.11s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
