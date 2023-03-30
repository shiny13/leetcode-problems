// See https://aka.ms/new-console-template for more information
using MaximumSubarray;

Console.WriteLine("53. Maximum Subarray");
Console.WriteLine("--------------------------------------");

var sol = new Solution();

Console.WriteLine("[-2,1,-3,4,-1,2,1,-5,4]");
Console.WriteLine($"Output: {sol.MaxSubArray(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 })}");

Console.WriteLine("[1]");
Console.WriteLine($"Output: {sol.MaxSubArray(new int[] { 1 })}");

Console.WriteLine("[5,4,-1,7,8]");
Console.WriteLine($"Output: {sol.MaxSubArray(new int[] { 5, 4, -1, 7, 8 })}");
