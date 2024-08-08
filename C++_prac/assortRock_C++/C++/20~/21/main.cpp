#include <stdio.h>

//사용자 정의 자료형
//자료형? 데이터 타입입니다.
//사용자 정의? 기본 언어 자료형말구 내방식대로 만듦,내코드서만 적용
//그게 바로 구조체


//struct:구조체
//struct _TagMyST:구조체 이름
//MYST:typedef을 사용해 다시 정한 이름,C++은 굳이 디파인 안써도됨 이왕이면 써라




typedef struct _tagMyST
{
	int a; //a라는 변수는 없고 int를 지칭하는 단어로 사용
	float f;
}MYST; // 만들어낸 자료형 이름




typedef struct _tagBig
{
	MYST k;//구조체 안에 구조체 가능
	int i;
	float c;
}BIG;

typedef int INT;
//typedef:타입을 재정의 해주는것 eg) typedef int INT;int를INT로 바꿔쓴다




int main()
{
	//21.구조체와 포인터 
	MYST t = {}; //선언, int,float으로 구성되어있음 8바이트
	MYST f = {100,3.14f}; //값을 넣어서 초기화 선언할수도 있음

	int iSize = sizeof(MYST);
	t.a = 10;
	t.f = 10.2312f;

	//typedef int INT;로 인한 결과
	INT a;  

	return 0;
}