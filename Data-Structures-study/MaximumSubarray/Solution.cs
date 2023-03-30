using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MaximumSubarray
{
    public class Solution
    {
        public Solution() { }

        public int MaxSubArray(int[] nums)
        {
            var max_so_far = Int32.MinValue;
            var max_ending_here = 0;

            foreach (int x in nums)
            {
                max_ending_here += x;
                if (max_so_far < max_ending_here)
                {
                    max_so_far = max_ending_here;
                }
                if (max_ending_here < 0)
                {
                    max_ending_here = 0;
                }
            }

            return max_so_far;
        }
    }
}
