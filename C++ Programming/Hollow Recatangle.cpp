#include<iostream>
using namespace std;
int main()
{
  int row,col;
  cout<<"enter no of row : ";
  cin>>row;
  cout<<"enter no of col : ";
  cin>>col;
  for(int i=1;i<=row;i++)//rows
 {
   for(int j=1;j<=col;j++)//cols
     {
       if (i==1 || i==row || j==1 || j==col)
       {
         cout<<"**";
       }
       else
       { cout<<"  "; }
     }
    cout<<endl;
  } 
  return 0;
}
