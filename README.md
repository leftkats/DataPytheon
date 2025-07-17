# :snake: DataPytheon

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![codecov](https://codecov.io/gh/leftkats/DataPytheon/graph/badge.svg?token=C69BFSAR0S)](https://codecov.io/gh/leftkats/DataPytheon)


Welcome to **DataPytheon** – a mythical library of **easy-to-use Python scripts** that help you **access, clean, and explore datasets** from both public repositories and live APIs.

Whether you're a **beginner learning data science**, a **developer prototyping fast**, or an **open-source contributor**, this project gives you plug-and-play tools to handle real-world data with ease.

---

## :bookmark_tabs: What Is This?

**DataPytheon** is a hybrid repository that offers:

- **`recipes/`** — Pre-cleaned **static datasets** (like Titanic, Iris, Netflix, etc.)
- **`syncers/`** — Scripts to **fetch real-time data** from public APIs (like exchange rates, crypto prices, weather, etc.)

All scripts return **ready-to-use Pandas DataFrames**, ideal for quick analysis, learning, or feeding into models.

Think of it as your **data prep toolbox** — one line of code away from clean, structured data.

---

## :hammer_and_wrench: Who Is It For?

- :student: **Beginners** in Python, data science, or machine learning
- :computer: **Developers** who want quick dataset access without boilerplate
- :sparkles: **Contributors** looking for a simple and valuable open-source project
- :books: **Educators** who need ready datasets for teaching or assignments

---

## :file_folder: Project Structure
```text
DataPytheon/
│
├── recipes/                    # Static datasets
│   └── titanic.py              # Example recipe
│
├── syncers/                    # Live/API data scripts
│   └── exchange_rates.py       # Example syncer
│
├── tests/                      # Basic unit tests for scripts
│   └── test_titanic.py
```

## 🧪 Run your tests

Just run the next command from the root folder of the project:

```
pytest --cov=src   
```