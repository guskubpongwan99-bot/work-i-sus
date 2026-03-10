#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <ctime>
#include <string>

using namespace std;

// โครงสร้างเก็บข้อมูล Ranking
struct RankEntry { string name; int score; };

// --- 1. Class แม่ (Base Class) ---
class Player {
public:
    string name;
    Player(string n) : name(n) {}
    
    virtual int choose(); // Method สำหรับ Scope Resolution (1)
    
    // Overloading Method (1): แบบไม่รับค่า (ใช้รับ Input จาก User)
    int getChoice() { return choose(); }
    // Overloading Method (2): แบบรับค่า (ใช้สำหรับบังคับค่าให้ Bot)
    int getChoice(int fixed) { return fixed; }
};

// Scope Resolution ครั้งที่ 1
int Player::choose() {
    int c;
    cout << "Choose [1:Rock, 2:Scissors, 3:Paper, 0:Exit]: ";
    while (!(cin >> c) || c < 0 || c > 3) {
        cout << "Invalid input! Try again: ";
        cin.clear();
        cin.ignore(1000, '\n');
    }
    return c;
}

// --- 2. Class Bot (Inheritance ครั้งที่ 1) ---
class Bot : public Player {
public:
    Bot(string n) : Player(n) {}
    int choose() override { return rand() % 3 + 1; }
};

// --- 3. Class HardBot (Inheritance ครั้งที่ 2) ---
class HardBot : public Bot {
    int lastMove = 0;
public:
    HardBot(string n) : Bot(n) {}
    void remember(int m) { lastMove = m; }
    int choose() override {
        if (lastMove == 0) return rand() % 3 + 1;
        // Logic แก้ทาง: ถ้าเราออกค้อน(1) -> Bot ออกกระดาษ(3), ถ้าเราออกกรรไกร(2) -> Bot ออกค้อน(1)
        return (lastMove == 1) ? 3 : (lastMove == 2) ? 1 : 2;
    }
};

// --- 4. Class Rank (จัดการไฟล์) ---
class Rank {
    vector<RankEntry> list;
public:
    void load() {
        list.clear();
        ifstream f("rank.txt");
        RankEntry e;
        while (f >> e.name >> e.score) list.push_back(e);
        f.close();
    }

    void save(); // Method สำหรับ Scope Resolution (2)

    void add(string n, int s) {
        bool found = false;
        for (auto &e : list) {
            if (e.name == n) {
                if (s > e.score) e.score = s;
                found = true; break;
            }
        }
        if (!found) list.push_back({n, s});
    }

    void show() {
        cout << "\n========== RANKING ==========\n";
        if (list.empty()) cout << "No records yet.\n";
        for (int i = 0; i < list.size(); i++) {
            cout << i + 1 << ". " << list[i].name << " : " << list[i].score << " pts\n";
        }
        cout << "=============================\n";
    }
};

// Scope Resolution ครั้งที่ 2
void Rank::save() {
    sort(list.begin(), list.end(), [](RankEntry a, RankEntry b) {
        return a.score > b.score;
    });
    ofstream f("rank.txt");
    for (auto &e : list) f << e.name << " " << e.score << "\n";
    f.close();
}

int main() {
    srand(time(0));
    Rank rank;
    rank.load();
    
    char menu;
    string names[] = {"Exit", "Rock", "Scissors", "Paper"};

    while (true) {
        cout << "\n--- MAIN MENU ---\n1. Normal Mode\n2. Hard Mode\n3. Show Rank\n4. Exit\nSelect: ";
        cin >> menu;

        if (menu == '4') break;
        if (menu == '3') { rank.show(); continue; }
        if (menu != '1' && menu != '2') continue;

        string pName;
        cout << "Enter Player Name: ";
        cin >> pName;

        Player p(pName);
        Bot* b;
        if (menu == '2') b = new HardBot("HardBot");
        else b = new Bot("NormalBot");

        int pScore = 0, bScore = 0;

        for (int r = 1; r <= 3; r++) {
            cout << "\nRound " << r << "!" << endl;
            int pc = p.getChoice(); // เรียกใช้ Overloading 1
            if (pc == 0) break;

            // เรียกใช้ Overloading 2: รอบแรก Bot จะออกค้อนเสมอ (เลข 1) เพื่อโชว์การใช้ Method
            int bc = (r == 1) ? b->getChoice(1) : b->choose();

            cout << ">> " << pName << ": " << names[pc] << " vs Bot: " << names[bc] << endl;

            if (pc == bc) cout << "Result: Draw!" << endl;
            else if ((pc == 1 && bc == 2) || (pc == 2 && bc == 3) || (pc == 3 && bc == 1)) {
                cout << "Result: You Win!" << endl;
                pScore++;
            } else {
                cout << "Result: Bot Win!" << endl;
                bScore++;
            }

            if (menu == '2') ((HardBot*)b)->remember(pc);
        }

        cout << "\nFinal Score -> You: " << pScore << " | Bot: " << bScore << endl;
        rank.add(pName, pScore);
        rank.save();
        delete b;
    }

    cout << "Goodbye!" << endl;
    return 0;
}
