#include <stdio.h>
int main(void)
{
	int n;
	scanf("%d",&n);
	int i;
	for(i = 0;i<n;i++)
	{
		int option_n;
		int sum,price_s;
		
		scanf("%d",&price_s);
		
		sum = price_s;
		
		scanf("%d", &option_n);
		
		if(option_n == 0)
		{
			printf("%d\n", sum);
			continue;
		}
		
		int j;
		for(j = 0;j<option_n;j++)
		{
			int howmany, option_price;
			scanf("%d %d",&howmany,&option_price);
			sum += howmany*option_price;	
		}
		printf("%d\n",sum);
		
	}
	
	return 0;
}
