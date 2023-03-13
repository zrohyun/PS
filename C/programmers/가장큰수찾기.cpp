#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> array) {
    vector<int> answer;
    int max = 0;
    int idx = 0;
    
    for(int i=0;i<array.size();i++){
        if (array[i] > max){
            max = array[i];
            idx = i;
        }
    }
    answer.push_back(max);
    answer.push_back(idx);
    
    
    return answer;
}

// using namespace std;

// vector<int> solution(vector<int> array) {
//     vector<int> answer;
//     auto t = max_element(array.begin(), array.end());
//     answer.push_back(*t);
//     answer.push_back(distance(array.begin(),t));
//     return answer;
// }