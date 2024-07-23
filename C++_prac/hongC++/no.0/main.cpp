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
0.MinGW installer.설치 (MS에 c/c++ for visual studio에 있음) 
   -설치잘됬나 확인 MinGW에 g++ -v 입력 
0.VScode_C/C++ 확장 (Extension) 설치

1.만들고싶은 폴더열어서 -> C++파일생성
2.^+shift+P -> c/c++ Edit configuration(UI) 설정
  - Compiler path: 비쥬얼 스튜디오의 기본 경로로 (C:/msys64/mingw64/bin/g++.exe)
  - IntelliSense mode : (windows-gcc-x64)
    -->이것들이 .vscode하위 json파일에 셋팅값으로 설정되어 있는 것을 볼 수 있다.
3.tasks 설정
  - Run Without Debugging(^+F5) >> C++(GDB/LLDB) >> (C/C++:g++.exe build and debug active file )
4.Launch 설정
  -디버깅하기: ^+shift+P - (C/C++: Add Debug Configuration) >> (C/C++:g++.exe build and debug active file )
*/