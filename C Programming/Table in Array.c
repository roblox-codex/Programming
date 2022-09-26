#include<stdio.h>
int main()
{
    int c[3][10],i,j,a[3];
    i=0;
    while(i<3)
    {
        printf("enter a number :- ");
        scanf("%d",&a[i]);
        i++;
    }
        i=0;
        while(i<10)
        {
            j=i+1;
            c[0][i]=a[0]*j;
            c[1][i]=a[1]*j;
            c[2][i]=a[2]*j;
            i++;
        }
        i=0;
        while(i<3)
        {
            j=0;
            while(j<10)
            {
                printf(" %d ",c[i][j]);
                j++;
            }
            printf("\n");
            i++;
        }
        return 0;
}
