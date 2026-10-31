# 06-Dars: Aylanish matritsalari, Kvaternionlar va SLERP interpolyatsiyasi
## Rotation Matrices, Quaternions & SLERP Trajectory Interpolation

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA sanoat robotlarida fazoviy orientatsiyani ifodalovchi intrinsic $Z-Y'-X''$ (A, B, C) Euler burchaklari, ortogonal $SO(3)$ matritsalari hamda $\mathbb{S}^3$ birlik kvaternionlari orasidagi to'g'ri va teskari almashtirishlarni qurish, Gimbal Lock (singulyarlik) muammosini tahlil qilish va robot flanetsining silliq harakat trayektoriyasini ta'minlovchi SLERP (Spherical Linear Interpolation) algoritmini yaratish.

---

### 📊 2. Natija (Result)
1. **Python Dasturi (`quaternion_slerp.py`):**
   - KUKA Euler $A, B, C \leftrightarrow R \in SO(3)$ konvertori (Gimbal Lock $B = \pm 90^\circ$ holati boshqaruvi bilan).
   - Shepperd algoritmi asosida yuqori aniqlikdagi $R \leftrightarrow \mathbf{q} \in \mathbb{S}^3$ aylantirish.
   - Hamilton ko'paytmasi ($\mathbf{q}_1 \otimes \mathbf{q}_2$).
   - SLERP interpolyatsiyasi (eng qisqa geodezik aylanish yo'li kafolatlangan).
2. **Pytest Unit Testlari (`test_quaternions.py`):**
   - Ortogonallik, teskari aylanuvchanlik va SLERP oraliq nuqtalari uchun 100% muvaffaqiyatli testlar (4/4 o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

#### 3.1. KUKA Euler Burchaklari Matritsasi:
$$R = R_z(A) R_y(B) R_x(C)$$

#### 3.2. SLERP Formulasi:
$$\text{SLERP}(\mathbf{q}_1, \mathbf{q}_2, t) = \frac{\sin((1-t)\Omega)}{\sin\Omega}\mathbf{q}_1 + \frac{\sin(t\Omega)}{\sin\Omega}\mathbf{q}_2, \quad \cos\Omega = \mathbf{q}_1 \cdot \mathbf{q}_2$$

To'liq isbotlar va Shepperd tenglamalari [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python skriptini tekshirish:
```bash
uv run --with numpy python src/scripts/quaternion_slerp.py
```

Konsol chiqishi:
```
=================================================================
Lesson 06: Rotation Matrices, Quaternions & SLERP Interpolation
=================================================================

Start Euler (A, B, C): (30.0, 45.0, -20.0)
End Euler   (A, B, C): (120.0, -15.0, 60.0)

Quaternion Start q_A: [0.8988 0.0543 0.3923 0.1947]

SLERP Trajectory (5 Waypoints):
  Step 0 (t=0.00): A= 30.00°, B= 45.00°, C=-20.00°
  Step 1 (t=0.25): A= 51.52°, B= 32.74°, C= -1.61°
  Step 2 (t=0.50): A= 73.19°, B= 18.57°, C= 17.59°
  Step 3 (t=0.75): A= 95.84°, B=  2.55°, C= 38.07°
  Step 4 (t=1.00): A=120.00°, B=-15.00°, C= 60.00°
```

Avtomatlashtirilgan testlarni tekshirish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_quaternions.py
```
Natija: `4 passed in 0.11s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
