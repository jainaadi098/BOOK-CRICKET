# 🏏 BOOK CRICKET

> **"The Classic Classroom Game, Digitized."**

A Python-based command-line game that simulates the nostalgic "Book Cricket" played with page numbers. This project features a robust game loop, a high-stakes "Infinite Survival" mode, and persistent data tracking.

## 📜 How It Works
The game simulates opening a book to a random page. The last digit (0-9) determines your score.
- **0** = Wicket (**OUT**)
- **1-9** = Runs scored

### The Game Modes
1.  **Normal Mode:** Your goal is to score a **Century (100 runs)**.
2.  **Infinite Mode (The Trap):** Once you cross 100 runs, you unlock Infinite Mode. In this mode, there is no "Quit" button. You must play until you hit a '0'. It is a test of pure luck and endurance.

## 🚀 Key Features
* **Logic & State:** Implements a state machine to handle the one-way transition from Normal to Infinite mode.
* **Persistence:** Auto-saves your **World Record** to a `highscore.txt` file using File I/O.
* **Input Safety:** Prevents crashes from invalid user inputs (e.g., typing "yep" instead of "yes").
* **Clean UI:** Professional console formatting with a dynamic header.

## 🕹️ Gameplay Preview
```text
============================================================
              BOOK CRICKET: INFINITE EDITION              
============================================================
      🏆 CURRENT RECORD: 145 RUNS
------------------------------------------------------------
Welcome, Player1!
Rules: Score 100 runs to unlock Infinite Mode.

[Mode: Normal] You scored 6. Total Runs: 94
[Mode: Normal] You scored 8. Total Runs: 102

************************************************************
 🏏 CONGRATULATIONS! YOU HIT A CENTURY (100+)! 🏏
 You have unlocked INFINITE MODE.
************************************************************
Warning: There is no turning back. Play until you get OUT.
🛠️ Tech Stack
Language: Python 3.x

Core Concepts: Loops (while), Conditionals (if/elif), Functions, File Handling (os, open), Randomization.

🏃‍♂️ How to Run
Clone the repository:

Bash

git clone [https://github.com/YOUR-USERNAME/book-cricket.git](https://github.com/YOUR-USERNAME/book-cricket.git)
Run the game:

Bash

python book_cricket.py
