#include <stdio.h>

int main(void)
{
	int n;
	scanf("%d",&n);
	int i=0;
	char string[51][51];
	char same[51];
	
	for(i = 0;i<n;i++)
	{
		scanf("%s", &string[i]);
	}
	int j = 0;
	int index = 0;
	
	for(i = 1;i<n;i++)
	{
		for(j = 0;j<strlen(string[0]);j++)
		{
			if(string[0][j] == string[i][j])
			{
				same[j] = string[0][j];
			}
			else
			{
				if(i == 1)index = j;
				else 
				{
					if(index>j) index = j;
					}	break;
			}
		}
	}
	for(i = 0;i<index;i++)printf("%c",same[i]);
	for(i = 0;i<strlen(string[0])-index;i++)printf("?");
	
	return 0;
}
