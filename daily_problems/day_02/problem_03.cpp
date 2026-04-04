// Day 2 - Problem 3 (C++)
// Topic: OOP + STL + tie-break sorting
//
// Build a small class `StudentTracker`:
// - add_score(name, score)
// - average_score(name) -> double (return -1 if no scores)
// - top_students() -> vector<pair<string, double>>
//
// top_students rules:
// 1) Compute average per student
// 2) Sort by average descending
// 3) Tie-break: name ascending
//
// Sample usage is in main().

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class StudentTracker {
private:
    unordered_map<string, vector<int>> scores;

public:
    void add_score(const string& name, int score) {
        // TODO
    }

    double average_score(const string& name) const {
        // TODO
        return -1;
    }

    vector<pair<string, double>> top_students() const {
        // TODO
        return {};
    }
};

int main() {
    StudentTracker st;
    st.add_score("Aman", 80);
    st.add_score("Aman", 90);
    st.add_score("Bina", 95);
    st.add_score("Bina", 75);
    st.add_score("Chirag", 88);

    cout << "Avg Aman: " << st.average_score("Aman") << "\n";
    cout << "Avg Zed: " << st.average_score("Zed") << "\n";

    auto tops = st.top_students();
    cout << "Ranking:\n";
    for (const auto& p : tops) {
        cout << p.first << " -> " << p.second << "\n";
    }

    return 0;
}