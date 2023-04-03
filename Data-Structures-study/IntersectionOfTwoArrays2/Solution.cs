using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IntersectionOfTwoArrays2
{
    public class Solution
    {
        public int[] Intersect(int[] nums1, int[] nums2)
        {
            var firstHashMap = new Dictionary<int, int>();
            var secondHashMap = new Dictionary<int, int>();
            var intersection = new List<int>();

            foreach (var i in nums1)
            {
                if (firstHashMap.ContainsKey(i))
                {
                    firstHashMap[i] += 1;
                }
                else
                {
                    firstHashMap.Add(i, 1);
                }
            }

            foreach (var i in nums2)
            {
                if (secondHashMap.ContainsKey(i))
                {
                    secondHashMap[i] += 1;
                }
                else
                {
                    secondHashMap.Add(i, 1);
                }
            }

            foreach (var node in firstHashMap)
            {
                if (secondHashMap.ContainsKey(node.Key))
                {
                    var count = 0;
                    if (node.Value == secondHashMap[node.Key])
                    {
                        count = node.Value;
                    }
                    else
                    {
                        count = (node.Value > secondHashMap[node.Key]) ? secondHashMap[node.Key] : node.Value;
                    }
                    
                    for (int i = 0; i < count; i++)
                    {
                        intersection.Add(node.Key);
                    }
                    firstHashMap.Remove(node.Key);
                    secondHashMap.Remove(node.Key);
                }
            }

            intersection.Sort();
            return intersection.ToArray();
        }
    }
}
