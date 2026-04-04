# AI + Robotics Curriculum (Updated)

## Why this version
This roadmap starts with baseline testing so the plan adapts to your real current level, not assumptions.

## Phase 0: Baseline + Foundations Reset (Week 0-2)
- Complete baseline tests in `assessments/baseline_day_00`.
- Identify weak areas in:
  - Python core (comprehensions, OOP, functions, modules)
  - C++ core (STL, classes, memory model basics)
  - Workflow (Git, debugging, testing, project structure)
- Output:
  - personalized weakness map
  - adjusted daily problems

## Phase 1: Coding Fluency (Week 3-8)
- Python:
  - list/dict/set comprehensions
  - OOP and dataclasses
  - error handling, file I/O, modules
  - testing with pytest
- C++:
  - STL containers, algorithms, classes
  - references/pointers/smart pointers (as needed)
  - compile/debug workflow
- Workflow:
  - Git branching, commit quality
  - issue breakdown
  - debug logs + reproducible bug reports

## Phase 2: AI Engineering Core (Week 9-14)
- NumPy, pandas, matplotlib
- ML pipeline:
  - preprocessing
  - train/validation split
  - metrics
- scikit-learn first, then PyTorch basics
- small model projects with proper repo structure

## Phase 3: Robotics Software Core (Week 15-20)
- Linux + ROS2 fundamentals
- nodes, topics, services
- coordinate frames, control loop basics
- simulation-first development (Gazebo)

## Phase 4: Integration + Portfolio (Week 21-24)
- End-to-end robotics+AI mini project
- quality checklist:
  - docs
  - tests
  - reproducible setup
  - demo video + architecture note

## Daily format (90-150 min)
1. 10-15 min recall (no notes)
2. 60-90 min coding problems
3. 20 min debugging/refactor
4. 10 min engineering log

## Tool strategy (where to invest vs avoid)
Invest deeply in:
- Python + C++ fundamentals
- Git and debugging
- reading docs quickly
- testing basics

Do not over-invest early in:
- heavy framework hopping
- advanced math proofs without coding application
- perfect architecture before first working version

Use tools instead of manual effort when possible:
- lint/formatters (`black`, `ruff`, `clang-format`)
- test runners (`pytest`, `ctest`/simple scripts)
- debugger/logging tools
- templates for project scaffolding

## Mentorship protocol
- You solve 2-5 tasks daily.
- I review with:
  - correctness
  - code quality
  - engineering quality
  - speed and confidence trend
- Every 7 days: focused reassessment and curriculum adjustment.