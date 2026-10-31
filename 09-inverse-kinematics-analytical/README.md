# 09-Dars: Analitik teskari kinematika (Pieper kriteriyasi va Status/Turn)
## Analytical Inverse Kinematics (Pieper's Criterion & Status/Turn)

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KR 6 R900-2 manipulyatorining sferik bilakli 6R kinematik zanjiri uchun Pieper mezoniga asoslangan to'liq yopiq shakldagi (closed-form) analitik teskari kinematika (IK) yechuvchisini ishlab chiqish, barcha 8 ta geometrik konfiguratsiya filiallarini hisoblash hamda KUKA Status (S) va Turn (T) bitmasklarini dasturiy shakllantirish.

---

### 📊 2. Natija (Result)
1. **Python Analitik IK Yechuvchisi (`analytical_ik_pieper.py`):**
   - Bilak markazini ajratish: $P_w = P_{tcp} - d_6 \cdot \mathbf{a}$.
   - Pozitsion zanjir ($A_1, A_2, A_3$) va sferik orientatsiya ($A_4, A_5, A_6$) ning mustaqil yechimi.
   - Barcha 8 ta filiallar generatsiyasi va KUKA Status ($S \in [0..7]$) hamda Turn ($T \in [0..63]$) hisoblash.
2. **KRL Verifikatsiya Dasturi (`IK_VERIFY.src` va `IK_VERIFY.dat`):**
   - E6POS formatidagi Status va Turn orqali bo'g'in burchaklarini bir qiymatli tanlash.
3. **Pytest Unit Testlari (`test_analytical_ik.py`):**
   - Dekompozitsiya, ko'p yechimli filiallarni saralash va bitmask testlari (3/3 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$P_w = P_{tcp} - d_6 \cdot \mathbf{a}$$
$$A_1 \in \{\text{atan2}(P_{wy}, P_{wx}), \text{atan2}(-P_{wy}, -P_{wx})\}$$
$$A_3 = \pm \arccos(D) - \delta$$
$$A_5 = \pm \arccos(R_{33}^{3\to 6})$$

Batafsil isbotlar [**docs/derivations.md**](./docs/derivations.md) da keltirilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python yechuvchisini ishga tushirish:
```bash
uv run --with numpy python src/scripts/analytical_ik_pieper.py
```

Konsol chiqishi:
```
=================================================================
Lesson 09: Analytical Inverse Kinematics (IK) & Pieper's Method
=================================================================

Target Cartesian Pose: X=480.0mm, Y=0.0mm, Z=435.0mm, A=0.0°, B=90.0°, C=0.0°
Total Analytical Solutions Found: 8
  Sol #1: Q = [0.0, 15.63, 76.54, 0.0, 45.0, 0.0] | Status S=0, Turn T=0
  Sol #2: Q = [0.0, 15.63, 76.54, 0.0, -45.0, 0.0] | Status S=4, Turn T=16
...
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_analytical_ik.py
```
Natija: `3 passed in 0.11s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
