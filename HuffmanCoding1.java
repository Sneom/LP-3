import java.util.*;

class Node{
    char ch;
    int freq;
    Node left,right;
    String huff = "";

    Node(char ch, int freq){
        this.ch = ch;
        this.freq = freq;
        this.left = null;
        this.right = null;
    }
}


public class HuffmanCoding1 {
    public static void printNodes(Node node, String val){
        String newVal = node.huff;

        if(node.left != null){
            printNodes(node.left,newVal);
        }
        if(node.right  != null){
            printNodes(node.right, newVal);
        }

        if(node.left== null || node.right == null){
            System.out.println(node.ch + "-> " + newVal);
        }
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        ArrayList<Node> nodes = new ArrayList<>();

        System.out.println("Enter number of Characters : ");
        int numchars = sc.nextInt();

        for(int i=0;i<numchars;i++){
            System.out.println("Enter Characters : ");
            char ch = sc.next().charAt(0);
            System.out.println("Enter frequence of " + ch + " : ");
            int freq = sc.next().charAt(0);

            nodes.add(new Node(ch,freq));
        }

        while(nodes.size() > 1){
            Collections.sort(nodes,new Comparator<Node>(){
                @Override
                public int compare(Node a, Node b) {
                    return a.freq - b.freq;
                }
            });

            Node left = nodes.get(0);
            Node right = nodes.get(1);

            left.huff = "0";
            right.huff = "1";

            Node newNode = new Node('-', left.freq + right.freq);
            newNode.left = left;
            newNode.right = right;

            nodes.remove(left);
            nodes.remove(right);

            nodes.add(newNode);
        }
        printNodes(nodes.get(0), "");

        sc.close();
    }
}
