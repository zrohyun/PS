#include <stdio.h>
#include <string.h>

int main(void)
{
	char a[12];
	
	scanf("%s",a);
	if(strcmp(a,"사.우.나") == 0)printf("사랑과 우정을 나누자\n"); 
	else if(strcmp(a,"오.징.어") == 0)printf("오래도록 징그럽게 어울리자\n"); 
	else if(strcmp(a,"사.이.다") == 0)printf("사랑하자 이 세상 다 바쳐\n"); 
	else if(strcmp(a,"나.가.자") == 0)printf("나라, 가정, 자신의 발전을 위하여\n");
	else if(strcmp(a,"재.개.발") == 0)printf("재미있고 개성있게 발전적으로 살자\n"); 
	else if(strcmp(a,"우.아.미") == 0)printf("우아하고 아름다운 미래를 위하여\n"); 
	else if(strcmp(a,"이.기.자") == 0)printf("이런 기회를 자주 만들자\n"); 
	else if(strcmp(a,"청.바.지") == 0)printf("청춘은 바로 지금부터\n");  
	return 0;
}
