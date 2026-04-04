// Day 1 - Problem 2 (C++)
// Task:
// Read n integers and output top k frequent elements.
// Use unordered_map + priority_queue.
//
// Sample input:
// n = 12
// arr = 1 1 1 2 2 3 3 3 3 4 5 5
// k = 2
//
// One valid output: 3 1
// (Order between equal frequencies can vary.)

#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    int k;
    cin >> k;

    // TODO:
    // 1) Build frequency map
    // 2) Push (frequency, value) into max-heap
    // 3) Pop k elements and print values

    return 0;
}