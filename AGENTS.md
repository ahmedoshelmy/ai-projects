# AI Projects - Agent Editing Guidelines

This document outlines the rules and conventions that AI agents (including Claude Code, Antigravity/Gemini, and others) must follow when editing and creating files in this repository.

## 🎯 Repository Overview
A comprehensive learning and development repository for advanced AI systems, including LLM-based agents, RAG systems, machine learning pipelines, and agentic applications.

## 🛠️ Project Structure and Conventions

### 1. Structure
- **`courses/`**: Learning materials and courses.
- **`projects/`**: Active and planned projects, numbered `01` to `10`.
- **`tools-and-utilities/`**: Reusable shared code, libraries, and utilities.

### 2. Adding a New Project
When creating or extending a project, follow this exact recipe:
1. Create a numbered folder: `projects/NN-project-name/` (e.g., `projects/11-new-project/`).
2. Create subdirectories as needed:
   - `src/` for source code
   - `tests/` for unit tests
   - `data/` for data files or assets
3. Include a `requirements.txt` file for all project dependencies.
4. Include a `README.md` containing:
   - Project overview
   - Key concepts to learn
   - Recommended stack
   - Project structure
   - Status tracker (`[ ] Not Started`, `[~] In Progress`, `[x] Complete`)

## 🐍 Python Setup and Commands
- **Python Version**: 3.10+
- **Virtual Environment**: Use the virtual environment in `.venv` at the root directory.
  - Activate on Windows: `.venv\Scripts\activate`
  - Activate on Unix/macOS: `source .venv/bin/activate`
- **Dependencies**: Install dependencies using `pip install -r requirements.txt` within the specific project directory.

## 🤖 Agent Conventions
- `CLAUDE.md` and `GEMINI.md` must reference `AGENTS.md`.
- Always document changes in `README.md` or a status tracker file when completing project steps.
- Preserve existing code comments and structure unless explicitly asked to refactor.
