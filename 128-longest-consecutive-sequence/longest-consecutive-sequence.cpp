class Solution {
public:
    int longestConsecutive(vector<int>& a) { int n = a.size();
    sort(a.begin(),a.end());
    if(n==0) return 0;
    if(n==1) return 1;

    int count = 1; int maxm = 1;
    for(int i = 1; i < n; i++){
    if(a[i]==a[i-1]) continue;    
    if(a[i] == a[i-1]+1) { count++; maxm= max(maxm,count);}
    else {maxm= max(maxm,count); count = 1;}
    }
return maxm;
}
};