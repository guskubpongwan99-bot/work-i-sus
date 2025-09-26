import random
weapons=['ค้อน','กรรไกร','กระดาษ']

def show_up(wp):
    wp_text=  weapons[wp-1]
    return wp_text

def check_win(p1,p2,w1,w2):
    if w1 == w2 :
        winner="เสมอ"
    elif w1==1 and w2==2 :
        winner=p1
    elif w1==2 and w2==3 :
        winner=p1
    elif w1==3 and w2==1 :
        winner=p1
    else:
        winner=p2
    return winner

def play_game():
    wp=int(input("'1=ค้อน','2=กรรไกร','3=กระดาษ':"))
    wm=random.randint (1,3)
    TheWiner=check_win("Player","Machine",wp,wm)
    print(f"Player =-->{show_up(wp)}")
    print(f"Machine --->{show_up(wm)}")
    print(f"The winner is !! ---> {TheWiner}")
def start():
    while True:
        play=input("play?? (y/n)")
        if play == 'y':
            play_game()
        else :
            print("Thank you for join our games.")
            break
        