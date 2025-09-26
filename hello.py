yen = int(input('จำนวนเงินเยนต่อ 1 บาท:'))
baht = int(input('จำนวนเงินบาทที่ต้องการแลก:'))
print (str(baht)+"บาท แลกได้ "+str(yen*baht)+"เยน")
print (f'{baht:.2f}บาท แลกได้ {(yen*baht):,.2f}เยน')