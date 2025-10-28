# Classic Pong Game 

This is a complete implementation of the classic arcade game Pong, built using Python's built-in `turtle` module. It's a two-player game featuring score tracking, increasing ball speed, and a "first to 10" win condition.


<img width="600" height="475" alt="image" src="https://github.com/user-attachments/assets/40b8d65b-e035-4e05-ad96-465f65b4a2a0" />


## 🚀 How to Run This Game

You can run this game on your local machine by following these simple steps.

### 1. Prerequisites

Make sure you have **Python 3** installed on your computer. This game uses only built-in libraries (`turtle`, `time`), so no external packages are needed.

### 2. Clone & Run

1.  Open your terminal or command prompt.
2.  Clone this repository to your computer using this command:
    ```bash
    git clone [https://github.com/Spargerx/Pong_Game.git](https://github.com/Spargerx/Pong_Game.git)
    ```
3.  Navigate into the newly created folder:
    ```bash
    cd Pong_Game
    ```
4.  Run the main game file:
    ```bash
    python main.py
    ```
    *(You may need to use `python3 main.py` on some systems)*

That's it! The game window should open, and you can start playing.

## 🕹️ Controls

* **Left Paddle:**
    * **Up:** `w`
    * **Down:** `s`
* **Right Paddle:**
    * **Up:** `Up Arrow`
    * **Down:** `Down Arrow`

## ✨ Features

* **Classic Two-Player Gameplay:** Control the paddles on the left and right to volley the ball.
* **Score Tracking:** The score is displayed at the top and updates automatically.
* **Progressive Difficulty:** The ball's speed increases after each successful paddle hit.
* **Win Condition:** The first player to reach 10 points wins the game!
* **Object-Oriented Design:** The code is cleanly separated into `Ball`, `Paddle`, and `Scoreboard` classes.

## 🛠️ File Structure

The project is broken down into four key files using Object-Oriented Programming (OOP) principles:

* `main.py`: This is the main driver file. It initializes the screen, creates the objects (paddles, ball, scoreboard), and contains the primary game loop and collision detection logic.
* `paddle.py`: Defines the `Paddle` class, which controls the creation, appearance, and movement (up/down) of the paddles.
* `ball.py`: Defines the `Ball` class, which manages the ball's movement, speed, and bouncing physics (off walls and paddles).
* `scoreboard.py`: Defines the `Scoreboard` class, which is responsible for drawing the scores, updating them, and displaying the "Game Over" message.
