import random
r1=random.randint(1,6)
r2=random.randint(1,6)
r3=random.randint(1,6)
sumr =r1+r2+r3
HL=input("Hight (h) or Low (l):")
GN=int(input("Guess number(1-->6):"))
if sumr <11 :
  LH ="l" 
else :
  LH = "H"
if HL == LH :
 print(sumr ,"You win !!") 
else :
 print(sumr ,"You Lose !!") 
number = (GN==r1)or(GN==r2)or(GN==r3)
print (r1,r2,r3)
if number == True :
 print ("BONUS!!!!!!!!!!!")
else :
 print ("No Bonus")

 