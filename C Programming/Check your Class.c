#include <stdio.h>
int main()
{
  int class;
  printf ("Enter your class:");
  scanf("%d",&class);
  switch (class)
  { case 1:
    printf ("You are in class 1");
    
    if(class<3)
    printf ("You can go to school");
    
    else
    printf ("You are junior");
    break;
    case 5:
    printf ("You are in class 5");
    break;
    default:
    printf ("Enter valid class");
    }
return 0;
}
