import sys 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        s_idx, t_idx = 0, 0

        while s_idx < s_len and t_idx < t_len and s_idx <= t_idx:
            if s[s_idx] == t[t_idx]:
                print("{} {} {}".format(s_idx, s[s_idx], t[t_idx]))
                s_idx += 1
            t_idx += 1
        print("s index: {} t index: {}".format(s_idx, t_idx))

        if s_idx == s_len:
            return True

        return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()

    sol = Solution()
    print(sol.isSubsequence(data[0], data[1]))
