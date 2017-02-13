public class CompareArrays
{
	public static void main(String[] args)
	{
		int [] alpha = {0, 1, 2, 43, 48, 59, 60, 70, 88, 90, 1000};
		int [] bravo = {0, 1, 2, 43, 48, 59, 60, 70, 88, 90, 1000};
		boolean equalFlag = true; // Set the flag to true
		// Test if the flag should be false
			if ( alpha.length != bravo.length )
			equalFlag = false;
			
			else
				for ( int i = 0; i < alpha.length; i++ )
				if ( alpha[i] != bravo[i] )
				equalFlag = false;
				// Print the result
				if ( equalFlag )
					System.out.println("alpha and bravo are equal");	
					else
					System.out.println("alpha and bravo are NOT equal");
	} // end of method main
} // end of class CompareArrays