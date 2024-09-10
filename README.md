# 🧮 Arithmetic Quiz Game
![image](https://github.com/user-attachments/assets/a0082f3e-ce24-466e-80dc-46ca01bb4328)

inspiration.. from professor toy.
This Python project is an interactive arithmetic quiz game that tests users on simple addition problems. The game generates random addition problems based on the chosen difficulty level, tracks user attempts, and keeps score. Users get three tries to input the correct answer for each problem, with a penalty applied for incorrect responses.

## 🌟 Features

- Three difficulty levels:
  - **Level 1**: Simple addition with numbers from 0 to 9.
  - **Level 2**: Addition with numbers from 10 to 99.
  - **Level 3**: Addition with numbers from 100 to 999.
- Tracks score, starting with 10 points.
- Lose a point for every incorrect set of answers (after 3 incorrect attempts).
- Immediate feedback with correct answers displayed after wrong attempts.

## 🚀 How to Play

1. Run the script.
2. Choose a difficulty level (1, 2, or 3).
3. Solve 10 random addition problems at the selected difficulty.
4. Try to maintain the highest possible score by answering correctly!

## 🛠️ Code Breakdown

- **`get_level()`**: Prompts the user to select a difficulty level (1, 2, or 3). It ensures valid input.
- **`generate_integer(level)`**: Based on the difficulty level, generates two random integers for each question and calls the checking function.
- **`checkint(X, Y)`**: Handles user input for each addition problem and tracks the number of incorrect attempts. If the user fails to answer correctly after three tries, the correct answer is displayed, and the score is reduced.
- **Score**: Starts at 10 and decreases by 1 point for every question that the user fails to answer correctly after three attempts.

## 📋 Example Gameplay

```bash
Level: 2
23 + 45 = 68
EEE
23 + 45 = 70
EEE
23 + 45 = 67
EEE
23 + 45 = 68
Score: 9
