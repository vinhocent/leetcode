class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> hash;

        for (int i = 0 ; i < nums.size() ; i++){
            if (hash.find(nums[i]) != hash.end()){ // exists already
                return {i, hash[nums[i]]};
            } else{
                hash[target-nums[i]] = i;
            }
        }
        return {};
    }
};