# 08-Dars: To'g'ri kinematika (Forward Kinematics) yechuvchisi
## Forward Kinematics (FK) Solver for KUKA KR 6 R900-2

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KR 6 R900-2 sanoat manipulyatorining 6 ta bo'g'in burchaklari $\mathbf{q} = [A_1, A_2, A_3, A_4, A_5, A_6]^T$ berilganida uning yakuniy ishchi flanetsi (TCP) fazoviy holatini $T_0^6 \in SE(3)$ transformatsiya matritsasi va KUKA $\{X, Y, Z, A, B, C\}$ koordinatalari ko'rinishida analitik hisoblash hamda KRL dasturi bilan solishtirish.

---

### 📊 2. Natija (Result)
1. **Python To'g'ri Kinematika Dasturi (`forward_kinematics.py`):**
   - 6 o'qning DH parametrlari asosida zanjirli bir jinsli transformatsiya.
   - Kartesian $\{X, Y, Z\}$ pozitsiyasi va $\{A, B, C\}$ orientatsiyalarini aniqlash.
2. **KRL Verifikatsiya Dasturi (`FK_CHECK.src` va `FK_CHECK.dat`):**
   - KUKA kontrolleri ichidagi `$POS_ACT` bilan Python analitik modeli qiymatlarini solishtirish.
3. **Pytest Unit Testlari (`test_fk.py`):**
   - Nol konfiguratsiya, simmetrik aylanish va xatoliklar nazorati (3/3 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$T_0^6 = \prod_{i=1}^6 A_i(q_i)$$
$$B = \text{atan2}\left(-r_{31}, \sqrt{r_{11}^2 + r_{21}^2}\right), \quad A = \text{atan2}(r_{21}, r_{11}), \quad C = \text{atan2}(r_{32}, r_{33})$$

Batafsil tahlil va singulyarlik holatlari [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python yechuvchisini ishga tushirish:
```bash
uv run --with numpy python src/scripts/forward_kinematics.py
```

Konsol chiqishi:
```
=================================================================
Lesson 08: Forward Kinematics (FK) Solver for KUKA KR 6 R900-2
=================================================================

Joint Configuration: [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]
KUKA Cartesian Pose:
  X =   480.00 mm
  Y =     0.00 mm
  Z =   435.00 mm
  A =     0.00°
  B =    90.00°
  C =     0.00°
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_fk.py
```
Natija: `3 passed in 0.11s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
