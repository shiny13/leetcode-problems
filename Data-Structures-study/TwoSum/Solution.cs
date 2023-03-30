using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TwoSum
{
    public class Solution
    {
        public Solution() { }

        public int[] TwoSum(int[] nums, int target)
        {
            var hasMap = new Dictionary<int, int>();
            var result = new int[2];

            for (int i = 0; i < nums.Length; i++)
            {
                var difference = target - nums[i];
                if (hasMap.ContainsKey(difference))
                {
                    result[0] = hasMap[difference];
                    result[1] = i;
                    break;
                }
                hasMap.Add(nums[i], i);
            }

            return result;
        }
    }
}
