/*
Write a function howSum(targetSum, numbers) that takes is a targetSum and an array of numbers as arguments
The function should return an array containing any combination of elements that add up to exactly the targetSum. 
If there is no combination that adds up to the targetSum, then return null

If there multiple combinations possible you may return a single one


this is a combinatoric problem
*/

//m = targetSum , n = number.length
//Brute Force approach => time: O(n^m * m), space: O(m)

//Using memoization => time O(n*m*m), space O(m*m) we will have m keys and each key has a value of an array of m length at worst

const howSum = (targetSum, numbers, table = {}) => {
  if (targetSum === 0) return [];
  if (targetSum < 0) return null;
  if (targetSum in table) return table[targetSum];

  for (let num of numbers) {
    const remainder = targetSum - num;
    const ans = howSum(remainder, numbers, table);
    if (ans != null) {
      //we multiply by m to the amount of recursive calls because for every call we have to copy all the elements of array which at most is m in length
      table[targetSum] = [...ans, num];
      return table[targetSum];
    }
  }

  table[targetSum] = null;
  return table[targetSum];
};

// console.log(howSum(7, [2, 3])); // [3,2,2]
// console.log(howSum(7, [5, 3, 4, 7])); //[4,3]
// console.log(howSum(7, [2, 4])); //null
// console.log(howSum(8, [2, 3, 5])); //[2,2,2,2]
// console.log(howSum(300, [7, 14])); //null

//Using tabulation

const howSum2 = (targetSum, numbers) => {
  const table = Array(targetSum + 1).fill(null);

  table[0] = [];

  for (let i = 0; i <= targetSum; i++) {
    if (table[i] !== null) {
      for (let num of numbers) {
        table[i + num] = [...table[i], num];
      }
    }
  }
  return table[targetSum];
};

console.log(howSum2(7, [2, 3])); // [3,2,2]
console.log(howSum2(7, [5, 3, 4, 7])); //[4,3]
console.log(howSum2(7, [2, 4])); //null
console.log(howSum2(8, [2, 3, 5])); //[2,2,2,2]
console.log(howSum2(300, [7, 14])); //null
