#include <stdio.h>
#include <iostream>
#include <string.h>
#include <list>
#include <stack>

using namespace std;

int char_to_idx(char c){
    if('0' <= c && c <= '9')
        return c - '0';
    else if('A' <= c && c <= 'Z')
        return c - 'A' + 10;
    else
        return c - 'a' + 36;
}

char idx_to_char(int index){
    if(index < 10)
        return index + '0';
    else if(index < 36)
        return index - 10 + 'A';
    else
        return index - 36 + 'a';
}

int main (){
    int I;      // num of instances
    int n;      // num of nodes
    bool visited[62];
    bool processed[62];
    cin >> I;
    while(I > 0){
        int m = 0;
        I--;
        for(int i = 0; i < 62; i++){
            visited[i] = false;
            processed[i] = true;
        }
        cin >> n;
        int N = n;
        list<int>* map[62];
        for (int i = 0; i < 62; i++)
            map[i] = new list<int>[n];
        stack<int> st;
        string line;
        cin.ignore();
        bool first = true;
        while(n > 0){
            n--;
            getline(cin, line);
            char c;
            int index = char_to_idx(line.at(0));
            processed[index] = false;
            if(first){
                st.push(index);
                first = false;
            }
            for(int i = 2; i < line.length(); i += 2){
                int k = char_to_idx(line.at(i));
                map[index]->push_front(k);
            }
        }
        
        while(!st.empty()){
            int u = st.top();
            st.pop();
            if(!visited[u]){
                m++;
                cout << idx_to_char(u);
                if(m != N)
                    cout << " ";
                visited[u] = true;
                processed[u] = true;
                while(!map[u]->empty()){
                    st.push(map[u]->front());
                    map[u]->pop_front();
                }
            }
            if(st.empty() && m != N)
                for(int i = 0; i < 62; i++)
                    if(!processed[i]){
                        processed[i] = true;
                        st.push(i);
                        break;
                    }
        }
    }
    return 0;
}

