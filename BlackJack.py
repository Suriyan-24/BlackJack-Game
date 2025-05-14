card=[[" ___ "], ["|", "N", "  |"], ["| ", "#", " |"], ["|__", "N", "|"]]
symbols_list=["♠", "♥", "♦", "♣"]
denotion_list=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
mystery_card=[[" ___ "], ["|", " ", "  |"], ["| ", "⍰", " |"], ["|__", " ", "|"]]

user_print_list=[]
computer_print_list=[]

import random

def user_card(round):

      symbol=""
      symbol_1=""
      symbol_2=""
      symbol=""
      denotion=""
      denotion_1=""
      denotion_2=""

      symbol_1=random.choice(symbols_list)
      symbol_2=random.choice(symbols_list)
      symbol=random.choice(symbols_list)
      denotion_1=random.choice(denotion_list)
      denotion_2=random.choice(denotion_list)
      denotion=random.choice(denotion_list)

      user_card_1=[[" ___ "], ["|", "N", "  |"], ["| ", "#", " |"], ["|__", "N", "|"]]
      user_card_2=[[" ___ "], ["|", "N", "  |"], ["| ", "#", " |"], ["|__", "N", "|"]]
      user_card=[[" ___ "], ["|", "N", "  |"], ["| ", "#", " |"], ["|__", "N", "|"]]
      
      user_card_1[1][1]=user_card_1[3][1]=denotion_1
      user_card_1[2][1]=symbol_1
      user_card_2[1][1]=user_card_2[3][1]=denotion_2
      user_card_2[2][1]=symbol_2
      user_card[1][1]=user_card[3][1]=denotion
      user_card[2][1]=symbol
      
      if round==1:

            print("Your cards are:")
            
            for list in user_card_1:
                  print("\n",end="")
                  for element in list:
                        print(element,end="")

            for list in user_card_2:
                  print("\n",end="")
                  for element in list:
                        print(element,end="")

            user_value=[denotion_1, denotion_2]
            return user_value

      elif round==2:

            print("\nYour card is:")

            for list in user_card:
                  print("\n",end="")
                  for element in list:
                        print(element,end="")

            user_value=denotion
            return user_value

def computer_card(round):

      symbol=""
      symbol_1=""
      symbol_2=""
      denotion=""
      denotion_1=""
      denotion_2=""

      symbol_1=random.choice(symbols_list)
      symbol_2=random.choice(symbols_list)
      denotion_1=random.choice(denotion_list)
      denotion_2=random.choice(denotion_list)
      denotion=random.choice(denotion_list)

      computer_card_1=[[" ___ "], ["|", "N", "  |"], ["| ", "#", " |"], ["|__", "N", "|"]]
      computer_card_2=[[" ___ "], ["|", "N", "  |"], ["| ", "#", " |"], ["|__", "N", "|"]]
      computer_card=[[" ___ "], ["|", "N", "  |"], ["| ", "#", " |"], ["|__", "N", "|"]]
      mystery_card=[[" ___ "], ["|", " ", "  |"], ["| ", "⍰", " |"], ["|__", " ", "|"]]
      computer_card_1[1][1]=computer_card_1[3][1]=denotion_1
      computer_card_1[2][1]=symbol_1
      computer_card_2[1][1]=computer_card_2[3][1]=denotion_2
      computer_card_2[2][1]=symbol_2
      computer_card[1][1]=computer_card[3][1]=denotion
      computer_card[2][1]=symbol

      if round==1:

            print("\n\nComputer's cards are:")

            for list in computer_card_1:
                  print("\n",end="")
                  for element in list:
                        print(element,end="")

            for list in mystery_card:
                  print("\n",end="")
                  for element in list:
                        print(element,end="")

            computer_value=[denotion_1, denotion_2]
            return computer_value

      elif round==2:

            print("\n\nComputer's card is:")

            for list in mystery_card:
                  print("\n",end="")
                  for element in list:
                        print(element,end="")

            computer_value=denotion
            return computer_value

print("Welcome to the Black Jack game.")
print("""
Instructions:
✯ When the game starts, you will be given two random cards.
✯ The computer will be assigned to random cards, one of which will not be revealed.
✯ You may choose to obtain another card, where the computer will also be assigned another card.
✯ King, Queen or Jack equals 10. 
✯ Whomsoever reaches the number closest to 21 wins.
✯ If you reach a number greater than 21, you lose.""")

print("Click enter to start the game.")
input()

continue_game=True
another_card=False
extra_user_value=extra_computer_value=0

while continue_game==True:

      user_value=0
      computer_value=0
      
      user_values=user_card(1)
      computer_values=computer_card(1)

      for element in user_values:
            if element in ["K", "J", "Q"]:
                  element=10
            elif element=="A":
                  element=1
            user_print_list.append(element)
            user_value+=int(element)

      for element in computer_values:
            if element in ["K", "J", "Q"]:
                  element=10
            elif element=="A":
                  element=1
            computer_print_list.append(element)
            computer_value+=int(element)

      choice_1=input("\nTry getting another card? (y/n): ")
      if choice_1=="y":
            another_card=True
      elif choice_1=="n":
            another_card=False

      while another_card==True:

            extra_user_value=user_card(2)
            extra_computer_value=computer_card(2)

            if extra_user_value in ["K", "J", "Q"]:
                  extra_user_value=10
            elif extra_user_value=="A":
                  extra_user_value=1
            user_print_list.append(extra_user_value)
            user_value+=int(extra_user_value)

            if extra_computer_value in ["K", "J", "Q"]:
                  extra_computer_value=10
            elif extra_computer_value=="A":
                  extra_computer_value=1
            computer_print_list.append(extra_computer_value)
            computer_value+=int(extra_computer_value)

            if user_value>=21 or computer_value>=21:
                  another_card=False
            else:
                  choice_1=input("\n\nTry getting another card? (y/n): ")
                  if choice_1=="y":
                        another_card=True
                  elif choice_1=="n":
                        another_card=False

      print("\n")

      print("Your card values are:", user_print_list)
      print("Computer's card values are:", computer_print_list)


      print("\n")
      print("The total value you've got: ", user_value)
      print("The total value computer's got: ", computer_value)
      print("\n")
      
      if user_value<=21 and computer_value>21:
            print("You win!")
      elif computer_value<=21 and user_value>21:
            print("Computer wins!")
      elif user_value==computer_value:
            print("It is a draw!")
      elif user_value<=21 and computer_value<=21:
            if user_value>computer_value:
                  print("You win!")
            elif computer_value>user_value:
                  print("Computer wins!")

      print("Good game.")
      
      choice_2=input("\nPlay another game? (y/n): ")
      if choice_2=="y":
            continue_game=True
      elif choice_2=="n":
            continue_game=False
