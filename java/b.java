import java.util.ArrayList;

class Main {
  public static void main(String[] args) {
    ArrayList<Integer> input = new ArrayList<>();
    input.add(1);
    input.add(2);
    input.add(3);
    input.add(4);
    input.add(5);
    //DON'T CHANGE THE CODE ABOVE THIS LINE

    //Your homework is to slowly reverse the arraylist and print each step
    //the output should look like this:
    //2 3 4 5 1
    //3 4 5 1 2
    //4 5 1 2 3
    //5 1 2 3 4
    //1 2 3 4 5

    for (int i = 0; i < input.size(); i++) {
      int firstElement = input.get(0);
      input.remove(0); 
      input.add(firstElement); 
      
      //print it out
      for (int j = 0; j < input.size(); j++) {
        System.out.print(input.get(j) + " ");
      }
      System.out.println();
    }
  }
}