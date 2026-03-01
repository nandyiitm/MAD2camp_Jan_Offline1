# 🚀 MAD2 Project

This repository contains my **MAD2 project** developed during the bootcamp.
It includes all source code, dependencies, and setup instructions required to run the project locally.

---

## 📦 Project Setup

Follow the steps below to set up the project on your local machine.

### 1️⃣ Create a Virtual Environment

Create a virtual environment named `venv`:

```bash
python -m venv venv
```

---

### 2️⃣ Activate the Virtual Environment

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```

* **Linux / macOS:**

  ```bash
  source venv/bin/activate
  ```

---

### 3️⃣ Install Dependencies

Install the required packages using:

```bash
pip install -r requirements.txt
```

---

## 🔄 Updating Requirements

If you install new packages, update the `requirements.txt` file with:

```bash
pip freeze > requirements.txt
```

---

## 📁 Project Structure

```
MAD2-project/
│
├── venv/                # Virtual environment (not pushed to GitHub)
├── requirements.txt     # Project dependencies
├── src/                 # Source code
└── README.md            # Project documentation
```

---

## ✅ Best Practices

* Always activate the virtual environment before running the project.
* Do not upload the `venv/` folder to GitHub (add it to `.gitignore`).
* Update `requirements.txt` whenever you install new packages.
