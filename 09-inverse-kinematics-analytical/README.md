# Analytical Inverse Kinematics (Pieper's Method)
## Analitik teskari kinematika (Pieper usuli) | Аналитическая обратная кинематика (Метод Пипера)

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
Sferik bilak uchun Piper (Pieper) dekouplingi, 8 ta analitik yechim, KUKA Status (S) va Turn (T) butun sonli bitlarining fizik ma'nosi.

#### 🇷🇺 Русский:
Разделение сферического запястья по Пиперу, 8 аналитических решений, физический смысл битов KUKA Status (S) и Turn (T).

#### 🇬🇧 English:
Pieper decoupling criterion for spherical wrists, 8 closed-form analytical solutions, KUKA Status (S) and Turn (T) bit decoding.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
09-inverse-kinematics-analytical/
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
