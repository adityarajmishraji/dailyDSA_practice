// Second Largest
// Difficulty: EasyAccuracy: 26.72%Submissions: 1.2MPoints: 2Average Time: 15m
// Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

// Note: The second largest element should not be equal to the largest element.

// Examples:

// Input: arr[] = [12, 35, 1, 10, 34, 1]
// Output: 34
// Explanation: The largest element of the array is 35 and the second largest element is 34.
// Input: arr[] = [10, 5, 10]
// Output: 5
// Explanation: The largest element of the array is 10 and the second largest element is 5.
// Input: arr[] = [10, 10, 10]
// Output: -1
// Explanation: The largest element of the array is 10 and the second largest element does not exist.
// Constraints:
// 2 ≤ arr.size() ≤ 105
// 1 ≤ arr[i] ≤ 105



class secondLargest {
    public int getSecondLargest(int[] arr) {
        // code here
        // to find lagrest no. from an array, I prefer to use 
        int first = -1; int second = -1;
        
        for(int num : arr){
            if(num>first){
                second = first;
                first = num;
            }else if(num < first && num > second){
                second = num;
            }
        }return second;
    }
    public void main(String[] args){
        
        int arr1[] = {12, 35, 1, 10 , 34, 1};
        System.out.println(getSecondLargest(arr1));
        
        int arr2[] = {10, 5, 10};
        System.out.println(getSecondLargest(arr2));
        
        int arr3[] = {10, 10, 10};
        System.out.println(getSecondLargest(arr3));
    }
}

// Did you get runtime error?