class Solution {

    public String encode(List<String> strs) {
        String out = new String();
        for (String str: strs){
            int length=str.length();
            out= out+Integer.toString(length)+"#"+str;
        }
        System.out.println(out);
        return out;
    }

    public List<String> decode(String str) {
        List<String> output= new ArrayList<>();
        String temp="";
        int i=0;
        while (i<str.length()){
            int j=i;
            while (str.charAt(j)!='#') {
                j++;
            }
            int length= Integer.parseInt(str.substring(i,j));
            j++;
            output.add(str.substring(j,j+length));
            i=j+length;
            
        }
        return output;
    }
}
