# Game of Greed

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
The Game of Greed is a game of chance. Also known as Ten Thousand, Zilch or Foo, the game centers around rolling six dice and calculating their values. The first player to 10,000 points is declared the winner. At the start of the game you roll your six dice then calculate the points you rolled. Ones have a value of 100. Fives have a value of 50. The other numbers have no inherant value. 

Three or more of the same number are worth more points. Three of a number is equal to 100 x the face value. More than three of the same number adds an additional tripple value for each aditional over three. Ex: (3,3,3) would yeild 300 points, (3,3,3,3) yeilds 600 points, (3,3,3,3,3) yeilds 900 points, and if every dice is a 3 it would yeild 1200 points!

Straights are worth 1500 points. Straights are considered rolling one of each number: (1,2,3,4,5,6).

Three pairs are also worth 1500 points. Ex: (2,2,3,3,4,4)

Not hitting any value on your first roll gives you one free re-roll. If values are hit on either roll, you can choose to set any of those values aside to add to your total score. Any dice you set aside, can not be re-rolled for additional score. After sucessfully hitting a scoring combination of dice, any dice that are not set aside may be re-rolled for additional points. 

A player may elect to bank their earned points at any time when they have earned them. Banking their points ends the round. Dice go to the next player for their turn. 

Otherwise a player can elect to set aside scoring dice and continue rolling. This can continue for as long as the resulting rolls end in a scoring value. If the additional roll results in a score of zero, ALL points are lost and the round ends.

The longer you wait to bank your earned points, the higher chance you have of losing them all...

Feeling greedy?
## Getting Started

First, make sure that you have python3 installed:
```
$ python3 --version
Python 3.7.5
```
If you do not:
```
$ brew install python
```
You need to have the files locally. Click on the green clone or download button and Download ZIP:

![Click_to_download](/assets/Click_to_download_x6c0g16lz.png)


In your command line, navigate to this directory:
```
$ cd ~  ##this is your root directory
$ cd Downloads  ##by default: Downloads is a directory inside of your root; and where your file will be downloaded
$ cd pythonic-garage-band ##and now you are in this directory
```
This is a command line interface game.
To start the game:
```
$ python3 game_of_greed.py
```
Follow the prompts - Good luck!

## Functionality/Architecture
This game is using 'dice rolls', arguements in the form of tuples. The dice rolls are between 1 and 6 individually and there are six dice at the start of the game. An instance of a GameOfGreed is created upon game start (invoking GameOfGreed class object method play()).

## Change Log
Mon Dec 09 2019 16:34:04<br>Created Game of Greed Module. Tested for app functionality and correct results. 

