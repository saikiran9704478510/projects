'''
1 for snake
-1 for water
and 0 for gun 

'''
import random

youstr = input("Enter your choice : ")
youDict = {"s": 1, "w": -1, "g": 0}
you =  youDict[youstr]
computer = random.choice(list(youDict.values()))

key = next((k for k, v in youDict.items() if v == computer), None)
print (f"computer's choice : {key}")

'''if(key  == youstr):
    print("it's a draw !!!")

elif(computer ==-1 and you ==1): 
    print("You win!")

elif(computer ==-1 and you ==0): 
    print("You Lose!")

elif(computer ==1 and you ==-1): 
    print("You lose!")

elif(computer ==1 and you ==0): 
    print("You Win!")

elif(computer ==0 and you ==-1): 
    print("You Lose!")

elif(computer ==0 and you ==1): 
    print("You Lose!")
'''

if ((computer - you) == -1 or (computer - you) == 2) :
    print("You Lose!")
elif ((computer - you) == -2 or (computer - you) == 1): 
    print("You Win!")
elif(key  == youstr):
    print("it's a draw !!!")  
else : 
    print("something went wrong")