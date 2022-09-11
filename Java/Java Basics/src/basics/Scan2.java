package basics;

import java.util.Scanner;

public class Scan2 {

	public static void main(String[] args) {
		  Scanner scanner = new Scanner( System.in );
		  
		  System.out.println("첫번째 숫자");
		  
		  int a = 5;
		  
		  String b = scanner.next();
		  
		  System.out.println(a + b);
		  
		  System.out.println("두번째 숫자");
		  
		  int c = scanner.nextInt();
		  
		  System.out.println( a + c );
	}

}
