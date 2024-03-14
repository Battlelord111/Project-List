import java.util.*;
public class ReverseString
{
    public static void main(String[] args)
    {
        String s = "";
        while(!(s.equals("exit")))
        {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a string to reverse");
        s = input.nextLine();
        if(s.equals("exit"))
        break;

        System.out.println(reverse(s) + "\n");
        }
    }
    public static String reverse(String str)
    {
     if ((str.length() <= 1)) //base case
           return str;
        else //recursive case
        {
            return (str.charAt(str.length()-1)) + 
            reverse(str.substring(0,str.length()-1));
        }
    }
}