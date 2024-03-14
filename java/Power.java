import java.util.*;
public class Power
{
    public static void main(String[] args)
    {
        int b =0;
        int p =0;
        while(b>=0)
        {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter bases and then powers:");
        b = input.nextInt();
        p = input.nextInt();
        if(b<1||p<1)
        break;
        System.out.println(b + " to the power " + p +  ": = "  +power(b,p) + "\n");
        }
    }
    public static int power(int base, int pow)
    {
     if(pow==0) //base case
     return 1;
     else // recursive case
     return base * power(base, pow-1);
    }
}