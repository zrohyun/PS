class Solution {
public:
    string reverseVowels(string s) {
        int l = 0;
        int r = s.size()-1;
        // cout << l << r;
        while (l < r){
            
            while ((l < r) && !isVowel(s[l])){
                l++;
            }
            while ((l < r) && !isVowel(s[r])){
                r--;
            }
            swap(s[l++],s[r--]);
        }
        return s;
    }

    bool isVowel(char c) {
        return c == 'a' || c == 'i' || c == 'e' || c == 'o' || c == 'u'
            || c == 'A' || c == 'I' || c == 'E' || c == 'O' || c == 'U';
    }

};
