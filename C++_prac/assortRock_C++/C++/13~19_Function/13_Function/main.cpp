#include <stdio.h>

int Factorial(int); //main�Լ��ȿ� �۵��ϱ� ���� �ӽ� ����
int Factorial_Recursion(int);




int Add(int a, int b)
{
	return 0;
}






int main() //���α׷� �� ��ä. return ������ ���α׷� �� . �׳� ������ �ʱ� ���� for () , while() ���� �ݺ����� ���
{
	int iData =Add(100,200) ;


	//13.�Լ�(1)
	//�ݺ���
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

	//14.����Ű
	//������ ���� �ּ�     : ctrl + k,c
	//������ ���� �ּ� ����: ctrl + k,u
	//Ư�� �κи� ���ε巹��: Alt Drag
	//�����				:F5
	//���� �ߴ������� �ڵ� ����

	//�ߴ��� ���� �� ����   :F9
	//����� ��, ��������    :F10
	//����� ��, ��������(�Լ�����): F11
	//����� ��, ����� �����ϱ� :Shift + F5

	//15.printf,scanf ���������
	//printf
	printf("%d\n",10);
	printf("%f\n", 3.14f);
	//scanf
	int j = 0;
	scanf_s("%d", &j ); //_s�� ����������

	//16.�Լ�(2)
	//�Լ��� ����ϴ� �޸� ������ 
	//���� �޸� ����_C++�ڵ� ¥�鼭 
	//�������� ���� ���̰� ������ �������� ��� �޸� ������ ����غ���
	//�ڵ念�� <-> �޸𸮿��� (�ٸ�) 
	//�ڵ念���� ����� ����ü��
	//�޸𸮿����� ���󼼰��� �����غ���

	//17.�Լ�(3)
	int iValue = Factorial(4);
	iValue = Factorial(10);
	printf("%d", iValue);
	
	//19.����Լ�(2)
	iValue = Factorial_Recursion(10);
	printf("%d",iValue);

	//19.����Լ�_�Ǻ���ġ
	iValue = Fibonacci(7);
	iValue = Fibonacci_Recursion(8); 


	return 0;
}



int Factorial(int cou)
{
	//17.�Լ�(3)
	//Factorial 
	// !8 (8���丮��)

	int iValue = 1;
	for (int j = 0; j < cou - 1; ++j)
	{
		iValue *= (j + 2);
	}

	//18.����Լ�(1) 
	//�߸� �� ���
	//Factorial(10); 
	//��� �ڱ� �ڽ��� ���� ���� �׾ƿ÷��� 
	// �׾ƿø���׾ƿø��� �ڱ��ڽ� ��ӺҸ���~~ 
	// ����ȵǰ�
	// -> ���ÿ����÷ο� �߻�
	 


	return iValue;
}


	//19.����Լ�(2)
	//Ż�� ������ ������ָ� ����
	//������, ������ ���� 
	//but ������ ���� �ʴ�.������� �̷� �� ����.
	// Recursion=����Լ�
int Factorial_Recursion(int inum)
{
	if (1 == inum)
	{
		return 1;
	}

	return inum * Factorial_Recursion(inum - 1);
}


	//19.����Լ�(2)
	// �Ǻ���ġ����_�׳� ����
	// 1 1 2 3 5 8 13 21 34 55 .....
	// ���̿� ������ �׸��鼭 �غ���
	//�������� Ʈ������ �Ҷ� ����Լ� ������
	// _���� ���̿� ���°� �� ����
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

	//�Ǻ���ġ ����_����Լ� ����
	// �Ǻ���ġ ���� ��û���� ������
	// _���� ���̿� ���°� �� ����
int Fibonacci_Recursion(int inum)
{
	if (1 == inum || 2 == inum)
	{
		return 1;
	}
	return Fibonacci_Recursion(inum - 1) + Fibonacci_Recursion(inum - 2);
}