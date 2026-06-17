class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs == null || strs.length == 0 ){
            return new ArrayList<>();
        }
        HashMap<String,List<String>> map = new HashMap<>();
        for( String s:strs){
            char[] NewArray = s.toCharArray();
            Arrays.sort(NewArray);
            String original = new String(NewArray);

            if(!map.containsKey(original)){
                map.put(original,new ArrayList<>());
            }
            map.get(original).add(s);
        
        }
        return new ArrayList<>(map.values());
    }
}
