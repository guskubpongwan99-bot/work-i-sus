#include <iostream>
#include <cstdlib>

using namespace std;

class Player {
public:
    virtual int choose() {
        int c;
        while(true){
            cout << "Choose: 1 = Rock, 2 = Scissors, 3 = Paper : ";
            if(!(cin >> c)){
                cout << "Error: Numbers only (1-3)\n";
                cin.clear();
                cin.ignore(1000,'\n');
                continue;
            }
            if(c < 1 || c > 3) continue;
            return c;
        }
    }
};

class Bot : public Player {
public:
    int choose() override {
        return rand() % 3 + 1;
    }
};

class Game {
private:
    Player *player;
    Bot *bot;
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

    for (int i = 1; i <= 3; i++) {
        game.playRound(i);
    }
    game.showResult();

    return 0;
}