import java.util.*;

public class Knapsack2 {
    public static int knapsack(int[] values, int[] weights, int capacity,int n){
        int[][] dp = new int[n+1][capacity+1];

        for(int i=0;i<=n;i++){
            for(int w=0;w<=capacity;w++){
                if(i == 0 || w == 0){
                    dp[i][w] = 0;
                }else if(weights[i-1] <= w){
                    dp[i][w] = Math.max(dp[i-1][w],values[i-1] + dp[i-1][w-weights[i-1]]);
                }else{
                    dp[i][w] = dp[i-1][w];
                }
            }
        }
        return dp[n][capacity];
    }

    public static void main(String args[]){
        int[] values = {2,3,4,5};
        int[] weight = {3,2,5,3};

        System.out.println(knapsack(values,weight , 5, 4));
    }
}
