#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<string> msg {"Hello World!"};

    for (const string& word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
}

/*
1.확장 (Extension) 설치
2.C/c++ Edit configuration 설정
3.task 설정
4.Launch 설정
*/