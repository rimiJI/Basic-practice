#include <stdio.h>

int Factorial(int); //main함수안에 작동하기 위한 임시 선언
int Factorial_Recursion(int);




int Add(int a, int b)
{
	return 0;
}






int main() //프로그램 그 잡채. return 만나면 프로그램 끝 . 그냥 끝내지 않기 위해 for () , while() 같이 반복문을 사용
{
	int iData =Add(100,200) ;


	//13.함수(1)
	//반복문
	for ( int i=0 ;i<3 ;++i )
	{
		printf("i\n");

		if (i % 2 == 1)
		{
			continue;
		}
		if (i == 2)
		{
			break;
		}
	}

	int i = 0;
	while (i < 3 )
	{
		printf("i\n");
		++i;
	}

	//14.단축키
	//지장한 구문 주석     : ctrl + k,c
	//지정한 구문 주석 해제: ctrl + k,u
	//특정 부분만 세로드레그: Alt Drag
	//디버깅				:F5
	//다음 중단점까지 코드 실행

	//중단점 생성 및 해제   :F9
	//디버깅 중, 구문수행    :F10
	//디버깅 중, 구문수행(함수진입): F11
	//디버깅 중, 디버깅 종료하기 :Shift + F5

	//15.printf,scanf 문자입출력
	//printf
	printf("%d\n",10);
	printf("%f\n", 3.14f);
	//scanf
	int j = 0;
	scanf_s("%d", &j ); //_s는 세이프버전

	//16.함수(2)
	//함수가 사용하는 메모리 영역을 
	//스택 메모리 영역_C++코드 짜면서 
	//스텍으로 위로 쌓이고 수행후 없어지고 라고 메모리 영역을 상상해보자
	//코드영역 <-> 메모리영역 (다름) 
	//코드영역은 명령의 집합체고
	//메모리영역을 가상세계라고 생각해보자

	//17.함수(3)
	int iValue = Factorial(4);
	iValue = Factorial(10);
	printf("%d", iValue);
	
	//19.재귀함수(2)
	iValue = Factorial_Recursion(10);
	printf("%d",iValue);

	//19.재귀함수_피보나치
	iValue = Fibonacci(7);
	iValue = Fibonacci_Recursion(8); 


	return 0;
}



int Factorial(int cou)
{
	//17.함수(3)
	//Factorial 
	// !8 (8펙토리얼)

	int iValue = 1;
	for (int j = 0; j < cou - 1; ++j)
	{
		iValue *= (j + 2);
	}

	//18.재귀함수(1) 
	//잘못 쓴 경우
	//Factorial(10); 
	//계속 자기 자신을 위로 스택 쌓아올려서 
	// 쌓아올리고쌓아올리고 자기자신 계속불르고~~ 
	// 종료안되고
	// -> 스택오버플로우 발생
	 


	return iValue;
}


	//19.재귀함수(2)
	//탈출 조건을 만들어주면 괜춘
	//가독성, 구현의 용이 
	//but 성능이 좋지 않다.해제비용 이런 것 땜시.
	// Recursion=재귀함수
int Factorial_Recursion(int inum)
{
	if (1 == inum)
	{
		return 1;
	}

	return inum * Factorial_Recursion(inum - 1);
}


	//19.재귀함수(2)
	// 피보나치수열_그냥 버전
	// 1 1 2 3 5 8 13 21 34 55 .....
	// 종이에 펜으로 그리면서 해보기
	//계층구조 트리구조 할때 재귀함수 용이함
	// _차라리 종이에 적는게 더 빠름
int Fibonacci(int inum)
{
	if (1 == inum || 2 == inum)
	{
		return 1;
	}

	int iprev1 = 1;
	int iprev2 = 1;
	int iValue = 0;

	for (int i = 0; i < inum - 2; ++i)
	{
		iValue = iprev1 + iprev2;
		iprev1 = iprev2;
		iprev2 = iValue;
	}
	return iValue;
}

	//피보나치 수열_재귀함수 버전
	// 피보나치 수열 엄청나게 느리다
	// _차라리 종이에 적는게 더 빠름
int Fibonacci_Recursion(int inum)
{
	if (1 == inum || 2 == inum)
	{
		return 1;
	}
	return Fibonacci_Recursion(inum - 1) + Fibonacci_Recursion(inum - 2);
}