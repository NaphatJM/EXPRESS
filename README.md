# MobileDev Backend Project

This project is part of the **240-331 MOBILE APPLICATIONS DEVELOPER MODULE** course.  
It focuses on learning how to build a backend using **Python**, **FastAPI**, and **PostgreSQL**, with **Poetry** as a dependency manager.

## Objective

- Understand backend development concepts
- Create RESTful APIs using FastAPI
- Connect to a PostgreSQL database using SQLAlchemy ORM
- Use modern Python tooling with Poetry
- Prepare backend APIs for mobile app integration

## Tech Stack

- **Language**: Python 3.12
- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **Environment Management**: Poetry
- **Web Server**: Uvicorn

## Getting Started

### 0. Run Virtual Environment:

In case you didn't have one 
```bash
python -m venv .venv 
source .venv/bin/activate #Linux
source .venv/Scripts/activate #window
```

### 1. Install Poetry

If you don’t have Poetry installed:

```bash
pip install poetry 
poetry --version
```

### 2. getting start 

initial poetry in working directory
```bash
poetry init 
```

### 3. install dependencies  

Install listed dependencies in pyproject.toml
```bash
poetry install 
```

### 4. run dev 

using scripts that i wrote 
```bash
./scripts/run-dev
```
