class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:

        mod = 10 ** 9 + 7

        return (self.sumSubarrayMax(nums) - self.sumSubarrayMins(nums)) 


    def sumSubarrayMins(self, arr: list[int]) -> int:

        n = len(arr)

        mod = 10**9 + 7

    #previous smaller element code
        pse = [-1]*n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                pse[i] = stack[-1]
            else:
                pse[i] = -1

            stack.append(i)

    #next smaller element code

        nse = [n]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]
            else:
                nse[i] = n

            stack.append(i)

    # code for the problem

        total = 0

        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i

            total = (total + (left * right * arr[i])) 

        return total
    
    def sumSubarrayMax(self, arr: list[int]) -> int:

        n = len(arr)

        total = 0

        mod = 10 ** 9 + 7

        #next greater element code
        nge = [n]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()

            if stack:
                nge[i] = stack[-1]
            else:
                nge[i] = n

            stack.append(i)


        #previous greater element code

        pge = [-1]*n
        stack = []

        for i in range(n):
            while stack and arr[i] > arr[stack[-1]]:
                stack.pop()

            if stack:
                pge[i] = stack[-1]
            else:
                pge[i] = -1

            stack.append(i)


        for i in range(n):
            left = i - pge[i]
            right = nge[i] - i

            total = (total + (left * right * arr[i])) 

        return total

        

        
    

obj = Solution()

arr = [4,-2,-3,4,1]

print(obj.subArrayRanges(arr))

        