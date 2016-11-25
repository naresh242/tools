
public class LevenshteinDistance {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(getLevenshteinDistance("naesh","naresh"));
	}

	private static int minimum(int a, int b, int c) {                            
        return Math.min(Math.min(a, b), c);                                      
    }                                                                            
                                                                                 
    public static float getLevenshteinDistance(CharSequence lhs, CharSequence rhs) {      
        int[][] distance = new int[lhs.length() + 1][rhs.length() + 1];        
                                                                                 
        for (int i = 0; i <= lhs.length(); i++)                                 
            distance[i][0] = i;                                                  
        for (int j = 1; j <= rhs.length(); j++)                                 
            distance[0][j] = j;                                                  
                                                                                 
        for (int i = 1; i <= lhs.length(); i++)                                 
            for (int j = 1; j <= rhs.length(); j++)                             
                distance[i][j] = minimum(                                        
                        distance[i - 1][j] + 1,                                  
                        distance[i][j - 1] + 1,                                  
                        distance[i - 1][j - 1] + ((lhs.charAt(i - 1) == rhs.charAt(j - 1)) ? 0 : 1));
                                                                                 
        //return distance[lhs.length()][rhs.length()];     
        int finalDistance=distance[lhs.length()][rhs.length()];
        
        return getPercentagecloseness(finalDistance,lhs.length(),rhs.length());
        
    }   
    
    private static float getPercentagecloseness(int noOfMismatch,int length1,int length2){
    	
    	float result;
    	
    	result=(float)noOfMismatch*100/(Math.max((float)length1,(float)length2));
    	
    	return result;
    }
}
