#include<stdio.h>
int main()
{
    int no1,no2 ,no3;
    printf("Enter the no1 :- ");
    scanf("%d",&no1);
    printf("Enter the no2 :- ");
    scanf("%d",&no2);
    printf("Enter the no3 :- ");
    scanf("%d",&no3);
    if (no1>no2)
    {
        if(no1>no3)
        { printf("no1 is bigger"); }
        else if (no1==no3)
        { printf("no1 and no3 are bigger"); }
         else  
        { printf("no3 is bigger"); }
    }
    else if(no2>no1)
    {
        if(no2>no3)
        {  printf("no2 is bigger"); }
          else if (no2 ==no3)
        { printf("no2 and no3 are bigger"); }
         else  
        { printf("no3 is bigger"); }
    }
    else
    {
        if(no1==no2 && no2==no3)
        { printf("All the numbers are equal"); }
        else if(no3>no2)
        { printf("no3 is bigger"); }
        else
        { printf("no1 and no2 are bigger"); }
    }    
    return 0;
}
