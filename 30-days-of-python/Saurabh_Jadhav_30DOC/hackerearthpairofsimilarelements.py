#hackerearthpairofsimilarelements
#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/pairs-having-similar-element-eed098aa/
#https://github.com/arifkhan1990/HackerEarth-solution/blob/master/Data%20Structures/Array/C%2B%2B/Pairs%20Having%20Similar%20Elements.cpp
'''
/*
                 ...........................................................
                   Solver      :   Arif Khan
                   Problem     :   Pairs Having Similar Elements
                   Judge       :   HackerEarth
                   Date        :   27/10/19
                   Time        :   1.84665Sec
                   Memory      :   8224KB
                   Difficulty  :   Easy
                 ...........................................................
    */
#include<bits/stdc++.h>
using namespace std;

long long SimilarElementsPairs(vector<int> A, int N)
{
    sort(A.begin(),A.end());
    long long int ans = 0;

    for(int i = 1; i < N; i++) {
        long long int cnt = 1, st = 1;
        while((A[i] == A[i-1]) or (A[i] == A[i-1]+1)){
            st++;
            if(A[i] == A[i-1]) cnt++;
            i++;
        }
        if(st != 1 and st != cnt) ans += (st*(st-1))/2;
    }
    return  ans;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    vector<int> A(N);
    for(int i_A=0; i_A<N; i_A++)
    {
    	cin >> A[i_A];
    }
 
    long long out_;
    out_ = SimilarElementsPairs(A,N);
    cout << out_;
    return 0;
}
'''
def SimilarElementsPairs (A,N):
    # Write your code here
    A=list(A)
    ans=0
    A=sorted(A)
    print(N)
    for i in range(1,N):
        stackofelements=1
        countofsimilar=1
        while( A[i]==A[i-1] or A[i]==A[i-1]+1):
            print(i)
            #if previous element is similar move forward 
            #if next element follows Aj=Ai+1 
            stackofelements+=1
            #increase stack of elements in order to find the elements under while
            #but get the similar elements also 
            if (A[i]==A[i-1]):
                countofsimilar+=1
            i+=1
        #once we have stack of elements and similar elements
        if stackofelements!=1 and stackofelements!=countofsimilar:
            #that is Aj=Ai+1 at least one pair found
            ans+=(stackofelements*(stackofelements-1))//2
    return ans

N = int(input())
A = map(int,input().split())
out_ = SimilarElementsPairs(A,N)
print (out_)