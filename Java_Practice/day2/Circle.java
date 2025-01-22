package Circular;

public class Circle {
    int radius = 8;
    static final double PI = 3.14;

    // Method to display the area of the circle
    void display() {
        double area = PI * radius * radius; // Area formula
        System.out.println("Area of the circle is: " + area);
    }

    public static void main(String[] args) {
        Circle obj = new Circle();
        obj.display();
    }
}
