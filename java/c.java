import java.util.Scanner;

class c {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    int x = input.nextInt();

    int y = calculateY(x); 

    if (y >= 0) {
      System.out.println("POSITIVE");
    } 
    else {
      System.out.println("NEGATIVE");
    
    input.close();
    }

  }

 
  public static int calculateY(int equationX) {
    int equationY = equationX*3 + 5;
    return equationY;
  }
}