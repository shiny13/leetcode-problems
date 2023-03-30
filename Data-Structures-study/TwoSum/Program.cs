// See https://aka.ms/new-console-template for more information
using TwoSum;

Console.WriteLine("1. Two Sum");
Console.WriteLine("--------------------------------");

var sol = new Solution();

Console.WriteLine("nums: [2,7,11,15] | target: 9");
var result = sol.TwoSum(new int[] { 2, 7, 11, 15 }, 9);
var resultStr = string.Join(", ", result);
Console.WriteLine($"Output: [{resultStr}]");

Console.WriteLine("nums: [3,2,4] | target: 6");
result = sol.TwoSum(new int[] { 3, 2, 4 }, 6);
resultStr = string.Join(", ", result);
Console.WriteLine($"Output: [{string.Join(", ", sol.TwoSum(new int[] { 3, 2, 4 }, 6))}]");

Console.WriteLine("nums: [3,3] | target: 6");
result = sol.TwoSum(new int[] { 3, 3 }, 6);
resultStr = string.Join(", ", result);
Console.WriteLine($"Output: [{string.Join(", ", sol.TwoSum(new int[] { 3, 3 }, 6))}]");
