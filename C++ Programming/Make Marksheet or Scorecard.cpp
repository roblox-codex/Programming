#include <iostream>
using namespace std;
int main()
{
  char str[100];
  double m1,m2,m3,m4,m5,m6,sum,percentage,avg;
  
  cout<<"Enter your name: ";
  cin>>str;
  //marks
  cout<<"Enter marks of Physics:";
  cin>>m1;
  cout<<"Enter marks of Eng. Electrical:";
  cin>>m2;
  cout<<"Enter marks of Communication Skill:";
  cin>>m3;
  cout<<"Enter marks of Eng.Mathematics:";
  cin>>m4;
  cout<<"Enter marks of Eng.Graphics:";
  cin>>m5;
  cout<<"Enter marks of Computer:";
  cin>>m6;
  //details
  sum=m1+m2+m3+m4+m5+m6;
  avg=(m1+m2+m3+m4+m5+m6)/6;
  percentage=(sum*100)/600;
  //outputs
  cout<<"Your name is: "<<str<<endl;
  cout<<"Your total marks "<<sum<<endl;
  cout<<"Your avg marks are "<<avg<<endl;
  cout<<"Your percentage is= "<<percentage<<endl;
  
  return 0;
}
