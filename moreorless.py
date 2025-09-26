import random
num = random.randint(1,10)
ans = 0 
count = 0
lose = False
corret = 0 
while lose == False and count != 3 :
    count += 1
    newnum = random.randint(1,10)
    ans = input(f"[{count}]เลขต่อไป มาก(m) หรือน้อย(l) กว่า{num}:")
    if newnum >= num and ans == "m":
        print (f"{newnum} >= {num} คุณตอบถูก")
        corret +=1
    elif newnum <= num and ans == "l" :
        print (f"{newnum} <= {num} คุณตอบถูก")
        corret +=1
    else : 
        print(f"{newnum} = {num} คุณตอบ ผิด")
        lose = True
    num=newnum
if lose == True :
    print(f"คุณตอบถูก{corret}รอบ--คุณแพ้")
else: 
    print(f"ตอบถูก {corret} รอบ---คุณชนะ")