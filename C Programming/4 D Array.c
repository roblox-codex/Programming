#include<stdio.h>
int main()
{
  int a[4];
  for (int b=0; b<=3; b++)
    {
      printf("enter no[%d]:- ",b);
      scanf("%d",&a[b]);
    }
  for (int b=3; b>=0; b--)
    {
      printf("%d",a[b]);
    }
  return 0;
}
