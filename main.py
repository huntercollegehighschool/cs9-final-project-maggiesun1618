"""
Name(s): Maggie Sun
Name of Project: Hangman
"""

#Write the main part of your program here. Use of the other pages is optional.
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
wrongguesses = []
ownlist = []

from drawing import *
import random
import os
from words import wordlist


def play():
  thing.penup()
  thing.setpos(-20,-70)
  draw_gallow(thing, '#000000')
  topic = input("Enter the corresponding number to one of the following topics from which the phrase will be chosen:\n1.Effects of sleep deprivation\n2.Names that I stole from Rachel Chen's project\n3.1st century Roman emperors\n4.Absolutly anything; I'm experiencing choice paralysis and do not want to deal with this\n5.Enter your own word/phrase (alphabet only, spaces allowed)\n6.Enter your own list of words/phrases to randomly choose from (alphabet only, spaces allowed)\n")
  while topic != "1" and topic != "2" and topic != "3" and topic != "4" and topic != "5" and topic != "6":
    topic = input("Please input one of the numbers on the list: ")
  if topic == "1":
    word = random.choice(wordlist[0])
  elif topic == "2":
    word = random.choice(wordlist[1])
  elif topic == "3":
    word = random.choice(wordlist[2])
  elif topic == "4":
    placeholder = random.choice(wordlist)
    word = random.choice(placeholder)
  elif topic == "5":
    word = input("Enter your own word or phrase: ")
    word = word.upper()
  elif topic == "6":
    ownchoice = input("Enter a word or phrase to be a part of your list, or enter 0 to end the list: ")
    while ownchoice != "0":
      ownlist.append(ownchoice.upper())
      print("Your current list of words is: ",ownlist)
      ownchoice = input("Enter a word or phrase to be a part of your list, or enter 0 to end the list: ")
    word = random.choice(ownlist)
  breakdown = len(word) * "_"
  breakdown = list(breakdown)
  for i in range(len(word)):
    if " " in word[i]:
      breakdown[i] = " "
  while "_" in breakdown:
    os.system("clear")
    print("".join(breakdown))
    print("Incorrect guesses: ", "".join(wrongguesses))
    print("Number of incorrect guesses left: ", 9 - len(wrongguesses))
    letter = input("Enter a letter as a guess: ")
    while len(letter) > 1 or letter.upper() in wrongguesses or letter.upper() in breakdown:
      if len(letter) > 1:
        letter = input("Please enter a single letter: ")
      if letter.upper() in wrongguesses or letter.upper() in breakdown:
        letter = input("You have already entered this letter before. Enter a different letter as a guess: ")
    letter = letter.upper()
    for i in range(len(word)):
      if letter == word[i]:
        breakdown[i] = letter
    if letter not in word and len(wrongguesses) < 9:
      wrongguesses.append(letter)
      if len(wrongguesses) == 1:
        draw_head(thing, '#000000')
      elif len(wrongguesses) == 2:
        draw_spine(thing,'#000000')
      elif len(wrongguesses) == 3:
        draw_leftarm(thing,'#000000')
      elif len(wrongguesses) == 4:
        draw_rightarm(thing,'#000000')
      elif len(wrongguesses) == 5:
        draw_leftleg(thing,'#000000')
      elif len(wrongguesses) == 6:
        draw_rightleg(thing,'#000000')
      elif len(wrongguesses) == 7:
        draw_lefteye(thing,'#000000')
      elif len(wrongguesses) == 8:
        draw_righteye(thing,'#000000')
      elif len(wrongguesses) == 9:
        draw_mouth(thing,'#000000')
    if len(wrongguesses) == 9:
        for i in range(len(word)):
          breakdown[i] = word[i]
  os.system("clear")
  print("The answer was: ","".join(breakdown))
  print("Incorrect guesses: ", "".join(wrongguesses))
  print("Number of incorrect guesses left: ", 9 - len(wrongguesses))
  if len(wrongguesses) == 9:
    print("You lost!")
  elif len(wrongguesses) < 9:
    print("You won! Congratulations on not dying!")
 
def playagain():
  play2 = input("Do you want to play again? Type 'YES' if you do; type 'NO' to end the game. Note that if you chose to enter your own list of words/phrases, that list will still be saved if you replay. ")
  while play2.upper() == 'YES':
    os.system("clear")
    wrongguesses.clear()
    turtle.resetscreen()
    play()
    play2 = input("Do you want to play again? Type 'YES' if you to play again; type 'NO' to end the game. ")
  if play2.upper() == 'NO':
    os.system("clear")

play()
playagain()


    

  

