# Forward Kinematics Solver & SE(3) Chain
## To'g'ri kinematika (Forward Kinematics) solveri | Решатель прямой кинематики (Forward Kinematics)

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-2-kinematics-and-math-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🌐 Overview & Multilingual Summary

#### 🇺🇿 O'zbekcha:
SE(3) transformatsiya matritsalari zanjiri. Bo'g'in burchaklariga ko'ra flanetsning fazodagi yakuniy o'rnini hisoblash va $POS_ACT bilan tekshirish.

#### 🇷🇺 Русский:
Цепочка однородных трансформаций SE(3). Расчет позиции фланца по углам сочленений и сверка с $POS_ACT.

#### 🇬🇧 English:
SE(3) homogeneous transformation chain. Computing Cartesian flange pose from joint angles and validating against $POS_ACT.

---

### 🗂️ Directory Structure (Mandatory Boilerplate)
```
08-forward-kinematics-solver/
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
