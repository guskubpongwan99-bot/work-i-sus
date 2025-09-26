subjects=['OS','DB','DS']
for i in subjects :
    num_score = 0
    for score in range(3) :
        sum = int(input(f"คะแนนวิชา {i} = ครั้งที่{score}:"))
        num_score=num_score+sum
    print(f"คะแนนรวมวิชา {i}={num_score}")