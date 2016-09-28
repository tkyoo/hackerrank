import java.util.*;
class Solution{

	public static void main(String []argh)
	{
		Scanner sc = new Scanner(System.in);

		String result = "false";
		boolean end = false;
		while (sc.hasNext()) {
			String input=sc.next();
			//Complete the code
			Stack<Character> stack = new Stack<Character>();

			for ( int i = 0 ; i < input.length(); i++) {
				char c = input.charAt(i);
				if ( c == '[' || c == '{' || c == '(' ) {
					stack.push(c);
				}

				if( c == ']' ) {
					if ( stack.isEmpty()) {
						end = true;
						break;
					}

					if ( stack.peek() == '[' ) {
						stack.pop();
					} else {
						end = true;
						break;
					}
				}

				if( c == '}' ) {
                    if ( stack.isEmpty()) {
						end = true;
                        break;
                    }

					if ( stack.peek() == '{' ) {
						stack.pop();
					} else {
						end = true;
						break;
					}
				}

				if ( c == ')' ) {
                    if ( stack.isEmpty()) {
						end  = true;
                        break;
                    }

					if ( stack.peek() == '(' ) {
						stack.pop();
					} else {
						end = true;
						break;
					}
				}
			}

			if ( end || !stack.isEmpty()) {
				System.out.println("false");
			} else {
				System.out.println("true");
			}

			end = false;
		}
	}
}

