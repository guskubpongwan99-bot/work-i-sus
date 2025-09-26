members=[]
while True :
    mem=input("กรุณาลงชื่อ เพื่อเล่นเกม หรือ exit เพื่อออกจากโปรแกรม:").strip()
    if mem == 'eexit' :
        break
    elif mem in members :
        print("เริ่มเล่นเกมกันเถอะ😁")
    else :
        print(f"ไม่พบชื่อ '{mem}' กรูณาลงทะเบียนก่อน")
        new_mem=''
        print("-----------ส่วนการลงทะเบียน----------")
        while new_mem != 'end' :
            new_mem = input("ชื่อผู้ที่ต้องการลงทะเบียน หรือ end เพื่อจบการลงทะเบียน :").strip()
            if new_mem in members:
                print(f"!!!! ลงทะเบียนไม่ได้ {new_mem} ซ้ำ")
            else:
                members.append(new_mem)
        members.remove("end")
        print(members)
print("เสียใจจริงๆที่คุณเลิกเล่น อย่าลทมกลับมาหากันใหม่นะ")