# Phase 2: Spatial Geometry & Kinematic Modeling
## 2-Bob: Fazoviy Geometriya va Kinematik Modellashtirish
### Глава 2: Пространственная Геометрия и Кинематическое Моделирование

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Topics](https://img.shields.io/badge/Topics-kuka--robotics--course%20%7C%20mechatronics%20%7C%20krl--programming%20%7C%20ros2--robotics%20%7C%20samdu%20%7C%20tsu-blue.svg)](#)

---

### 🌐 Phase Description (Trilingual)

#### 🇺🇿 O'zbekcha:
Rodrigues formulasi, so(3) Lie algebrasi, Eyler burchaklari (A, B, C), Kvaternionlar, DH parametrlari va To'g'ri/Teskari kinematika.

#### 🇷🇺 Русский:
Формула Родрига, алгебра Ли so(3), углы Эйлера (A, B, C), кватернионы, параметры ДХ и прямая/обратная кинематика.

#### 🇬🇧 English:
Rodrigues rotation formula, so(3) Lie algebra, Euler angles (A, B, C), Quaternions, DH parameters, Forward and Analytical Inverse Kinematics.

---

### 📑 Lessons Curriculum / Darslar Mundarijasi / Содержание уроков

* [**05-rodrigues-rotation-formula**: Spatial Rotations & Rodrigues Rotation Formula](./05-rodrigues-rotation-formula)
  * 🇺🇿 so(3) Lie algebrasi, skew-symmetric operator [k]_x va Rodrigues formulasining geometrik hamda matritsaviy eksponensial keltirib chiqarilishi.
  * 🇷🇺 Алгебра Ли so(3), кососимметрический оператор [k]_x и вывод формулы Родрига через матричную экспоненту e^{theta K}.
  * 🇬🇧 so(3) Lie algebra, skew-symmetric operator [k]_x, geometric derivation, and matrix exponential proof e^{theta K}.

* [**06-rotation-matrices-and-quaternions**: Rotation Matrices, Euler Angles & Quaternions](./06-rotation-matrices-and-quaternions)
  * 🇺🇿 KUKA Z-Y'-X'' (A, B, C) Eyler burchaklari, Gimbal Lock (B=+-90) muammosi va to'rt o'lchamli birlik kvaternionlar orqali SLERP interpolyatsiyasi.
  * 🇷🇺 Углы Эйлера KUKA Z-Y'-X'' (A, B, C), проблема Gimbal Lock (B=+-90) и сферическая интерполяция кватернионов SLERP.
  * 🇬🇧 KUKA Z-Y'-X'' (A, B, C) Tait-Bryan angles, Gimbal Lock singularity at B=+-90, unit quaternions and SLERP orientation interpolation.

* [**07-dh-parameters-modelling**: Denavit-Hartenberg (DH) Parameter Modeling](./07-dh-parameters-modelling)
  * 🇺🇿 Standart va Modifikatsiyalangan DH konvensiyalari. KUKA KR 6 R900-2 uchun rasmiy DH koordinata jadvallarini noldan qurish.
  * 🇷🇺 Стандартная и модифицированная конвенции DH. Построение официальной таблицы DH для KUKA KR 6 R900-2.
  * 🇬🇧 Standard and Modified DH conventions. Deriving the analytical DH parameter table for the KUKA KR 6 R900-2.

* [**08-forward-kinematics-solver**: Forward Kinematics Solver & SE(3) Chain](./08-forward-kinematics-solver)
  * 🇺🇿 SE(3) transformatsiya matritsalari zanjiri. Bo'g'in burchaklariga ko'ra flanetsning fazodagi yakuniy o'rnini hisoblash va $POS_ACT bilan tekshirish.
  * 🇷🇺 Цепочка однородных трансформаций SE(3). Расчет позиции фланца по углам сочленений и сверка с $POS_ACT.
  * 🇬🇧 SE(3) homogeneous transformation chain. Computing Cartesian flange pose from joint angles and validating against $POS_ACT.

* [**09-inverse-kinematics-analytical**: Analytical Inverse Kinematics (Pieper's Method)](./09-inverse-kinematics-analytical)
  * 🇺🇿 Sferik bilak uchun Piper (Pieper) dekouplingi, 8 ta analitik yechim, KUKA Status (S) va Turn (T) butun sonli bitlarining fizik ma'nosi.
  * 🇷🇺 Разделение сферического запястья по Пиперу, 8 аналитических решений, физический смысл битов KUKA Status (S) и Turn (T).
  * 🇬🇧 Pieper decoupling criterion for spherical wrists, 8 closed-form analytical solutions, KUKA Status (S) and Turn (T) bit decoding.

* [**10-numerical-inverse-kinematics**: Numerical Inverse Kinematics & Optimization](./10-numerical-inverse-kinematics)
  * 🇺🇿 Nyuton-Rafson iteratsiyasi, Yakobian transponirlangan va Levenberg-Marquardt (Damped Least Squares) optimallashtirish algoritmlari.
  * 🇷🇺 Итерации Ньютона-Рафсона, транспонированный якобиан и алгоритм Левенберга-Марквардта (Damped Least Squares).
  * 🇬🇧 Newton-Raphson iteration, Jacobian Transpose, and Levenberg-Marquardt Damped Least Squares (DLS) optimization.

---

### 🏛️ Repository Internal Structure
```
kuka-robotics-phase-2-kinematics-and-math/
├── 05-rodrigues-rotation-formula/
├── 06-rotation-matrices-and-quaternions/
├── 07-dh-parameters-modelling/
├── 08-forward-kinematics-solver/
├── 09-inverse-kinematics-analytical/
├── 10-numerical-inverse-kinematics/
```

---

### 👥 Academic Alliance & Authorship
* **Author / Muallif:** Muzaffarbek Mustafayev
* **Academic Partners:** Samarkand State University (SamDU) & Tomsk State University (TSU)
* 🔗 **[Master Syllabus Navigator](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
