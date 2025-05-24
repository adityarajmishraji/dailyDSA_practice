// Move All Zeroes to End
// Difficulty: EasyAccuracy: 45.51%Submissions: 330K+Points: 2Average Time: 15m
// You are given an array arr[] of non-negative integers. Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.

// Examples:

// Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
// Output: [1, 2, 4, 3, 5, 0, 0, 0]
// Explanation: There are three 0s that are moved to the end.
// Input: arr[] = [10, 20, 30]
// Output: [10, 20, 30]
// Explanation: No change in array as there are no 0s.
// Input: arr[] = [0, 0]
// Output: [0, 0]
// Explanation: No change in array as there are all 0s.
// Constraints:
// 1 ≤ arr.size() ≤ 105
// 0 ≤ arr[i] ≤ 105


// User function Template for Java

class Solution {
    void pushZerosToEnd(int[] arr) {
        // code here
        int n = arr.length;
        int lastNonZeroIndex = 0;
        
        // Move all non-zero elements to the front
        for (int i=0; i < n; i++)
        {
            if(arr[i] != 0)
            {
                arr [lastNonZeroIndex] = arr[i];
                lastNonZeroIndex++;
            }
        }
        // Fill the rest with Zeros
        for(int i = lastNonZeroIndex; i < n; i++)
        {
            arr[i]=0;
        }
    }
    
    // Example use
    public void main(String[] args){
        int[] arr = {1,2,0,4,3,0,5,0};
        pushZerosToEnd(arr);
        for(int num : arr){
            System.out.print(num + " ");
        }
    }
    
}


// Do you know about Error: Main method is not static in class Solution, please define the main method as:
//    public static void main(String[] args). Because once we make it static then it again shows error.