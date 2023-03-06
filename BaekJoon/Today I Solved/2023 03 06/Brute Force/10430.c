#include <stdio.h>
void calulator(int A,int B,int C){
    int ans1=(A+B)%C;
    int ans2=((A%C)+(B%C))%C;
    int ans3=(A*B)%C;
    int ans4=((A%C)*(B%C))%C;
    printf("%d\n",ans1);
    printf("%d\n",ans2);
    printf("%d\n",ans3);
    printf("%d\n",ans4);
  }
