# Assignment 4: Blackjack

> [!IMPORTANT]
> This assignment is to be completed individually. It is not a team project.  You must document (using comments in your code) all resources (beyond our official textbook, Canvas, the class discussion forum, or the class website) that you used to help you complete this assignment. For example, if you referenced a code example from an online website such as Stackoverflow or github you could acknowledge it as follows: 
>
> ```
> # Next we print 'Hello, World' to the console.
> # Based on help from: https://stackoverflow.com/questions/826948/syntax-error-on-print-with-python-3
> print("Hello, world!")
> ```
>
> You must provide an attribution to any resource you consulted to complete this assignment except for our official textbook, Canvas, the class discussion forum, or the class website. Resources that require attribution include — but are not limited to — AI tools (even those built in to VS Code), websites, books, notes from other students, tutors, or help from other people (friends, classmates, etc.). Under no circumstances are you to look at or copy any material related to another person's solution for this assignment.
>
> To repeat, you must attribute any resource you consulted to complete this assignment other than our official textbook, Canvas, class discussion forum, or the class website. You must cite all AI technologies you used, if any, to complete this assignment. Failure to provide attribution is a violation of the honor code.

## Overview

Blackjack, also know as twenty-one, is a card game that is played at casinos around the world. In casinos, players bet money on each hand (with, as you would expect in a casino, the odds stacked in favor of the dealer). Point-based variants of the game are also popular, including a large number of Blackjack Phone Apps for Android and iPhone. You can [read more about the game on Wikipedia](https://en.wikipedia.org/wiki/Blackjack).

In this assignment we'll be developing a simplified version of Blackjack. Our version will proceed as follows:

At the start of a new hand, the player will be dealt two cards. The player will then choose, with a goal of obtaining a set of cards that sum as close to 21 as possible without going over, to either "HIT" (get an additional card to add to the player's hand) or "STAY" (stick with the player's existing hand of cards). If the sum of the values of all cards in a player's hand ever goes over 21, they player immediately loses the hand. We call this way of losing "going bust." If the player chooses to STAY before going bust (i.e., with a hand value of 21 or less), it becomes the dealer's turn.

For our game, the dealer is the computer. In the **Basic Requirements**, you should assign the computerized dealer a score at random within in the range 16-21. We'll look at a more sophisticated approach in the **Advanced Requirements** below. This computerized dealer score will then be compared to the player's total hand value. If the computer's score is greater than or equal to the player's total hand value (and not over 21), then the player loses the hand. Otherwise, the player wins!

**The deck of cards:** Traditionally, a deck of playing cards contains 52 cards, with 13 different card values (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King), each of which is found in four distinct suits (Hearts, Diamonds, Spades, and Clubs). In this assignment, we'll ignore suits. For the **Basic Requirements**, we'll further simplify things to use a deck of cards that has the values from 1 through 10. Moreover, we'll ignore the fact that when playing with real cards, each card can only be used once in a given hand. These assumptions let us simplify the process of dealing a card to the generation of a random number in the range of 1 to 10. For this assignment's **Advanced Requirements**, we'll add some of this complexity back into the program.


## Basic Requirements

> [!NOTE]
> Satisfying only the basic requirements perfectly, with no points deducted for any reason, would earn a maximum score of 8 out of 10 for this assignment.

You are to implement the basic blackjack game as outlined above. It should provide clear prompts and displays to the user along they way. These prompts should be clear enough to tell the user all they need to play the game, and to determine who wins each hand. The basic flow of the game should be as follows:

* Deal two cards to the user, compute the sum, and display it to the user. (Remember, a card is just a random number form 1 to 10).
* Ask the user if he/she wishes to HIT or STAY.
* Each time the user chooses to HIT, deal him/her a new card, update the total, and check to see if he/she has gone bust (over the limit of 21).
* Eventually, the player will choose to stay or go bust. If the player goes bust, he/she automatically loses. If not, then the computer gets its turn.
* Generate the computer's score and compare it to the player's score and determine who wins. The computer's score should be a random number between 16 and 21.
* Ask the user if he or she is ready to play a new hand of blackjack. If so, your program should go to back to step 1. If not, your program should quit.

Developing the solution for this program would be quite challenging without using functions. To make your job easier, think about how functions can be used to simplify the design. Your solution should have, at a minimum, the following functions:

* **main**: the main function, which should have the main loop that repeats for each hand
* **get_player_score**: handles the initial deal of two cards to the player and the "HIT or STAY" loop. It should return the final player score.
* **deal_card**: generate a card value for the player (using random). This should be used within the get_player_score function. The value should be between 1 and 10.
* **get_dealer_score**: generate the dealer's score (using random)

You may find that additional functions are useful to modularize your design. Adding more functions when appropriate is perfectly fine! However, the four functions identified above are REQUIRED.

The output produced by your program should be nearly identical to the sample output provided below. While the numbers will vary because of the use of random numbers, the prompts and messages printed to the console when using your program should match those in the sample output to receive full credit.


## Advanced Requirements

> [!NOTE]
> Satisfying both the basic and advanced requirements perfectly, with no points deducted for any reason, will result in a full 10 out of 10 score for this assignment.

Expand on the basic requirements by extending your program as follows.

* Make the function deal_card more sophisticated by accounting for Jacks, Queens and Kings. They all have the same value as a 10, which means that values of 10 should be four times more likely other values. Thanks to the power of functions, this change should not impact any of your code outside of the deal_card function.
* Make the dealer more sophisticated. To do this, you'll need to make two extensions to your basic program:
    * Make the function get_dealer_score more sophisticated by using individual cards to determine the value of the dealer's hand rather than simply choosing a random value. Your get_dealer_score function should behave as follows:
        * Deal two cards, and sum the value.
        * As long as the dealer's sum is below 16, deal another card and add it to the total.
    * When comparing the dealer's score to the player's score (step 6 in the basic requirements description), the computer can "go bust" as well as the human player. If the dealer's score goes over 21, the player should win.

## Sample Output

The following is an example of the output that should be produced by your solution:

```
Your hand of two cards has a total value of 11.
Would you like to take another card? (y/n) y
Your hand now has a total value of 15.
Would you like to take another card? (y/n) y
Your hand now has a total value of 20.
Would you like to take another card? (y/n) n
You have stopped taking more cards with a hand value of 20.
The dealer was dealt a hand with a value of 20.

** You lose! **

Would you like to play again? (y/n) y
Your hand of two cards has a total value of 11.
Would you like to take another card? (y/n) y
Your hand now has a total value of 15.
Would you like to take another card? (y/n) y
You BUSTED with a total value of 25!

** You lose. **

Would you like to play again? (y/n) y
Your hand of two cards has a total value of 17.
Would you like to take another card? (y/n) n
You have stopped taking more cards with a hand value of 17.
The dealer BUSTED with a value of 25!

** You win! **

Would you like to play again? (y/n) n
```


## Grading Criteria

This assignment will be graded on a 10 point scale. Your grade for this assignment will be based on a combination of factors, including:

* Correct functionality (e.g., Does your Python code do what it is supposed to do as outlined in the basic and/or advanced requirements?)
* Clarity of your solution (e.g., Did you solve the problem directly and efficiently? Or is your answer excessively complex and/or inefficient?)
* Coding style (e.g., Is your code readable with comments, meaningful variable names, and good whitespace/indentation?)
* Meets submission requirements (see below)

## Seeking Help

For general questions about Python, please use the class forum on Piazza to seek assistance. For questions that are personal in nature or that would reveal a solution to the assignment, you ask for help by email or during office hours. However, please note that emailed questions will not receive an immediate response. It is likely that it will take 24-48 hours for me to respond.

## Submitting Your Solution

When you have completed your work on the assignment, it is time to submit your solution via Canvas.  You can submit your assignment by taking the following steps:
1. Be sure that all of your changes have been pushed to your GitHub repository for the assignment.
2. Go to the web page for your repository on github.com
3. Click the green button labeled "< > Code &#9660;" which should open a popup menu.
4. From the popup menu, click on "Download ZIP" which will download a zip file containing your entire project to your computer. 
5. Submit the zip file you just downloaded via Canvas as your solution for this assignment.


> [!WARNING]
> NOTE FOR MAC USERS: Mac users who use the Safari browser will notice that the browser will, by default, automatically unzip and delete zip files you download from the internet. To change this behavior, press and hold the Option key when clicking the "Download ZIP" menu item.  This will prevent Safari from automatically unzipping and deleting the Zip file. Instead, it will just download the Zip file as it is just as you would get on any other browser.  Only Safari users need to take this extra step.


## Due Date

The due date for this assignment can be found in the official class schedule and on Canvas.

