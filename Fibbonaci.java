import java.util.*;
public class Fibbonaci

{
    public static void main(String[] args)
    {
        int i = 0;
        while(i>=0)
        {
         Scanner input =  new Scanner(System.in);
         System.out.println("Enter up to which Fibbonaci series to print: ");
         i = input.nextInt();
         if(i<0)
         break;
         System.out.println("Fibbonaci numbers up to " + i + " numbers : \n");
         for(int x = 1; x<=i; x++)
         {
          System.out.print(fib(x) + " ");
         }
         System.out.println("\n");
        }
    }
    public static int fib(int i)
    {

     if(i==1)//base case
     return 1;

     else if(i==0)//alternate base case
     return 0;

     else// recursive case
     return  fib(i-1) + fib(i-2);
    }
}
