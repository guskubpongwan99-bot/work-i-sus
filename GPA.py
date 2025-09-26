subjects=['OS','DB','DS']
sumPoint = 0 
sumcredit = 0
for GPA in subjects :
     credit=int(input("หน่วยกิต ="))
     grade=float(input(f"{GPA} ได้เกรด ="))
     Point = grade*credit
     sumPoint += Point
     sumcredit += credit
     GPA = sumPoint / sumcredit
print(f"GPA ={GPA:,.2f}")