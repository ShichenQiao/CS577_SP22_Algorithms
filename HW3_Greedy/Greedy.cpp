#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

bool sort_by_FF(const vector<int> &v1, const vector<int> &v2)
{
    return v1[1] < v2[1];
}

int main (){
    int I;
    cin >> I;
    while(I > 0){
        I--;
        int n;
        int cnt = 0;
        cin >> n;
        vector< vector<int> > data;
        for(int i = 0; i < n; i++){
            int a, b;
            cin >> a >> b;
            vector<int> temp;
            temp.push_back(a);
            temp.push_back(b);
            data.push_back(temp);
        }
        
        sort(data.begin(), data.end(), sort_by_FF);         // O(NlogN)
        
        while(!data.empty()){
            vector<int> current = data.front();
            data.erase(data.begin());
            cnt++;
            for (int i = data.size() - 1; i >= 0; i--)
                if(data[i][0] < current.back())
                    data.erase(data.begin() + i);
        }
        cout << cnt << endl;
    }
    return 0;
}
