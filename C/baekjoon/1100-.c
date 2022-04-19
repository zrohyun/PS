#include <stdio.h>
int main(void)
{
	int i,j;
	char chess;
	int count = 0;
	int c = 0&1; 
	for(i = 0;i<8;i++)
	{
		for(j = 0;j<8;j++)
		{
			scanf("%c",&chess);
			if(chess == 'F' && ((i^j)&1)== 0 )count++;
		}
		getchar();
	}
	printf("%d",count);
	return 0;	
}

