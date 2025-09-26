import random
card1=random.randint(1,10)
print("Playercard1 =",(card1))
card2=random.randint(1,10)
print("Playercard2 =",(card2))
print("Player point =",(card1+card2)%10) 
Player_point = (card1+card2)%10
card1=random.randint(1,10)
print("Dealercard1 =",(card1))
card2=random.randint(1,10)
print("Dealercard2 =",(card2))
print("Dealer point =",(card1+card2)%10) 
Dealer_point = (card1+card2)%10
if Dealer_point > Player_point :
   print ("Dealer Win")
elif Dealer_point == Player_point :
   print ("draw")
else :
   print("Player win")