import tkinter as tk
from tkinter import ttk,messagebox,Label
from tkinter.scrolledtext import ScrolledText

# Function Insert ScrollText

# Function Clear ScrollText

# Function แสดงรายละเอียดและการจ่ายเงิน

# Main Program
root = tk.Tk()
root.title("Food Order")
root.geometry('600x400+200+100')

# สร้าง ComboBox
foodlist=['ข้าวขาหมู','ข้าวหมูแดง','ข้าวมันไก่']

# สร้างปุ่มบันทึกรายการอาหาร

# สร้างปุ่มล้างรายการอาหาร

# สร้าง ScrolledText รายการอาหาร

# สร้าง Checkbox รายละเอียด

# สร้าง Radio การจ่ายเงิน

# สร้าง ScrolledText รายละเอียด


# ใส่ข้อความ Line1 Column0
# indexของLineเริ่มจาก 1/Index Column เริ่มจาก 0
# แทรกบรรทัดใหม่ไปเรื่อยๆ



def copyText() :
    # อ่านข้อความเฉพาะส่วนที่เลือก
    thetext=st.selection_get()
    st2.insert('1.0',thetext)
...

def btn1Click():
    st2.insert('1.0',cmbSubj.get()+'\n')

st2=ScrolledText(root, width=30 ,height=10)
st2.place(x=550,y=10)

btn1=ttk.Button(root,text='บันทึกรายการอาหาร',command=btn1Click)
btn1.place(x=200,y=10)


# สร้าง List ข้อมูล
foodlist=['ข้าวขาหมู','ข้าวหมูแดง','ข้าวมันไก่']

# สร้าง Combobox 
cmbSubj=ttk.Combobox(root)

# โยนค่าในList ไปให้ Combobox
cmbSubj['values']=foodlist
cmbSubj.place(x=10,y=10)


def clear() :
    # ลบบรรทัดที่1 ถึงจุดสุดท้าย
    st2.delete('1.0','end')
    st2.focus()
...


btnclear=ttk.Button(root,text='ล้างรายการ',command=clear)
btnclear.place(x=200,y=50)


def chkClicked():
    st.delete('1.0','end')
    thetext=f"{varChk1.get()} {varChk2.get()} {varChk3.get()} {varfree.get()} "
    st.insert('1.0',thetext)
# Checkbox ต้องติดต่อผ่าน Widget variable
varChk1=tk.StringVar()
chk1=ttk.Checkbutton(root,text="รับช้อน",command=chkClicked,variable=varChk1,
                     onvalue='รับช้อน',offvalue="")
chk1.place(x=220,y=250)


varChk2=tk.StringVar()
chk2=ttk.Checkbutton(root,text="รับถุง",command=chkClicked,variable=varChk2,
                     onvalue='รับถุง',offvalue="")
chk2.place(x=100,y=250)

varChk3=tk.StringVar()
chk3=ttk.Checkbutton(root,text="อุ่น",command=chkClicked,variable=varChk3,
                     onvalue='อุ่น',offvalue="")
chk3.place(x=10,y=250)


varfree=tk.StringVar()
rdo1=ttk.Radiobutton(root,text='เงินสด',value='เงินสด',variable=varfree,command=chkClicked)
rdo1.place(x=10,y=350)


rdo2=ttk.Radiobutton(root,text='เงินโอน',value='เงินโอน',variable=varfree,command=chkClicked)
rdo2.place(x=100,y=350)

st=ScrolledText(root, width=20 ,height=5)
st.place(x=550,y=200)





tk.mainloop()

