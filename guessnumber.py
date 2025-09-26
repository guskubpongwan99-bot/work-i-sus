import random
secret = random.randint(1,10)


guess = 0
count = 0
while guess != secret :
    count +=1
    guess = int (input("เดาตัวเลช 1--->10 :"))
    #ตรวจสอบว่าเราถูกรึเปล่า
    #ถ้ามากไป บอกมากไป
    #ถ้าน้อยไปบอกน้อยไป
    if guess > secret :
        print(f"{guess}มากไป")
    elif guess < secret :
        print(f"{guess}น้อยไป")
    else :
        print(f"{guess}ถูกต้อง")
print(f"ใช้ไปทั้งหมด{count}รอบ:")          