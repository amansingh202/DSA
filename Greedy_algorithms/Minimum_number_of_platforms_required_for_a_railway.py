class Solution:
    def findPlatform(self, Arrival, Departure):
        #your code goes here

        n = len(Arrival)

        Arrival.sort()
        Departure.sort()

        i, j = 1, 0

        platform_needed = 1
        max_platform = 1

        while i < n and j < n:
            if Arrival[i] < Departure[0]:
                platform_needed += 1
                i += 1
            else:
                platform_needed -= 1
                j += 1

            max_platform = max(max_platform, platform_needed)

        return max_platform
            
    
Arrival = [900, 1100, 1235] 
Departure = [1000, 1200, 1240]

obj = Solution()

print(obj.findPlatform(Arrival, Departure))