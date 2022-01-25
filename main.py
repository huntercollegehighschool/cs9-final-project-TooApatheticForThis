"""
Name(s): Jamie Schechner
Name of Project: Jamie's Battle Simulator

This was a bit of an ambitious project for me (I have never coded outside of this class), and there are a few bugs that I likely either missed or simply wasn't able to figure out how to solve.
"""

import random
import time
import os

wins = 0

defense = 10
health = 25

enemy = 'unused'
position = 'unused'

print("You are playing Jamie\'s Battle Simulator.")
time.sleep(2)
print("\nHow to play: \n\nYou will be given 3 enemies to fight. In each attack sequence, you can choose to move to the Left, Middle, or Right. These positions effect attack success probabilities and damage output. You will then be able to pick a weapon to use. Each weapon has different damage, with the higher damage weapons having a much lower chance to hit the target.\n\nIn the final fight, you will have to think outside of the box and use weapons that are not labled. Use your imagination. Good Luck!\n")
time.sleep(2)
print("Type \'Start\' to begin.")
startornot.lower() = input("")

def fight(enemy):
  position = 'middle'
  miss = True
  defense = 5
  health = 25
  Weaponvalue = 0
  extrahealth = 0
  print("You've entered combat with",enemy,"!")
  print("")
  if enemy == "Bear":
    Ehealth = 30
    Eattack = 3
    Edefense = 3
  if enemy == "Police Officer":
    Ehealth = 25
    Eattack = 15
    Edefense = 10
  if enemy == "Jesus Christ":
    Ehealth = 9999999999999999999999999999999999999999999
    Eattack = -100
    Edefense = 99 # <-- He turns the other cheek
  time.sleep(.05)
  while Ehealth > 0 and health > 0:
    time.sleep(1)
    time.sleep(1)
    position = input("You can move to the following positions: Left, Middle, Right.\n")
    time.sleep(1)
    print('You are in the',position,'position.\n\nTime to Attack.')
    time.sleep(1)
    print("\nWhich weapon would you like to use?\n")
    time.sleep(1)
    if enemy == 'Police Officer':
      print("Current Available Weapons: Missile Launcher, Pistol, Fist, Medkit")
    elif enemy == 'Bear':
      print("Current Available Weapons: Plastic Explosive, Bear Spray, Fist, Medkit")
    elif enemy == 'Jesus Christ':
      print("Current Available Weapons: Crucifix, (un)Holy Water, Bible, Medkit, ???")
    x = input("")
    if x.lower() == 'missile launcher' and enemy == 'Police Officer':
      roll = (random.randint(1,100))
      if position.lower() == 'left':
        roll -= 15
      elif position.lower() == 'right':
        roll += 15
      if roll > 25:
        print("")
        print("Your Missile Launcher missed!")
        miss = True
      elif roll <= 25:
        Weaponvalue += (random.randint(15,70))
        if position == 'left':
          Weaponvalue -= 5
        elif position == 'right':
          Weaponvalue += 5
        print("")
        print("PEEEWWWWW!!!")
        miss = False
    elif x.lower() == 'missile launcher' and enemy != 'Police Officer':
      print("")
      print("That weapon is not currently usable.")
      miss = True
    elif x.lower() == 'plastic explosive' and enemy == 'Bear':
      roll = (random.randint(1,100))
      if position.lower() == 'left':
        roll -= 15
      elif position.lower() == 'right':
        roll += 15
      if roll > 25:
        print("")
        print("Your Plastic Explosive didn't go off!")
        miss = True
      elif roll <= 25:
        Weaponvalue += (random.randint(15,70))
        if position == 'left':
          Weaponvalue -= 5
        elif position == 'right':
          Weaponvalue += 5
        print("")
        print("BOOOOOM!")
        miss = False
    elif x.lower() == 'plastic explosive' and enemy != 'Bear':
      print("")
      print("That weapon is not currently usable.")
      miss = True
    elif x.lower() == 'crucifix' and enemy == 'Jesus Christ':
      roll = (random.randint(1,100))
      if position.lower() == 'left':
        roll -= 15
      elif position.lower() == 'right':
        roll += 15
      if roll > 25:
        print("")
        print("Your Crucifix rotted and fell over (oops)!")
        miss = True
      elif roll <= 25:
        Weaponvalue += (random.randint(15,70))
        if position == 'left':
          Weaponvalue -= 5
        elif position == 'right':
          Weaponvalue += 5
        print("")
        print("*Stomach Growling Noises*")
        miss = False
    elif x.lower() == 'crucifix' and enemy != 'Jesus Christ':
      print("")
      print("That weapon is not currently usable.")
      miss = True
    elif x.lower() == 'pistol' and enemy == 'Police Officer':
      roll = (random.randint(0,100))
      if position.lower() == 'left':
        roll -= 15
      elif position.lower() == 'right':
        roll += 15
      if roll > 60:
        print("")
        print("Your pistol missed!")
        miss = True
      elif roll <= 60:
        Weaponvalue += (random.randint(5,30))
        if position == 'left':
          Weaponvalue -= 5
        elif position == 'right':
          Weaponvalue += 5
        print("")
        print("Bang! Bang! Bang!")
        miss = False
    elif x.lower() == 'pistol' and enemy != 'Police Officer':
      print("")
      print("That weapon is not currently usable.")
      miss = True
    elif x.lower() == 'bear spray' and enemy == 'Bear':
      roll = (random.randint(0,100))
      if position.lower() == 'left':
        roll -= 15
      elif position.lower() == 'right':
        roll += 15
      if roll > 60:
        print("")
        print("Your bear spray can didn't spray!")
        miss = True
      elif roll <= 60:
        Weaponvalue += (random.randint(5,30))
        if position == 'left':
          Weaponvalue -= 5
        elif position == 'right':
          Weaponvalue += 5
        print("")
        print("Kchsssssshhhhhhhh!")
        miss = False
    elif x.lower() == 'bear spray' and enemy != 'Bear':
        print("")
        print("That weapon is not currently usable.")
        miss = True
    elif x.lower() == '(un)Holy Water' or 'Holy Water' and enemy == 'Jesus Christ':
      roll = (random.randint(0,100))
      if position.lower() == 'left':
        roll -= 15
      elif position.lower() == 'right':
        roll += 15
      if roll > 60:
        print("")
        print("You dropped your (un)Holy Water in His divine presence!")
        miss = True
      elif roll <= 60:
        Weaponvalue += (random.randint(5,30))
        if position == 'left':
          Weaponvalue -= 5
        elif position == 'right':
          Weaponvalue += 5
        print("")
        print("*Splish splash take an un-holy bath*")
        miss = False
      elif x.lower() == '(un)Holy Water' or 'Holy Water' and enemy != 'Jesus Christ':
        print("")
        print("That weapon is not currently usable.")
    elif x.lower() == 'fist' and enemy != 'Jesus Christ':
      roll = (random.randint(0,100))
      if roll <= 99:
        Weaponvalue += (random.randint(2,4))
        print("")
        print("Pow! Kablam!")
        miss = False
      elif roll > 99:
        print("")
        print("You missed! How?")
        miss = True
    elif x.lower() == 'fist' and enemy == 'Jesus Christ':
      print("")
      print("Why would you punch Jesus????????")
      miss = True
    elif x.lower() == 'medkit':
      print("")
      extrahealth = (random.randint(10,20))
      defense += (random.randint(5,10))
      miss = True
    elif x.lower() == 'satanic ritual' or 'bible' or 'prayer' or 'god' or 'religion' or 'judaism' or 'islam' or 'buddhism' or 'hinduism' or 'paganism' and enemy != 'Jesus Christ':
      if enemy == 'Bear':
        print("The bear looks confused at your silliness.")
      elif enemy == 'Police Officer':
        print("The disgruntled officer rolls his eyes. What effect could this possibly have?")
    elif x.lower == 'satanic ritual' or 'bible' or 'prayer' or 'god' or 'religion' or 'judaism' or 'islam' or 'buddhism' or 'hinduism' or 'paganism' and enemy == 'Jesus Christ':
      print("Your holy hellfire rains down onto the good Lord's child. You hurt him immensely.")
      Weaponvalue += 9999999999999999999999999999999999999999999999999999999999999999999999999
      miss = False
    else:
      print("")
      print("You didn't select a viable weapon and will not use one.")
      time.sleep(1)
      print("(sux 4 u)")
      miss = True
    time.sleep(1)
    Tdefense = defense + (random.randint(-10,10))
    TEdefense = Edefense + (random.randint(-5,5))
    if miss == False:
      Fdam = (random.randint(0,10)) + Weaponvalue
    elif miss == True:
      Fdam = 0
    if extrahealth == 0:
      Tdam = Fdam - TEdefense
    elif extrahealth > 0:
      Tdam = 0
    Ehealth = Ehealth - Tdam 
    if TEdefense < 0:
      TEdefense = 0
    if Fdam == 0 and extrahealth > 0:
      print("You healed",extrahealth,"health.")
    elif Tdam > 0:
      print("You did",Fdam,"Damage, but",enemy,"blocked",TEdefense,"damage!",enemy,"took",Tdam,"damage.")
    elif Tdam == 0:
      print("You did",Fdam,"Damage, but",enemy,"blocked",TEdefense,"Damage! No damage was dealt.")
    elif Tdam < 0:
      print("You did",Fdam,"Damage, but",enemy,"blocked",TEdefense,"Damage!",enemy,"healed",abs(Tdam),"health.")
    print("")
    time.sleep(1)
    Edam = (random.randint(5,15)) + Eattack
    ETdam = Edam - Tdefense
    health = health - ETdam
    if Tdefense < 0:
      Tdefense = 0
    print(enemy,"prepares to attack!")
    print("")
    time.sleep(2)
    if ETdam > 0:
      print(enemy,"did",Edam,"Damage, but you blocked",Tdefense,"damage!",enemy,"did",ETdam,"damage.")
    elif ETdam == 0:
      print(enemy,"did",Edam,"Damage, but you blocked",Tdefense,"damage! No damage was dealt.")
    elif ETdam < 0:
      print(enemy,"did",Edam,"Damage, but you blocked",Tdefense,"damage! You healed",(ETdam),"health.")
    print("")
    health = health + extrahealth
    if health > 100:
      health = 100
    if health > 100:
      Ehealth = 100
    Weaponvalue = 0
    ETdam = 0
    Edam = 0
    Tdam = 0
    Fdam = 0
    extrahealth = 0
    time.sleep(2)
    print("You have",health,"health.")
    time.sleep(1)
    if enemy != 'Jesus Christ':
      print(enemy,"has",Ehealth,"health.")
    else:
      print('In his divineness, Jesus Christ has infinite health. You cannot hope to hurt him in his godly power.')
    time.sleep(4)
    if health > 0 and Ehealth > 0:
      os.system('clear')
      time.sleep(1)
      print("It's your turn again.\n")
    elif health > 0 and Ehealth <= 0:
      print("Congratulations! You won the battle.")
      time.sleep(2)
      os.system('clear')
    elif Ehealth > 0 and health <= 0:
      print("You died.")
      exit()
    elif Ehealth < 0 and health < 0:
      print("You and",enemy,"died. While you have won this fight, there will be no others in your future.")
      exit()

if startornot == ("Start"):
  fight("Bear")
  if health > 0:
    wins += 1

x = input("To move to the next stage, type 'Next'.")
if wins == 1 and x == 'Next':
  fight("Police Officer")
  if health > 0:
    wins += 1
  
y = input("To move to the next stage, type 'Next'.")
if wins == 2 and y == 'Next':
  fight("Jesus Christ")
  if health > 0:
    print("You've won this simulation! Congratulations.")
