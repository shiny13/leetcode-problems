using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ContainsDuplicate
{
    public class Solution
    {
        public Solution () { }

        public bool ContainsDuplicate(int[] nums)
        {
            var isDuplicate = false;
            var hashMap = new Dictionary<int, bool>();

            for (int i = 0; i < nums.Length; i++)
            {
                if (hashMap.ContainsKey(nums[i]))
                {
                    isDuplicate = true;
                    break;
                }
                hashMap.Add(nums[i], true);
            }

            return isDuplicate;
        }
    }
}
