import java.util.Scanner;

/** Simple interactive Java input example for AICodingEditor Embedded Console. */
public class HelloInputTest {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Please enter your name: ");
            System.out.flush();
            String name = scanner.nextLine();
            System.out.println(name + " hello! Nice to meet you.");
        }
    }
}
