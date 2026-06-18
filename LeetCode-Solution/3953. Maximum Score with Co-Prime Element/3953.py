class Solution(object):
    def maxScore(self, nums, maxVal):
        M = maxVal
        for x in nums:
            if x > M:
                M = x
                
        cnt = [0] * (M + 1)
        for x in nums:
            cnt[x] += 1

        C = [0] * (M + 1)
        for i in range(1, M + 1):
            s = 0
            for j in range(i, M + 1, i):
                s += cnt[j]
            C[i] = s

        mu = [0] * (M + 1)
        mu[1] = 1
        for i in range(1, M + 1):
            m_i = mu[i]
            if m_i:
                for j in range(2 * i, M + 1, i):
                    mu[j] -= m_i

        divs = [[] for _ in range(M + 1)]
        for i in range(1, M + 1):
            if mu[i]:
                for j in range(i, M + 1, i):
                    divs[j].append(i)

        ans = -10**9
        n = len(nums)
        
        visited = [False] * (M + 1)
        for x in nums:
            visited[x] = True
        for v in range(1, maxVal + 1):
            visited[v] = True

        for V in range(1, M + 1):
            if not visited[V]:
                continue
                
            coprime_cnt = 0
            for d in divs[V]:
                coprime_cnt += mu[d] * C[d]
            N_V = n - coprime_cnt

            if cnt[V]:
                penalty = N_V - 1 if V > 1 else 0
                score = V - penalty
                if score > ans:
                    ans = score
            elif V <= maxVal:
                penalty = 1 if N_V < 1 else N_V
                score = V - penalty
                if score > ans:
                    ans = score

        return ans