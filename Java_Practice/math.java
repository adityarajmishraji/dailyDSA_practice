class MathOperations {
    
    int a = 12;
    int b = 5;
    int add = a + b;
    int sub = a - b;
    int multi = a * b;
    int divide = a / b;
    int remainder = a % b;

    void displayResults() {
        System.out.println("Addition of " + a + " and " + b + " is: " + add);
        System.out.println("Subtraction of " + a + " and " + b + " is: " + sub);
        System.out.println("Multiplication of " + a + " and " + b + " is: " + multi);
        System.out.println("Division of " + a + " and " + b + " is: " + divide);
        System.out.println("Remainder of " + a + " and " + b + " is: " + remainder);
    }

    public static void main(String[] args) {
        MathOperations math = new MathOperations();
        math.displayResults();
    }
}


// Changes Made
// Class Renaming: Renamed the class to MathOperations to follow Java naming conventions.

// Display Method: Moved the System.out.println statements to a non-static method (displayResults()).

// Instance Creation: Created an instance of MathOperations in the main method and called the displayResults() method
