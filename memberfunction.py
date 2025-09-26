import janken

members=[]
def check_name(mem):
    if mem in members:
        return True
    else : 
        return False
def PLAY_GAME(themem):
    print("----ส่วน Play game----")
    print(f"เริ่มเล่นเกมกัน{themem}\n")
    janken.start()

def register():
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
while True :
    mem=input("กรุณาลงชื่อ เพื่อเล่นเกม หรือ exit เพื่อออกจากโปรแกรม:").strip()
    if mem == 'exit' :
        break
    elif check_name(mem):
        PLAY_GAME(mem)
    else :
        print(f"ไม่พบชื่อ '{mem}' กรูณาลงทะเบียนก่อน")
        register()

