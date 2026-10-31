# Rotation Matrices, Euler Angles & Quaternions
## Aylanish matritsalari, Eyler burchaklari va Kvaternionlar | Матрицы поворота, углы Эйлера и Кватернионы

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
KUKA Z-Y'-X'' (A, B, C) Eyler burchaklari, Gimbal Lock (B=+-90) muammosi va to'rt o'lchamli birlik kvaternionlar orqali SLERP interpolyatsiyasi.

#### 🇷🇺 Русский:
Углы Эйлера KUKA Z-Y'-X'' (A, B, C), проблема Gimbal Lock (B=+-90) и сферическая интерполяция кватернионов SLERP.

#### 🇬🇧 English:
KUKA Z-Y'-X'' (A, B, C) Tait-Bryan angles, Gimbal Lock singularity at B=+-90, unit quaternions and SLERP orientation interpolation.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
06-rotation-matrices-and-quaternions/
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
