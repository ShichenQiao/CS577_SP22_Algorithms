#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

int main (){
    int n;
    string s;
    cin >> n;
    getline(cin, s);
    for (int i = 0; i < n; i++) {
        getline(cin, s);
        cout << "Hello, " << s << "!\n";
    }

    return 0;
}

