#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2 ) {
    vector<string> answer;
    
    for(int i = 0; i<n; i++){
        int a = arr1[i] | arr2[i];
        string ans;
        for(int j=0; j<n; j++){
            if (a & 1) ans = "#" + ans;
            else ans = ' ' + ans;
            a = a >>1;
        }
        answer.push_back(ans);
    }
    return answer;
}

int main(){
    // solution();
    
    std::cout << "test\n";
    return 0;
}