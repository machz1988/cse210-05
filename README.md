# Overview
---
Cycle is a game in which two players seeks to get the each other into running into the others trail. The game continues as long as the players do not collide with the others trail or their own!

[All of the documentation and images are taken from here](https://byui-cse.github.io/cse210-course-competency/polymorphism/materials/cycle-specification.html)

---
## Rules
---
Cycle is played according to the following rules:

* Player 1, Red, will use w, a, s, d to more up, left, down and right respectively.
* Player 2, Green, will use i, j, k, l to more up, left, down and right respectively.
* If a player runs into the other players trail or their own trail, that player loses.
* The game continues until a player runs into their own trail or the other players trail.

---
## Interface

---
<img src="images/cycle-screenshot.png" width="500">

---
## Getting Started

---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 __main__.py
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

---
## Project Structure

---
root                  (project root folder)
+-- data              (data files for game)
+-- game              (specific game classes)
+-- __main__.py       (entry point for program)
+-- README.md         (general info)

---
## Required Technologies

---
* Python 3.8.0
* Raylib Python CFFI 3.7

---
## Authors

---
* Antonio Saucedo (antoniojesus@byui.edu)
* Godwin Iyip (iyi21001@byui.edu)
* Manuel Cipriano (cip21002@byui.edu)
* Shane Cook (scc0131@byui.edu)
* (Cole) Ukeje Chinemerem (uke21001@byui.edu)