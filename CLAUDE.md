# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kalfa is a Python CLI application using calendar versioning (YYYY.MM.DD). The version is automatically bumped daily via GitHub Actions.

## Development Commands

```bash
# Install the package in development mode
uv pip install -e .

# Run the CLI
kalfa
# or directly via uv
uv run kalfa

# Run from source without installing
uv run python -m kalfa.main
```

## Architecture

### Versioning Strategy

- **Calendar versioning** (CalVer) in `YYYY.MM.DD` format
- Automated version bumps run daily at 00:00 UTC via `.github/workflows/version-bump.yml`
- Workflow creates git tags for each version (e.g., `v2026.02.14`)
- Manual version bumps can be triggered via workflow dispatch

### Package Structure

- **Entry point**: `kalfa.main:main` - prints package name and version using `importlib.metadata`
- **Build system**: `uv_build` (modern uv-based build backend)
- **Python version**: 3.14 (specified in `.python-version`)

### Key Files

- `pyproject.toml` - Project metadata, dependencies, and build configuration
- `src/kalfa/main.py` - CLI entry point using `importlib.metadata.Distribution`
- `.python-version` - Python version specification for uv and pyenv

## Development Notes

- Use `uv` for all package management operations (already preferred per global CLAUDE.md)
- The project currently has no external dependencies
- No test suite exists yet - tests should be added to a `tests/` directory if needed
