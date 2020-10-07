class Solution {
public static int numUniqueEmails(String[] emails) {
    	Set<String> f = new HashSet<>();
    	for(int i=0; i<emails.length; i++) {
    		StringBuilder sb = new StringBuilder();
    		String[] s = emails[i].split("\\@");
    		char[] c = s[0].toCharArray();
    		for(int j=0; j<c.length;j++) {
    			if(c[j] != '.' && c[j] != '+') {
    				sb.append(c[j]);
    			}
    			if(c[j] == '.') {
    				continue;
    			}
    			if(c[j] == '+')break;
    		}
    		sb.append('@').append(s[1]);
    		f.add(sb.toString());
    	}
		return f.size();
    }
    
}
