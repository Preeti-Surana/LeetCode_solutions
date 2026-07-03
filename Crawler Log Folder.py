class Solution(object):
    def minOperations(self, logs):
        depth = 0
        for log in logs:
            if log == "../":
                if depth > 0:
                    depth -= 1
            elif log == "./":
                continue
            else:
                depth += 1

        return depth
      
"""
Approach:-
Maintain a variable depth to represent the current folder depth from the main folder.
Traverse each operation in logs:
"../" → Move to the parent folder. Decrease depth only if it is greater than 0.
"./" → Stay in the current folder. Do nothing.
"x/" → Move into a child folder. Increase depth by 1.
After processing all operations, depth is the minimum number of operations needed to return to the main folder
Time Complexity: O(n)
Space Complexity: O(1)
"""
