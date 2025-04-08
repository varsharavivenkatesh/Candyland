# Varsha Ravivenkatesh 11-17-2024
# Assignment 5
#
# This is a computer version of the classic boardgame 'Candy Land' and is called as 'Candy Realm! where you can play with 3 other people or AI'
import random
from colorama import Fore, Back, Style 
print("Candy Realm!")
print("By: Varsha Ravivenkatesh")
print("[COM S 127 1]")
print("-"*30)

def instructions():
    print("\nThis is a game of candy land")
    print("You can play with friends or with a computer")
    print("You Start at point S and move as you are dealt cards")
    print("First person to reach the color just before the * is the winner")

def print_positions(position1, position2, position3, position4):  
    print(" " * position1 + "1")
    print(" " * position2 + "2")
    print(" " * position3 + "3")
    print(" " * position4 + "4")  
      
def playing():
    while True:
        players=int(input("\nHow Many Human Players [1] - [4]?:" ))
        try:
            if players not in (1,2,3,4):
                raise ValueError
            c=4
            lastpos1=lastpos2=lastpos3=lastpos4=0
            position1=position2=position3=position4=0
            board1="S R P G B V O P Y R B V O G P B O G R Y B G V P R O G B O R V * "
            board2="\033[37mS \033[31mR \033[35mP \033[32mG \033[34mB \033[34mV \033[33mO \033[35mP \033[33mY \033[31mR \033[34mB \033[34mV \033[33mO \033[32mG \033[35mP \033[34mB \033[33mO \033[32mG \033[31mR \033[33mY \033[34mB \033[32mG \033[34mV \033[35mP \033[31mR \033[33mO \033[32mG \033[34mB \033[33mO \033[31mR \033[34mV \033[37m*  "
            if players==1:
                    while True:
                        if c%4==0:
                            while True:
                                try:
                                    choice=input("Player 1 would you like to [d]raw or [q]uit:")
                                    if choice not in ('d','q'):
                                        raise ValueError
                                    if choice=='q':
                                        return
                                    else:
                                        card=cards()
                                        position1=find_next_position(board1, lastpos1, card)  
                                        lastpos1=position1
                                        
                                        print_positions(position1, position2, position3, position4)
                                        print(board2)
                                        print("^")
                                        print('|')
                                        print("START HERE")
                                        print('Player 1 has drawn', card)
                                        c+=1
                                        if position1 == 60:
                                            print("\nPlayer 1 wins!")
                                            return
                                        break
                                except ValueError:
                                    print('Invalid Input please type again') 
                                    continue   

                            
                        elif c%4==1:
                            card=cards()
                            position2=find_next_position(board1, lastpos2, card)  
                            lastpos2=position2
                            print_positions(position1, position2, position3, position4)
                            print(board2)
                            print("^")
                            print('|')
                            print("START HERE")
                            print('Player 2(Computer) has drawn', card)
                            c+=1
                            if position2==60:
                                print("\nPlayer 2(Computer) wins!")
                                return

                                
                        elif c%4==2:
                            card=cards()
                            position3=find_next_position(board1, lastpos3, card)  
                            lastpos3=position3
                            print_positions(position1, position2, position3, position4)
                            print(board2)
                            print("^")
                            print('|')
                            print("START HERE")
                            print('Player 3(Computer) has drawn', card)
                            c+=1
                            if position3==60:
                                print("\nPlayer 3(Computer) wins!")
                                return
                            
                            
                        elif c%4==3:
                            card=cards()
                            position4=find_next_position(board1, lastpos4, card)  
                            lastpos4=position4
                            print_positions(position1, position2, position3, position4)
                            print(board2)
                            print("^")
                            print('|')
                            print("START HERE")

                            print('\nPlayer 4(Computer) has drawn', card)
                            c+=1
                            if position4==60:
                                print("Player 4(Computer) wins!")
                                return
                            
                            
            if players==2:
                while True:
                        if c%4==0:
                            while True:
                                try:
                                    choice=input("Player 1 would you like to [d]raw or [q]uit:")
                                    if choice not in ('d','q'):
                                        raise ValueError
                                    if choice=='q':
                                        return
                                    else:
                                        card=cards()
                                        position1=find_next_position(board1, lastpos1, card)  
                                        lastpos1=position1
                                        
                                        print_positions(position1, position2, position3, position4)
                                        print(board2)
                                        print("^")
                                        print('|')
                                        print("START HERE")
                                        print('Player 1 has drawn', card)
                                        c+=1
                                        if position1 == 60:
                                            print("\nPlayer 1 wins!")
                                            return
                                        break
                                except ValueError:
                                    print('Invalid Input please type again') 
                                    continue   

                            
                        elif c%4==1:
                            while True:
                                try:
                                    choice=input("Player 2 would you like to [d]raw or [q]uit:")
                                    if choice not in ('d','q'):
                                        raise ValueError
                                    if choice=='q':
                                        return
                                    else:
                                        card=cards()
                                        position2=find_next_position(board1, lastpos2, card)  
                                        lastpos2=position2
                                        
                                        print_positions(position1, position2, position3, position4)
                                        print(board2)
                                        print("^")
                                        print('|')
                                        print("START HERE")
                                        print('Player 2 has drawn', card)
                                        c+=1
                                        if position2 == 60:
                                            print("\nPlayer 2 wins!")
                                            return
                                        break
                                except ValueError:
                                    print('Invalid Input please type again') 
                                    continue   


                                
                        elif c%4==2:
                            card=cards()
                            position3=find_next_position(board1, lastpos3, card)  
                            lastpos3=position3
                            print_positions(position1, position2, position3, position4)
                            print(board2)
                            print("^")
                            print('|')
                            print("START HERE")
                            print('Player 3(Computer) has drawn', card)
                            c+=1
                            if position3==60:
                                print("\nPlayer 3(Computer) wins!")
                                return
                            
                            
                        elif c%4==3:
                            card=cards()
                            position4=find_next_position(board1, lastpos4, card)  
                            lastpos4=position4
                            print_positions(position1, position2, position3, position4)
                            print(board2)
                            print("^")
                            print('|')
                            print("START HERE")

                            print('Player 4(Computer) has drawn', card)
                            c+=1
                            if position4==60:
                                print("\nPlayer 4(Computer) wins!")
                                return
                            
                
            if players==3:
                while True:
                        if c%4==0:
                            while True:
                                try:
                                    choice=input("Player 1 would you like to [d]raw or [q]uit:")
                                    if choice not in ('d','q'):
                                        raise ValueError
                                    if choice=='q':
                                        return
                                    else:
                                        card=cards()
                                        position1=find_next_position(board1, lastpos1, card)  
                                        lastpos1=position1
                                        
                                        print_positions(position1, position2, position3, position4)
                                        print(board2)
                                        print("^")
                                        print('|')
                                        print("START HERE")
                                        print('Player 1 has drawn', card)
                                        c+=1
                                        if position1 == 60:
                                            print("\nPlayer 1 wins!")
                                            return
                                        break
                                except ValueError:
                                    print('Invalid Input please type again') 
                                    continue   
                                

                            
                        elif c%4==1:
                            while True:
                                try:
                                    choice=input("Player 2 would you like to [d]raw or [q]uit:")
                                    if choice not in ('d','q'):
                                        raise ValueError
                                    if choice=='q':
                                        return
                                    else:
                                        card=cards()
                                        position2=find_next_position(board1, lastpos2, card)  
                                        lastpos2=position2
                                        
                                        print_positions(position1, position2, position3, position4)
                                        print(board2)
                                        print("^")
                                        print('|')
                                        print("START HERE")
                                        print('Player 2 has drawn', card)
                                        c+=1
                                        if position2 == 60:
                                            print("\nPlayer 2 wins!")
                                            return
                                        break
                                except ValueError:
                                    print('Invalid Input please type again') 
                                    continue   


                                
                        elif c%4==2:
                            while True:
                                try:
                                    choice=input("Player 3 would you like to [d]raw or [q]uit:")
                                    if choice not in ('d','q'):
                                        raise ValueError
                                    if choice=='q':
                                        return
                                    else:
                                        card=cards()
                                        position3=find_next_position(board1, lastpos3, card)  
                                        lastpos3=position3
                                        
                                        print_positions(position1, position2, position3, position4)
                                        print(board2)
                                        print("^")
                                        print('|')
                                        print("START HERE")
                                        print('Player 3 has drawn', card)
                                        c+=1
                                        if position3 == 60:
                                            print("\nPlayer 3 wins!")
                                            return
                                        break
                                except ValueError:
                                    print('Invalid Input please type again') 
                                    continue   

                            
                            
                        elif c%4==3:
                            card=cards()
                            position4=find_next_position(board1, lastpos4, card)  
                            lastpos4=position4
                            print_positions(position1, position2, position3, position4)
                            print(board2)
                            print("^")
                            print('|')
                            print("START HERE")

                            print('Player 4(Computer) has drawn', card)
                            c+=1
                            if position4==60:
                                print("\nPlayer 4(Computer) wins!")
                                return
                            
            if players==4:
                while True:
                        if c%4==0:
                            while True:
                                try:
                                    choice=input("Player 1 would you like to [d]raw or [q]uit:")
                                    if choice not in ('d','q'):
                                        raise ValueError
                                    if choice=='q':
                                        return
                                    else:
                                        card=cards()
                                        position1=find_next_position(board1, lastpos1, card)  
                                        lastpos1=position1
                                        
                                        print_positions(position1, position2, position3, position4)
                                        print(board2)
                                        print("^")
                                        print('|')
                                        print("START HERE")
                                        print('Player 1 has drawn', card)
                                        c+=1
                                        if position1 == 60:
                                            print("\nPlayer 1 wins!")
                                            return
                                        break
                                except ValueError:
                                    print('Invalid Input please type again') 
                                    continue   
                                

                            
                        elif c%4==1:
                            while True:
                                try:
                                    choice=input("Player 2 would you like to [d]raw or [q]uit:")
                                    if choice not in ('d','q'):
                                        raise ValueError
                                    if choice=='q':
                                        return
                                    else:
                                        card=cards()
                                        position2=find_next_position(board1, lastpos2, card)  
                                        lastpos2=position2
                                        
                                        print_positions(position1, position2, position3, position4)
                                        print(board2)
                                        print("^")
                                        print('|')
                                        print("START HERE")
                                        print('Player 2 has drawn', card)
                                        c+=1
                                        if position2 == 60:
                                            print("\nPlayer 2 wins!")
                                            return
                                        break
                                except ValueError:
                                    print('Invalid Input please type again') 
                                    continue   
                                


                                
                        elif c%4==2:
                            while True:
                                try:
                                    choice=input("Player 3 would you like to [d]raw or [q]uit:")
                                    if choice not in ('d','q'):
                                        raise ValueError
                                    if choice=='q':
                                        return
                                    else:
                                        card=cards()
                                        position3=find_next_position(board1, lastpos3, card)  
                                        lastpos3=position3
                                        
                                        print_positions(position1, position2, position3, position4)
                                        print(board2)
                                        print("^")
                                        print('|')
                                        print("START HERE")
                                        print('Player 3 has drawn', card)
                                        c+=1
                                        if position3 == 60:
                                            print("\nPlayer 3 wins!")
                                            return
                                        break
                                except ValueError:
                                    print('Invalid Input please type again') 
                                    continue   
                                
                            
                            
                        elif c%4==3:
                            while True:
                                try:
                                    choice=input("Player 4 would you like to [d]raw or [q]uit:")
                                    if choice not in ('d','q'):
                                        raise ValueError
                                    if choice=='q':
                                        return
                                    else:
                                        card=cards()
                                        position4=find_next_position(board1, lastpos4, card)  
                                        lastpos4=position4
                                        
                                        print_positions(position1, position2, position3, position4)
                                        print(board2)
                                        print("^")
                                        print('|')
                                        print("START HERE")
                                        print('Player 4 has drawn', card)
                                        c+=1
                                        if position4 == 60:
                                            print("\nPlayer 4 wins!")
                                            return
                                        break
                                except ValueError:
                                    print('Invalid Input please type again') 
                                    continue   
                        
        except ValueError:
            print("Wrong input - Please Try again\n")
            continue

    
def gameboard():
    
    board1=" R P G B V O P Y R B V O G P B O G R Y B G V P R O G B O R V * "
    board=['START','R', 'P', 'G', 'B', 'V', 'O', 'P', 'Y', 'R', 'B', 'V', 'O', 'G', 'P', 'B', 'O', 'G', 'R', 'Y', 'B', 'G', 'V', 'P', 'R' ,'O', 'G ','B', 'O', 'R', 'V' ,'*']
    return board

    pass
def cards():
    carddeck=['R','G','Y','O','B','P','V']
    return random.choice(carddeck)

def find_next_position(board, last_pos, card):
   if card == '*':
        star_pos = board.find('*')
        if last_pos == star_pos - 1:
            return star_pos
        return last_pos
   if last_pos == 0:
       pos = board.find(card)
       return pos if pos != -1 else 0
   else:
       pos = board.find(card, last_pos + 1)
       return pos if pos != -1 else last_pos
while True:
    v=input("\nMAIN MENU: [p]lay game, [i]nstructions, or [q]uit?: ")
    
    try:
        if v not in("p","i","q"):
         raise ValueError
        if v=='p':
            playing()
        if v=='i':
            instructions()
        if v=='q':
            print("\nThanks for playing Candy Realm")
            break
    except ValueError:
        print("\nNot a valid input - Type again")
        continue



