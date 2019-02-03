name=input("Enter your name")
while name.isalpha()==False or len(name)<6:
      name=input("your name is wrong please enter again")
else:
    print("Hello",name)
age=(input("Enter your age"))
while age.isdigit()==False :
      age=input("your age is wrong please enter again")
else:
    print("your age is accepted",age)
password=int(input("Enter your password"))
password=int(1234567)
while True:
        if password ==1234567:
            print("your password is accepted")
            break
        else:
            password("your password is wrong please enter again")
count = 0

choice=input(" \n 1.Play Game \n 2.Exit\n")
while choice != "2":

  if choice =="1":
    print("Game begins...")
    import random

    game_word =["rock","paper","scissor"]
    pc_result = random.choice(game_word)


    user_word = str(input("Enter in small letter type :'rock','paper','scissor':"))
    game_word = ['rock','paper','scissor']
    pc_result = random.choice(game_word)


  if pc_result =='rock' and user_word =='paper' :
     print('you win')
     count= count + 1
  elif pc_result == 'paper' and user_word == 'scissor':
     print("you win")
     count=count + 1
  elif pc_result == 'scissor' and user_word == 'rock':
     print("you win")
     count=count + 1
  elif pc_result == 'rock' and user_word == 'scissor':
     print("you lose")
  elif pc_result =='paper' and user_word == 'rock':
     print("you lose")
  elif pc_result == 'scissor' and user_word == 'paper':
    print("you lose")
  else:
    print("MATCH IS DRAW...")

  print("you have entered :",user_word)
  print("computer entered :",pc_result)
  print("your score is ",count)

  print("\n you wanna play again")
  if choice == "2":
    print("exit")
choice = input("\n 1. play game \n 2.exit\n")
