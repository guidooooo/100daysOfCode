def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        nums.sort()
        last_n = None
        
        for n in range(len(nums)-1):

            j = n+1
            m = len(nums)-1
            
            if last_n == nums[n]: continue

            # print("Hola")

            last_n = nums[n]

            while j < m:

                sum_nums = nums[j] + nums[m] + nums[n]
                if sum_nums > 0:
                    m -= 1
                elif sum_nums<0:
                    j += 1
                else:
                    new_result = [nums[n], nums[j], nums[m]]
                    if new_result not in result:
                        result.append(new_result) 
                    j += 1
                
        return result

print(threeSum([0,0,0,0]))

