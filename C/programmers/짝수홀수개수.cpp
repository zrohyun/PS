// #include <string>
// #include <vector>
// #include <iostream>

// using namespace std;

// vector<int> solution(vector<int> num_list) {
//     vector<int> answer(2,0);
    
//     // for(int x : num_list){
//     //     answer[x & 1]++;
//     // }
    
//     for(int i=0;i<num_list.size();i++){
//         answer[num_list[i] & 1]++;
//     }
    
    
//     return answer;
// }

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer(2,0);
    for(const auto v: num_list)
    {
        answer[v%2]++;
    }
    return answer;
}