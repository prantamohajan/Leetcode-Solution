#include<iostream>
#include<vector>
using namespace std;

int main (){
          vector<int> arr = {2,3,2,4,4};
          int result = 0;
                    for(int num : arr){
                              result ^=num;
                    }
                    cout<<"single number: "<< result << endl;
                    return 0;
}
