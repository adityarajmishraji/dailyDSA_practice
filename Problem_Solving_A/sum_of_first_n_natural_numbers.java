// Program to find sum of first n natural numbers
// Given a number n, find the sum of the first n natural numbers.

// Examples : 

// Input: n = 3
// Output: 6
// Explanation: Note that 1 + 2 + 3 = 6

// Input  : 5
// Output : 15 
// Explanation : Note that 1 + 2 + 3 + 4 + 5 = 15

// JAVA program to find sum of first
// n natural numbers.


import java.io.*;

class naturalSum{
    static int findSum(int n)
    {
        int sum = 0;
        for (int x = 1; x <= n; x++) 
            sum = sum + x;
        return sum;
    }

    // Driver code
    public static void main(String args[])
    {
        int n = 5;
        System.out.println(findSum(n));
    } 
}

