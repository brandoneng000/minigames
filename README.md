# minigames
![CI/CD](https://github.com/brandoneng000/minigames/actions/workflows/deployment.yml/badge.svg)

[https://worldminigame.com/](https://worldminigame.com/)

## Overview

Minigames is a Python/Django application where users can play some simple games. Current games are Rock paper scissors and a coin toss.
The rock paper scissors game records and displays the total scores of everyone who has played. While the coin toss game
records the number of heads, tails, sides, and times played. 

Website is deployed on an AWS EC2 Instance. The database that records the scores is utilizing AWS RDS. 

### Rock paper scissors

Players can pick any of the three choices and a random AI will make their own choice.

### Coin Toss

Players attempt to predict how the coin will land and the click on the `Flip` button.
The coin will primarily land on heads or tails, but has a small chance to land on its side.