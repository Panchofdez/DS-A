/*Write a function canSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments
the function should return a boolean indicating whether or not it is possible 
to generate the targetSum using numbers from the array
You may use an element of the array as many times as needed
you may assume that all input numbers are nonnegative


This is a decision problem
*/

//m = targetSum , n = number.length
//Brute Force approach => time: O(n^m), space: O(m)

//Using memoization => time O(n*m), space O(m)

const howSum = (targetSum, numbers, table = {}) => {
  if (targetSum === 0) return true;
  if (targetSum < 0) return false;
  if (targetSum in table) return table[targetSum];

  for (let num of numbers) {
    const remainder = targetSum - num;
    if (howSum(remainder, numbers, table)) {
      table[targetSum] = true;
      return table[targetSum];
    }
  }
  table[targetSum] = false;
  return table[targetSum];
};

// console.log(howSum(7, [2, 3])); //true
// console.log(howSum(7, [5, 3, 4, 7])); //true
// console.log(howSum(7, [2, 4])); //false
// console.log(howSum(8, [2, 3, 5])); //true
// console.log(howSum(300, [7, 14])); //false

//USING TABULATION

const howSum2 = (targetSum, numbers) => {
  const table = Array(targetSum + 1).fill(false);

  table[0] = true;

  for (let i = 0; i <= targetSum; i++) {
    if (table[i] === true) {
      for (let num of numbers) {
        if (i + num <= targetSum) {
          table[i + num] = true;
        }
      }
    }
  }
  return table[targetSum];
};

console.log(howSum2(7, [2, 3])); //true
console.log(howSum2(7, [5, 3, 4])); //true
console.log(howSum2(7, [2, 4])); //false
console.log(howSum2(8, [2, 3, 5])); //true
console.log(howSum2(300, [7, 14])); //false
