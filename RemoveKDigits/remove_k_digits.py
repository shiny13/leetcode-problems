import sys

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        number_to_remove = k

        for current_element in num:
            while number_to_remove and stack and stack[-1] > current_element:
                stack.pop()
                number_to_remove = number_to_remove - 1
            stack.append(current_element)
        answer = "".join(stack[0:len(num)-k]).lstrip("0")

        if len(answer):
            return answer
        else:
            return "0"

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    sol = Solution()
    print(sol.removeKdigits(str(data[0]), data[1]))
