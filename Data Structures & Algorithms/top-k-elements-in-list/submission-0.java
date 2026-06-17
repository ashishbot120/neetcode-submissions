class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> freq = new HashMap<>();
        for ( int n:nums){
            freq.put(n,freq.getOrDefault(n,0)+1);
        }
        List<Integer>[] bucket = new List[nums.length+1];
        for(int i=0;i<bucket.length;i++){
            bucket[i]=new ArrayList<>();
        }
        for (int key : freq.keySet()) {
            int frequency = freq.get(key);
            bucket[frequency].add(key);
        }
        int[] result = new int[k];
        int resultIndex = 0;
        for (int i = bucket.length - 1; i >= 0 && resultIndex < k; i--) {
            for (int num : bucket[i]) {
                result[resultIndex] = num;
                resultIndex++;
                if (resultIndex == k) {
                    break;
                }
            }
        }
        return result;
    }
}
