#include <stdio.h>

//����� ���� �ڷ���
//�ڷ���? ������ Ÿ���Դϴ�.
//����� ����? �⺻ ��� �ڷ������� ����Ĵ�� ����,���ڵ弭�� ����
//�װ� �ٷ� ����ü


//struct:����ü
//struct _TagMyST:����ü �̸�
//MYST:typedef�� ����� �ٽ� ���� �̸�,C++�� ���� ������ �Ƚᵵ�� �̿��̸� ���




typedef struct _tagMyST
{
	int a; //a��� ������ ���� int�� ��Ī�ϴ� �ܾ�� ���
	float f;
}MYST; // ���� �ڷ��� �̸�




typedef struct _tagBig
{
	MYST k;//����ü �ȿ� ����ü ����
	int i;
	float c;
}BIG;

typedef int INT;
//typedef:Ÿ���� ������ ���ִ°� eg) typedef int INT;int��INT�� �ٲ㾴��




int main()
{
	//21.����ü�� ������ 
	MYST t = {}; //����, int,float���� �����Ǿ����� 8����Ʈ
	MYST f = {100,3.14f}; //���� �־ �ʱ�ȭ �����Ҽ��� ����

	int iSize = sizeof(MYST);
	t.a = 10;
	t.f = 10.2312f;

	//typedef int INT;�� ���� ���
	INT a;  

	return 0;
}