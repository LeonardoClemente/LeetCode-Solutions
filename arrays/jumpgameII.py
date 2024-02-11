class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)< 2:
            return 0
 
        goal = len(nums) - 1
        current_max = nums[0]
        previous_max = -1
        n_jumps = 1

        if current_max >= goal:
                return n_jumps 

        for i, distance in enumerate(nums):
            
            # Check if new distance can extend current
            new_distance = i+distance
            if new_distance > current_max:
                 
                # If i is still within previous jump, then modify
                # so we jump from here instead of there
                if i > previous_max:
                    previous_max = current_max
                    n_jumps += 1
                
                current_max = new_distance
            
            if current_max >= goal:
                return n_jumps 
                    
                    
                    





        
        