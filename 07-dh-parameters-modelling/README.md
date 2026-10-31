# Denavit-Hartenberg (DH) Parameter Modeling
## Denavit-Hartenberg (DH) parametrlari modellashtirishi | Моделирование параметров Денавита-Хартенберга (DH)

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
Standart va Modifikatsiyalangan DH konvensiyalari. KUKA KR 6 R900-2 uchun rasmiy DH koordinata jadvallarini noldan qurish.

#### 🇷🇺 Русский:
Стандартная и модифицированная конвенции DH. Построение официальной таблицы DH для KUKA KR 6 R900-2.

#### 🇬🇧 English:
Standard and Modified DH conventions. Deriving the analytical DH parameter table for the KUKA KR 6 R900-2.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
07-dh-parameters-modelling/
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
