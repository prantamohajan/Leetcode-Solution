class Solution {
public:
    string reformatDate(string date) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        stringstream ss(date);
        string dayStr, monthStr, year;
        ss >> dayStr >> monthStr >> year;

        string months[] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};
        
        string mon = "";
        for (int i = 0; i < 12; i++) {
            if (months[i] == monthStr) {
                
                if (i + 1 < 10) mon = "0" + to_string(i + 1);
                else mon = to_string(i + 1);
                break;
            }
        }
        string da = "";
        if (isdigit(dayStr[1])) {
            da = dayStr.substr(0, 2); 
        } else {
            da = "0" + dayStr.substr(0, 1); 
        }

        
        return year + "-" + mon + "-" + da;
    }
};