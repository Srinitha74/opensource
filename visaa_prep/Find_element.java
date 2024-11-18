import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc =  new Scanner(System.in);
        int a = sc.nextInt();
        int[] arr = new int[a];
        for(int i = 0; i < a ; i++){
            arr[i] = sc.nextInt();
        }
        int b = sc.nextInt();
        int index = searching(arr, b);
        System.out.println(index);
        sc.close();
    }
    public static int searching(int[] arr, int b){
        int l = 0;
        int r = arr.length - 1;
        while(l <= r){
            int m = (l + r) / 2 ;
            if (arr[m] == b){
                return m;
            }
            if (arr[m] < b){
                l = m + 1;
            }
            else{
                r = m - 1;
            }
        }
        return -1;
    }
}
