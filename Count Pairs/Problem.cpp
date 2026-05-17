#include<iostream>
#include <vector>
using namespace std;
int main(){
          vector <int> arr = {1,5,3,4,2};
          int k = 2;
          int count = 0;
          for(int i = 0; i < arr.size(); i++){
                    for(int j = i + 1; j < arr.size(); j++){
                              if(abs(arr[i]-arr[j])==k){
                                        count++;
                              }
                    }
                    
          }
          cout<< "pair count :" << count << endl;
          return 0;
}