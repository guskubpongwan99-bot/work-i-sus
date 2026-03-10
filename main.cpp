#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

class Player {
public:
    virtual int choose() {
        string input;
        while(true){
            cout << "Choose: 1 = Rock, 2 = Scissors, 3 = Paper : ";
            
            // ใช้ getline แทน cin >> เพื่ออ่านทั้งบรรทัด (รวมช่องว่าง)
            getline(cin, input);

            // ตรวจสอบว่าในบรรทัดนั้นมีแค่ตัวอักษรเดียว และเป็น 1, 2, 3 เท่านั้น
            if(input.length() == 1 && (input[0] == '1' || input[0] == '2' || input[0] == '3')) {
                return input[0] - '0';
            }

            // ถ้าใส่ "1 2 3" หรือ "1  " หรือ "p 1" มันจะติด Error ทันที
            cout << "Error: Invalid input! Please enter only 1, 2, or 3.\n";
        }
    }
};

// ... ส่วนที่เหลือ (Bot และ Game) คงเดิมเหมือนโค้ดก่อนหน้า ...

class Bot : public Player {
public:
    int choose() override { return rand() % 3 + 1; }
};

class Game {
private:
    Player *player; Bot *bot;
    int scorePlayer = 0, scoreBot = 0;
    string convertChoice(int c) {
        if(c==1) return "Rock";
        if(c==2) return "Scissors";
        return "Paper";
    }
public:
    Game(Player *p, Bot *b) : player(p), bot(b) {}
    void playRound(int round) {
        cout << "\n----- Round " << round << " -----\n";
        int p = player->choose();
        int b = bot->choose();
        cout << "You chose: " << convertChoice(p) << " | Bot chose: " << convertChoice(b) << endl;
        if (p == b) cout << "Draw!\n";
        else if ((p == 1 && b == 2) || (p == 2 && b == 3) || (p == 3 && b == 1)) {
            cout << "You win this round!\n";
            scorePlayer++;
        } else {
            cout << "Bot wins this round!\n";
            scoreBot++;
        }
    }
    void showResult() {
        cout << "\n===== FINAL RESULT =====\n";
        cout << "Player: " << scorePlayer << " - Bot: " << scoreBot << endl;
        if (scorePlayer > scoreBot) cout << "You win the game!\n";
        else if (scoreBot > scorePlayer) cout << "Bot wins the game!\n";
        else cout << "Game Draw!\n";
    }
};

int main() {
    Player p;
    Bot b;
    Game game(&p, &b);
    for (int i = 1; i <= 3; i++) game.playRound(i);
    game.showResult();
    return 0;
}
