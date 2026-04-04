// Baseline Test - C++
// File: baseline_cpp.cpp
// Goal: evaluate STL, classes, and problem-solving style.
//
// Instructions:
// 1) Solve all TODOs.
// 2) Keep total time <= 90 minutes.
// 3) Use C++17 style.

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <queue>
#include <algorithm>
using namespace std;

// Task 1: Return top-k frequent numbers.
vector<int> top_k_frequent(const vector<int>& arr, int k) {
    // TODO
    return {};
}

// Task 2: Basic class design
// Make a class MotorController with:
// - private int speed
// - set_speed(int s): clamp to [0, 100]
// - get_speed() const
// - stop(): sets speed=0
class MotorController {
    // TODO
};

// Task 3: String parsing
// Parse "temp=36.5;hum=45.2" and print key-value pairs.
void parse_packet(const string& packet) {
    // TODO
}

int main() {
    vector<int> arr = {1,1,1,2,2,3,3,3,4,5};
    int k = 2;

    auto ans = top_k_frequent(arr, k);
    cout << "Task 1: ";
    for (int x : ans) cout << x << " ";
    cout << "\n";

    MotorController m;
    m.set_speed(120);
    cout << "Task 2: " << m.get_speed() << "\n";
    m.stop();
    cout << "Task 2 (after stop): " << m.get_speed() << "\n";

    cout << "Task 3:\n";
    parse_packet("temp=36.5;hum=45.2");

    return 0;
}