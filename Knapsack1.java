import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

// Class to represent an item in the knapsack
class Item {
    int value, weight;
    double ratio;

    // Constructor
    public Item(int value, int weight) {
        this.value = value;
        this.weight = weight;
        this.ratio = (double) value / weight; // Calculate the value-to-weight ratio
    }
}

public class Knapsack1{

    // Function to perform the fractional knapsack algorithm
    public static double fractionalKnapsack(ArrayList<Item> items, int capacity) {
        // Sort items based on value-to-weight ratio in descending order
        Collections.sort(items, new Comparator<Item>() {
            @Override
            public int compare(Item a, Item b) {
                return Double.compare(b.ratio, a.ratio); // Sorting by ratio in descending order
            }
        });

        double totalValue = 0.0;  // Total value accumulated

        for (Item item : items) {
            if (capacity >= item.weight) {
                // If the knapsack can hold the whole item, take it all
                totalValue += item.value;
                capacity -= item.weight;
            } else {
                // Take the fraction of the item that fits
                totalValue += item.ratio * capacity;
                break;  // No more items can be taken once the knapsack is full
            }
        }

        return totalValue;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input from the user
        System.out.print("Enter the number of items: ");
        int n = sc.nextInt();

        ArrayList<Item> items = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            System.out.print("Enter the value of item " + (i + 1) + ": ");
            int value = sc.nextInt();
            System.out.print("Enter the weight of item " + (i + 1) + ": ");
            int weight = sc.nextInt();
            items.add(new Item(value, weight));
        }

        System.out.print("Enter the maximum capacity of the knapsack: ");
        int capacity = sc.nextInt();

        // Calculate the maximum value that can be carried in the knapsack
        double maxValue = fractionalKnapsack(items, capacity);

        System.out.printf("Maximum value in Knapsack = %.2f\n", maxValue);
    }
}
