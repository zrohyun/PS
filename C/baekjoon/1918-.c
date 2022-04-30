#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char string[256];
char Stack[10];
char Pbuff[254];

int Bindex = 0;
int Sindex = 0;
int i,j;

int al(char);
void Pop(void)
{
	if(Sindex == 0) Sindex++;
	Pbuff[Bindex++] = Stack[--Sindex];
	Stack[Sindex--] = '\0';
}
void PushS(int a)
{
	if(Sindex == -1) Sindex++;
	Stack[Sindex++] = string[a];
}
void PushB(int a)
{
	Pbuff[Bindex++] = string[a];
}

int main(void)
{
	scanf("%s",string);

	for(i = 0;i<strlen(string);i++)
	{
		if(al(string[i]) == 0) PushB(i);
		else if(al(string[i]) == 5)
		{
			while(Stack[Sindex] != '(')
			{
				Pop();
			}
			Stack[Sindex] = '\0';
		}
		else
		{
			if(Sindex == 0 || al(string[i]) == 1)
			{
				PushS(i);
				continue;
			}
			for(j = Sindex-1;j>=0;j--)
			{
				if(al(string[i]) <= al(Stack[j]))Pop();	
			}
			PushS(i);
		}
	}
	for(i = strlen(Stack) -1;i>=0;i--)
	{
		Pop();
	}
	for(i = 0;i<strlen(string);i++)
	{
		printf("%c",Pbuff[i]);
	}
	
	return 0;
}
int al(char a)
{
	switch(a)
	{
		case '*': case '/': return 3;
		case '(': return 1;
		case '+': case '-': return 2;
		case '^': return 4;
		case ')': return 5;
		default: return 0;
	}
}

