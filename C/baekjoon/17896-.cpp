#include <iostream>
#include <regex>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    string input;
    
    cin >> input;
    smatch m;

    if(regex_search(input,m, regex("meow"))){
        cout << 0;
    }else if(regex_search(input,m,regex("(meo([a-z])*|me[.]w|m[.]ow|[a-z]*eow)"))){
        cout << 1;
    }else if(regex_search(input,m, regex("(m[a-z]{0,2}w|eo|me|ow)"))){
        cout << 2;
    }else if( regex_search(input,m,regex("(m|e|w|o)"))){
        cout <<3;
    }else{
        cout << 4;
    }
        // std::cout << 1;
        // }
    
}