import random
from game_data import data
from art import logo,vs
from replit import clear


score =0
counter=0
game_finished=False

def compare(a,b):
    if int(a['follower_count'])>int(b['follower_count']):
        return "a"
    else:
        return "b"
        
def random_data():
    return random.choice(data)
    
def format_data(account):
    return f"{account['name']}, a {account['description']} from {account['country']}"

    
b=random_data()
print(logo)
while not game_finished:
    a=b
    b=random_data()
    while(a==b):
        b=random_data()

    print(f"Compare A:{format_data(a)}")
    print(vs)
    print(f"Aganist B:{format_data(b)}")
    
    guess=input("Who has more followers? Type 'A' or 'B': ")
    clear()
    print(logo)
    if guess.lower()==compare(a,b):
        score+=1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry you lost, Final score:{score}.")
        game_finished=True
   
    
        
    
    
