# Best of 5 five Coin Toss
# 1st Get Random lib
import random

# 2nd Define a function for coin toss
def coin_toss():
    
    # Set up a variable for our decision process
    flip = random.randint(0,1)
    
    # For the following results do that
    if flip == 0:
        
        # Insert any name between the ''
        print('Linux')    
    else:
        print('Unix')

# 3rd Program Logic
# Loop Controller
x=0    

# While loop to throw the coin 'n' times.
# For n=5
while x < 5:
    # Execute the function
    coin_toss()
    
    # Loop counter, in here it could be at begining or at end of the loop
    x+=1