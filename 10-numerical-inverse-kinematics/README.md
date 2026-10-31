# 10-Dars: Sonli teskari kinematika (Newton-Raphson va DLS algoritmlari)
## Numerical Inverse Kinematics (Newton-Raphson & Levenberg-Marquardt DLS)

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KR 6 R900-2 roboti uchun analitik yechimlar chegarasidan tashqaridagi yoki murakkab cheklovli vaziyatlarda teskari kinematika masalasini sonli iteratsion usullar — Newton-Raphson (psevdo-teskari) hamda Levenberg-Marquardt Damped Least Squares (DLS) algoritmlari orqali hal qilish, bo'g'in burchaklari chegaralarini ($\mathbf{q} \in [\mathbf{q}_{min}, \mathbf{q}_{max}]$) qat'iy nazorat qilish va singulyarlik yaqinida barqaror konvergentsiyani ta'minlash.

---

### 📊 2. Natija (Result)
1. **Python Sonli IK Yechuvchisi (`numerical_ik_solver.py`):**
   - 6x6 geometrik Yaqobi matritsasini sonli differentsiyalash.
   - Levenberg-Marquardt DLS yechimi: $\Delta \mathbf{q} = J^T(JJ^T + \lambda^2 I)^{-1} \mathbf{e}$.
   - Bo'g'inlar diapazoni qisqichlari (clamping).
   - Pozitsiya va orientatsiya bo'yicha mustaqil xatolik konvergentsiyasi ($< 0.5\text{ mm}$, $< 0.001\text{ rad}$).
2. **Pytest Unit Testlari (`test_numerical_ik.py`):**
   - Yaqob matritsasi o'lchamlari, DLS yechim konvergentsiyasi va burchak chegaralari nazorati (3/3 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$\mathbf{\Delta q = J^T (J J^T + \lambda^2 I)^{-1} e}$$
$$\min_{\Delta \mathbf{q}} \left( \|J \Delta \mathbf{q} - \mathbf{e}\|^2 + \lambda^2 \|\Delta \mathbf{q}\|^2 \right)$$

Batafsil tahlil va isbotlar [**docs/derivations.md**](./docs/derivations.md) da keltirilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python yechuvchisini sinash:
```bash
uv run --with numpy python src/scripts/numerical_ik_solver.py
```

Konsol chiqishi:
```
=================================================================
Lesson 10: Numerical Inverse Kinematics (Newton-Raphson & DLS)
=================================================================

Target Position: [450.  50. 420.] mm

[DLS Solver Result]
  Converged:    True (in 6 iterations)
  Final Joints: [6.34, -72.41, 88.19, 0.12, 14.88, -0.05] deg
  Pos Error:    0.0412 mm

[Newton-Raphson Solver Result]
  Converged:    True (in 5 iterations)
  Pos Error:    0.0084 mm
```

Unit testlarni ishga tushirish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_numerical_ik.py
```
Natija: `3 passed in 0.12s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
