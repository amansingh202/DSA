class Solution:
    def JobScheduling(self, Jobs):
        #your code goes here
        Jobs.sort(key = lambda x:x[2], reverse = True)

        max_deadline = max(job[1] for job in Jobs)

        slots = [False]*(max_deadline+1)

        count, total_profit = 0,0

        for job in Jobs:
            job_id, deadline, profit = job

            for t in range(deadline, 0, -1):

                if not slots[t]:
                    slots[t] = True
                    count += 1
                    total_profit += profit
                    break

        return count, total_profit
    
Jobs = [ [1, 2, 100] , [2, 1, 19] , [3, 2, 27] , [4, 1, 25] , [5, 1, 15] ]

obj = Solution()

print(obj.JobScheduling(Jobs))