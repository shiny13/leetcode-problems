// See https://aka.ms/new-console-template for more information
using ContainsDuplicate;

Console.WriteLine("271. Contains Duplicate");
Console.WriteLine("-----------------------------------------");

var sol = new Solution();
bool result;

Console.WriteLine("[1,2,3,1]");
result = sol.ContainsDuplicate(new int[] { 1, 2, 3, 1 });
Console.WriteLine($"result: {result}");

Console.WriteLine("[1,2,3,4]");
result = sol.ContainsDuplicate(new int[] { 1, 2, 3, 4 });
Console.WriteLine($"result: {result}");

Console.WriteLine("[1,1,1,3,3,4,3,2,4,2]");
result = sol.ContainsDuplicate(new int[] { 1, 1, 1, 3, 3, 4, 3, 2, 4, 2 });
Console.WriteLine($"result: {result}");
