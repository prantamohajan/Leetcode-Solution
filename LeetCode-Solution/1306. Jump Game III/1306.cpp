class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        if (n == 0) return false;
        if (arr[start] == 0) return true;
        
        vector<bool> visited(n, false);
        queue<int> q;
        
        q.push(start);
        visited[start] = true;
        
        while (!q.empty()) {
            int i = q.front();
            q.pop();
            
            // Jump forward
            int forward = i + arr[i];
            if (forward < n && !visited[forward]) {
                if (arr[forward] == 0) return true;
                visited[forward] = true;
                q.push(forward);
            }
            
            // Jump backward
            int backward = i - arr[i];
            if (backward >= 0 && !visited[backward]) {
                if (arr[backward] == 0) return true;
                visited[backward] = true;
                q.push(backward);
            }
        }
        
        return false;
    }
};