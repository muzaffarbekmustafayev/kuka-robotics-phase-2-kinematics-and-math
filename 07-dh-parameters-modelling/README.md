# 07-Dars: Denavit-Hartenberg (DH) Parametrlari va Kinematik Modellashtirish
## Denavit-Hartenberg Parameters & Kinematic Modelling

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KR 6 R900-2 (KR AGILUS-2) olti bo'g'inli sanoat roboti uchun standart Denavit-Hartenberg (DH) parametrlar jadvalini ishlab chiqish, 4 ta elementar transformatsiyalar orqali $A_i^{i-1}$ matritsalarini hosil qilish va zvenolarning fazoviy oraliq koordinata tizimlari ketma-ketligini dasturlash.

---

### 📊 2. Natija (Result)
1. **Python DH Modeli (`dh_model_kr6.py`):**
   - 6 ta bo'g'in uchun to'liq DH parametrlari ($d_1=400, a_1=25, a_2=455, a_3=35, d_4=420, d_6=80\text{ mm}$).
   - Standart DH transformatsiya matritsasi generatori.
   - Har bir zveno uchun kumulyativ bazaviy freymlar $T_0^1, T_0^2, \dots, T_0^6$.
2. **Pytest Unit Testlari (`test_dh_model.py`):**
   - Geometrik parametrlar to'g'riligi, matritsalar ortogonalligi va $XHOME$ fazoviy holati tekshiruvi (3/3 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$T_i^{i-1} = \begin{bmatrix}
\cos\theta_i & -\sin\theta_i \cos\alpha_i & \sin\theta_i \sin\alpha_i & a_i \cos\theta_i \\
\sin\theta_i & \cos\theta_i \cos\alpha_i & -\sin\theta_i \sin\alpha_i & a_i \sin\theta_i \\
0 & \sin\alpha_i & \cos\alpha_i & d_i \\
0 & 0 & 0 & 1
\end{bmatrix}$$

Parametrlar jadvali va batafsil xulosalar [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python skriptini tekshirish:
```bash
uv run --with numpy python src/scripts/dh_model_kr6.py
```

Konsol chiqishi:
```
=================================================================
Lesson 07: Denavit-Hartenberg (DH) Model for KUKA KR 6 R900-2
=================================================================

Flange Pose at Zero Configuration [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]:
  Position (X, Y, Z) mm: [-475.00, 0.00, 890.00]

Flange Pose at XHOME Configuration [0.0, -90.0, 90.0, 0.0, 0.0, 0.0]:
  Position (X, Y, Z) mm: [480.00, 0.00, 435.00]
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_dh_model.py
```
Natija: `3 passed in 0.11s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
