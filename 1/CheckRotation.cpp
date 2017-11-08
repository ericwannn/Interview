#include <iostream>
#include <string>

class Rotation {
public:
    bool chkRotation(string A, int lena, string B, int lenb) {
        // write code here
        if(lena != lenb)
            return false;
        string str1 = A + A;
        if(str1.find(B) != string::npos)
            {return true;}
        else{
            return false;
        }
    }
};