#include <stdio.h>
#include <string.h>

int main(void)
{
	char string[51];
	scanf("%s", string);
	int len = strlen(string);
	int i;
	for(i = 0;i<len;i++)
	{
		printf("%X",string[i]);
	}
	return 0;
}
