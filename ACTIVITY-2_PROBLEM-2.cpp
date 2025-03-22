#include<iostream>
using namespace std;

int sumRecursion(int N) 
{
    if(N == 0)
        return 0;
    else
        return N + sumRecursion(N - 1);
}

int main() 
{
    int N;
    cout << "ENTER THE VALUE OF N--> ";
    cin >> N;

    //-------- using loop 
    int sum = 0; 
    for (int i = 1; i <= N; ++i) 
    { 
        sum += i; 
    } 
    cout << "SUM USING LOOP--> " << sum << endl; 

    //------------ using equation 4
    int sum1 = N * (N + 1) / 2; 
    cout << "SUM USING EQUATION--> " << sum1 << endl;
    
    int sum2 = sumRecursion(N);

    cout << "SUM USING RECURSION--> " << sum2 << endl;
    return 0;
}
