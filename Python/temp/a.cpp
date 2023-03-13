#include <iostream>
#include <cmath>
#include <vector>
#include <set>
using namespace std;

bool is_Prime(int n)
 {

   int square_root = sqrt(n); // use math.h
   int toggle = 1;
   for(int i = 2; i <= square_root; i++)
   {
     if(n%i==0)
     { 
        toggle = 0;
        break;
     }
   }

   if(toggle)
     return true;
   else
     return false;

 } 

int main() {
	
	int n;
	cin >> n;
    set<int> S;
    vector<int> v;
	
	for (int i=2;i<pow(10,n);i++){
		if (is_Prime(i)){
            S.insert(i);
		}
	}
    // for (set<int>::iterator it = S.begin(); it != S.end(); it++) {
	//     cout << *it << " ";
    // }
    // for(auto it = S.begin(); it != S.end(); it++)
    // {
    //     cout << *it << endl;
    // }
        

	for (int i=pow(10, n-1); i<pow(10,n);i++){
        
        int temp = i;
        bool flag = true;
        while (temp > 0){
            std::set<int>::iterator it=S.find(temp);
            // cout << i << " ";
            if (it != S.end()){
                temp = (int)temp/10;
                
            }else{
                flag=false;
                break;
            }
        }
        if (flag){
            v.push_back(i);
        }
	}
    for(auto it = v.begin(); it != v.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
	
	return 0;
}

