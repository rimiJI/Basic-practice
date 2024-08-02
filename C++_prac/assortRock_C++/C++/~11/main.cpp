#define HUNGRY 1 //첫번째칸 2의 0승 - 32비트 칸 중에서 오른쪽부터
#define THIRSTY 2 //2번쨰칸 2의 1승
#define TIRED 4 //3번쨰칸 2의 2승

//가독성
// 유지보수

int main()
{
	//자료형: (크기단위, byte) 영어론 Data type
	// 정수형: char(1), short(), int(4) ,long(4), long long(8)
	// 실수형: float(4),double(8)
	
	//여기선 int : 자료형 ,  i: 변수명
	int i = 0;
	
	// (0~255) 공간이 1인 양의 정수만 출력하겠다.
	unsigned char c = 0;  

	c = 0;
	c = 255;
	c = 256; //초과하면 잘려서 안들어감. 디버깅하면 여기에 무슨값들어갔는 지 할 수 있다. 
	c = -1; //정의 외 음수

	//1바이트로 양,음수 둘다표시
	char c1 = 0; //(-128~0~127)
	c1 = -1;
	
	//음의 정수 찾기(2의 보수법)
	//대응되는 양수의 부호를 반전 후, 1을 더한다.

	//정수와 실수는 표현하는 방법이 다르다 -부동소수점 발생
	//실수 표현방식은 정밀도에 의존
	//따라서 double(8) 자료형이 float(4) 보다 더 아래의 소수점까지 정확하게 표현이 가능하다
	int a = 4 + (int)4.0; //눈에 보이지 않지만 형변환이 이뤄진다. 그 과정에서 실수가 발생한다. 

	//정수는 정수끼리, 실수는 실수끼리 연산하되, 두 표현방식의 피 연산자가 연산될 경우 명시적으로 변환하자
	float b = 10.2415f + (float)20;

	//연산자
	//대입연산자 =
	//산술연산자 + - * / %  ++ -- 
	
	//연산자의 우선순위 : 1)산술연산자 - 2)대입연산자
	int d = 10 + 10;
	d += 20; //a = a + 20;

	//실수끼리 나눈건 나머지가 존재하지 않는다. -> 오류뜸... 계속 나눠지니까 실수끼린
	//int data = 0;
	//data = 10. / 3.; 
	//data = 10. % 3.;
	//나누기도 실수끼리 안됨

	//그래서 이렇게 표기
	int data = 0;
	data = (int)(10.f / 3.f);

	//실수타입에 f 붙여주면 float 안붙여주면, double
	float f = 10.2516f + (float)20;


	//++,--
	data = 0;
	++data; 
	++data; 
	data = ++data; // data -> 1


	// 논리연산자 
	// // ! (역), &&(and), ||(or)
	//참(true),거짓(False)
	//참: 1로 0이아닌 값.\
	//거짓: 0

	int e = true; //a=1
	int ee = false; //b=0

	bool isT = (bool)100; //True (100을 저장하는 게 아니고  True로 , bool 은 0과1밖에 모르는 바보)

	isT = true;
	isT = !isT; //false

	isT = 100 && 100; //true&&true = true
	isT = 0 && 200; //false &&true = false
	isT = 0 || 200; //true


	//비교연산자
	//== != < <= > >= 
	//참 거짓


	//구문
	//if, else , switch case
	data = 0;
	if (true)
	{
		data = 100;
	}

	if (data == 100)
	{
		data = 200; //실행안됨
	}
	else if (data==200)
	{
		data = ++data;
	}
	else//없어도됨.
	{

	}


	//switch
	switch (20) //(20과 일치하는거까지 앞에서부터 실행)
	{
	case 10:
		//break;
	case 20:
		break;
	default:
		break;
	}

	//얘랑 같이 if 문에 넣으려면
	int iTest = 30;
	switch (iTest)
	{
	case 10:
	case 20:
	case 30:

	default:
		break;
	}
	//위 switch를 if문으로 바꾸려면
	if (iTest == 10 || iTest == 20 || iTest == 30)
	{

	}
	else
	{

	}



	//삼항연산자
	// 질문? A : B 이프엘스를 간단하게 쓰고 싶어서
	iTest == 20 ? iTest = 100 : iTest = 200; // iTest가 20입니까??- 맞으면 :가운데 실행 - 틀리면: 맨오른쪽 실행
	//위에껄  ifelse로 바꾸면
	if (iTest == 20)
	{
		iTest = 100;
	}
	else
	{
		iTest = 200;
	}

	//비트연산자 _자주까먹음
	//쉬프트 <<, >>  10진수에서 한칸 증가한다- *10이 증가한다.. 2진수에서 한칸증가한다 -2배가 증가한다.
	unsigned char byte = 1;
	byte = byte << 1; // 한칸 증가해서 2배가 된다. 
	//이건 byte<<=3 과 같다
	byte <<= 2; //2^n 배수 (2의 n승) - 왼쪽으로 민다
	byte >>= 3; //2^n으로  나눈 몫 -오른쪽으로 민다.

	//비트곱(&),합(|),xor(^)  진짜 비트끼리 자릿수대로 연산.비트합은 1+1가 2아니라 1
	//비트에서 반전은 (~) .....!이거랑 같은 개념
	// & 둘다 1인경우 1
	// | 둘중 하나라도 1이면 1
	//xor 같으면 0 다르면1 _좀 청개구리같으네
	// ~ 1은 0으로, 0은 1으로

	//비트연산자 게임에서 많이 사용함. 게임에서 특히
	//전처리 # 이거 할 때 , 지금 맨 위에다 썼는데
	int iStatus = HUNGRY; //맨 위 선언한대로 3이 출력
	
	//int iStatus 는 32비트
	unsigned int Status = 0;

	Status |= TIRED;

	


	return 0;
}