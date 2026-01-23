# Project 01 — 2D Robotic Arm Simulator (Python)

## Objective 🎯
Develop a desktop application that simulates a planar 2-link robotic arm.
The application visualizes the arm configuration and computes its kinematics.

## Features 📋
-   Forward kinematics (2-link planar arm)
-   Interactive joint angle control (Sliders & Spinboxes)
-   Professional "Dashboard" GUI with Sidebar Layout
-   2D visualization with engineering grid
-   Inverse kinematics (Current Focus)

## Technologies 🛠️
-   Python 3
-   Math
-   Matplotlib
-   PyQt5

## Status
**Phase 1 - Core Kinematics** ✅ **COMPLETE**
-   [x] Set up project structure
-   [x] Create pure kinematics module (kinematics.py)
-   [x] Implement forward kinematics with proper error handling

**Phase 2 - GUI Development** ✅ **COMPLETE**
-   [x] Design PyQt5 interface (Professional Dashboard Look) 🎨
-   [x] Connect GUI to kinematics module 🔌
-   [x] Implement 2D visualization with Matplotlib integration 👁️
-   [x] Add real-time position updates ⏱️

**Phase 3 - Inverse Kinematics** 🔄 **IN PROGRESS**
-   [ ] Create solver structure (ik_solver.py)
-   [ ] Implement geometric solver logic (Law of Cosines)
-   [ ] Connect solver to GUI Inputs