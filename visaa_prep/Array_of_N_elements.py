import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args)throws IOException {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a=Integer.parseInt(br.readLine());
        List<Integer>res = createArray(a);
        System.out.println(res);  
    }
    public static List<Integer>createArray(int n){
        List<Integer>array = new ArrayList<>();
        for(int i = 0; i < n; i++){
            array.add(i);
        }
        return array;
    }
}
