import java.util.Stack;
class Solution {
    public String removeStars(String s) {
        Stack<Character> stack = new Stack<>();
        for (char ch : s.toCharArray()) {
            if (ch == '*') {
                stack.pop();
            } else {
                stack.push(ch);
            }
        }

        StringBuilder ans = new StringBuilder();

        for (char ch : stack) {
            ans.append(ch);
        }
        return ans.toString();
    }
}

"""
Intuition:-
Every * removes the closest character to its left.
The closest character to the left is always the last character that has not been removed yet.
This "last added, first removed" behavior is exactly what a Stack (LIFO - Last In, First Out) is designed for.

Algoritm:-
- Create an empty stack.
- Traverse the string from left to right.
- For each character:
If it is a normal character, push it onto the stack.
If it is *, pop the top character from the stack (this removes the closest character on the left).
- After processing the entire string, the stack contains only the remaining characters.
- Join all characters in the stack to form the final string and return it.

Time Complexity: O(n)
Space Complexity : O(n)

"""
