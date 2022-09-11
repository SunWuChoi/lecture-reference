package basics;

import java.util.Scanner;

public class Scan {

	public static void main(String[] args) {
		Scanner scanner = new Scanner( System.in );
		
	    System.out.println("입력해주세요.");
	  
	    String testA = scanner.next();
//	    String testA = scanner.nextLine();
//	    int testA = scanner.nextInt();
	    
	    System.out.println( testA );
	}

}
