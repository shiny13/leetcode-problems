using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BestTimeToBuySellStock
{
    public class Solution
    {
        public Solution() { }

        public int MaxProfit(int[] prices)
        {
            var profit = 0;
            var difference = 0;
            for (int i = 0; i < prices.Length; i++)
            {
                if (i + 1 == prices.Length)
                    break;
                difference = prices[i+1] - prices[i];
                if (difference > 0)
                {
                    if (difference > profit)
                        profit = difference;
                }
                else
                {
                    difference = 0;
                }
            }

            return profit;
        }
    }
}
