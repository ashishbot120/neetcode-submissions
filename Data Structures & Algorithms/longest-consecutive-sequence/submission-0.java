class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }

        Set<Integer> numSet = new HashSet<>();
        int longestStreak = 0;
        for( int num : nums ){
            numSet.add(num);
        }

        for( int num : numSet){
            if(!numSet.contains(num - 1)){
                int currentnum = num ;
                int currentStreak = 1;

                while (numSet.contains(currentnum + 1)) {
                    currentnum += 1;
                    currentStreak += 1;
                }
            longestStreak = Math.max(longestStreak,currentStreak);
            }

        
        }
    return longestStreak;
    }
}