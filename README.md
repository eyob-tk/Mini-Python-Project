# Python Fundamentals: Currency Converter & Statistical Analyzer

A collection of functional Python tools demonstrating API integration, data processing, mathematical computations, and input validation with error handling.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Projects Included](#-projects-included)
  - [1. Real-Time USD to ETB Currency Converter](#1-real-time-usd-to-etb-currency-converter)
  - [2. Multi-Number Statistical Analyzer](#2-multi-number-statistical-analyzer)
- [Prerequisites & Installation](#-prerequisites--installation)
- [How to Run](#-how-to-run)
- [Error Handling](#-error-handling)
- [License](#-license)

---

## 📖 Overview

This repository contains two practical Python projects:
1. An **API-driven Currency Converter** that fetches live USD to ETB (Ethiopian Birr) exchange rates and calculates conversion amounts.
2. A **Statistical Data Analyzer** that takes a list of space-separated numbers and computes various stats including min/max values, even/odd counts, and averages.

---

## 🛠️ Projects Included

### 1. Real-Time USD to ETB Currency Converter
* **Concept:** Fetching live data via standard HTTP GET requests using external REST APIs.
* **Functionality:**
  * Connects to standard Exchange Rate APIs to retrieve current foreign exchange rates.
  * Prompts user input for a USD amount and returns the equivalent value in ETB.
  * Re-prompts continuously if non-numeric values are entered.

### 2. Multi-Number Statistical Analyzer
* **Concept:** Array operations, list transformations, and basic statistical computations.
* **Functionality:**
  * Parses a space-separated string of user inputs into integer values.
  * Finds the maximum (`max`) and minimum (`min`) numbers in the dataset.
  * Determines the count of even and odd numbers using modulus operations and list operations.
  * Calculates the exact arithmetic mean (average) of the dataset.

---

## ⚙️ Prerequisites & Installation

### Requirements
* **Python 3.7+**
* **`requests`** library for handling API calls

1. **Clone the repository:**
   ```bash
   git clone https://github.com/eyob-tk/USD-to-ETB-Currency-Converter-Multi-Number-Statistical-Analyzer.git
   cd USD-to-ETB-Currency-Converter-Multi-Number-Statistical-Analyzer
   ```

2. **Install required dependencies:**
   ```bash
   pip install requests
   ```

---

### 🚀 How to Run
* **Execute the main script using Python:**
  ``` bash
  python assignment.py
  ```

---

### 🛡️ Error Handling
* **API Network Failure:** Handles HTTP request timeouts or connectivity issues gracefully without crashing
* **Invalid User Inputs:** Uses  ```try-except``` blocks and input validation loops to prompt users until valid numeric input is provided.
* **Empty Data Entries:** Prevents division-by-zero errors in statistical calculations by checking if the input list contains valid data points before proceeding.

---

### 📜 License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).