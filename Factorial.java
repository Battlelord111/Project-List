import java.util.*;
public class Factorial

{
    public static void main(String[] args)
    {
        int i = 0;
        while (i>=0)
        {
         Scanner input = new Scanner(System.in);
         System.out.println("Enter your factorial, enter a negative to exit.");
         i = input.nextInt();
         if (i < 0)
         break;

         System.out.println("Factorial of " + i + " using recursion is " + factorial(i));
         System.out.println();
        }
    }

    public static int factorial(int i)
    {
     if(i == 0)  // base case
     return 1;


     else //recursive case
     return i * factorial(i-1);
    }
}