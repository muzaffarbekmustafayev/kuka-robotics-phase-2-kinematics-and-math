# Numerical Inverse Kinematics & Optimization
## Raqamli (Numerical) teskari kinematika usullari | Численные методы обратной кинематики (Numerical IK)

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
Nyuton-Rafson iteratsiyasi, Yakobian transponirlangan va Levenberg-Marquardt (Damped Least Squares) optimallashtirish algoritmlari.

#### 🇷🇺 Русский:
Итерации Ньютона-Рафсона, транспонированный якобиан и алгоритм Левенберга-Марквардта (Damped Least Squares).

#### 🇬🇧 English:
Newton-Raphson iteration, Jacobian Transpose, and Levenberg-Marquardt Damped Least Squares (DLS) optimization.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
10-numerical-inverse-kinematics/
├── src/
│   ├── krl/            # Production KRL code (.src, .dat) [All code & comments in English]
│   └── scripts/        # Python verification scripts (.py) [All code & comments in English]
├── sim/                # KUKA.Sim Pro layouts (.vcmx), URDF and CAD models
├── docs/               # Theoretical diagrams, figures, and proofs
├── CLAUDE.md           # AI developer instructions
└── README.md           # Trilingual guide (Uzbek, Russian, English)
```

---

### 🧮 Mathematical Foundations & Verification
All formulas, derivations, and theorems for this lesson are detailed in [**docs/derivations.md**](./docs/derivations.md).
Runnable Python verification scripts are provided in `src/scripts/verify_theorem.py`.

To run the verification test:
```bash
uv run --with numpy python src/scripts/verify_theorem.py
```

---
🔗 **[Return to Master Syllabus / Bosh Mundarija](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
