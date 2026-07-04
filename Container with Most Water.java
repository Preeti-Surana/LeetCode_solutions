class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length -1;
        int ans = 0;
        while(left<right){
            int hl = height[left];
            int hr = height[right];
            int area;

            if(hl<hr){
                area = hl*(right-left);
                left++;
            }
            else{
                area = hr*(right-left);
                right--;
            }

            if(area>ans){
                ans=area;
            }
        }
        return ans;
    }
}
/* 
Approach:-
- Place one pointer at the left end and the other at the right end of the array.
- Calculate the area using:
  Width = right - left
  Height = min(height[left], height[right])
- Update the maximum area if the current area is larger.
- Move the pointer with the smaller height, because:
  The current area is limited by the shorter line.
  Moving the taller line only decreases the width without increasing the limiting height.
  Moving the shorter line gives a chance to find a taller line and increase the area.
- Repeat until the two pointers meet.

Time Complexity: O(n)
Space  Complexity: O(1)
*/
