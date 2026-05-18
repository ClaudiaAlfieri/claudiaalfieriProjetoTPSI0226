# claudiaalfieriProjetoTPSI0226

# 🎬 PyFlix - Movie & Series Management System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![ATEC](https://img.shields.io/badge/Training-TPSI%20%7C%20ATEC-darkgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

> Python application developed as the final project for the Python Programming course of the CET TPSI program at ATEC.
>
> PyFlix is a personal movie and series management system with a command-line interface (CLI).

---

## 📌 About the Project

**PyFlix** was developed as the final project for the **Python Programming** course unit of the **CET TPSI** program at **ATEC — Training Academy**.

The goal is to implement a complete management system with registration, validation, storage, and persistent data manipulation, applying the concepts taught throughout the course.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 Authentication | Login with email and password validation via regex |
| 📋 Listing | Full view of all registered entries |
| ➕ Add | Register new movies/series with data validation |
| ✏️ Edit | Update any field with validation |
| 🗑️ Delete | Removal with user confirmation |
| 🔍 Linear Search | Search by title — traverses the entire list |
| 🔍 Binary Search | Search by year — splits the list in half (automatic sorting) |
| 📊 Bubble Sort | Sorting by comparing neighbouring elements |
| 📊 Selection Sort | Sorting by selecting the smallest element |
| 📈 Statistics | Average, max/min, total by type, and filters |
| 💾 Persistence | Data automatically saved and loaded in JSON |
| 📤 CSV Export | Export the list to an Excel-compatible file |
| 📝 Activity Logs | Automatic logging of all actions with date and time |

---

## 🗂️ Project Structure

```
pyflix/
├── main.py          # Entry point — coordinates the program
├── auth.py          # Authentication and login
├── menus.py         # CLI menu interface
├── filmes.py        # CRUD operations (create, read, edit, delete)
├── data.py          # JSON data persistence
├── validate.py      # Validation with regular expressions (regex)
├── search.py        # Search algorithms (linear and binary)
├── sort.py          # Sorting algorithms (Bubble and Selection Sort)
├── estatisticas.py  # Statistics and filters
├── exportar.py      # Data export to CSV
└── logs.py          # Activity logging
```

---

## 🔐 Test Credentials

```
Email:    admin@pyflix.com
Password: Admin123
```

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/ClaudiaAlfieri/claudiaalfieriProjetoTPSI0226.git
```

2. Navigate to the project folder:
```bash
cd claudiaalfieriProjetoTPSI0226
```

3. Run the program:
```bash
python main.py
```

> No additional installations required — the project uses only Python's native libraries (`json`, `re`, `csv`, `datetime`).

---

## 🛠️ Technologies Used

- **Python 3** — main language
- **JSON** — data persistence
- **CSV** — data export to Excel
- **Regex (re)** — email, password, and date validation
- **datetime** — date and time logging
- **Git** — version control
- **GitHub** — remote repository

---

## 📐 Concepts Applied

| Concept | Description |
|---|---|
| 🧩 Modularisation | 11 files with separate responsibilities |
| 🔎 Linear Search | Traverses the full list element by element |
| 🔎 Binary Search | Splits the list in half at each comparison |
| 📊 Bubble Sort | Compares and swaps neighbouring elements successively |
| 📊 Selection Sort | Finds the smallest element and places it in the correct position |
| ✅ Regex | Format validation for email, password, and date |
| 💾 JSON Persistence | Data loaded on startup and saved on exit |
| ⚠️ Exceptions | Error handling with try/except in file operations |
| 📤 CSV Export | List exported to an Excel-compatible file |
| 📝 Logs | Automatic action logging with date and time |

---

## 👩‍💻 Author

This project was developed by **Cláudia Alfieri** as the final project for the Python Programming course of the CET TPSI program at ATEC.

---

Made with ❤️, lots of `print()` statements, and a fair amount of `try/except` along the way 🐍🚀
