/*Write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments
Function should return an array containing the shortest combination of numbers that add up to exactly the targetSum
If there is a tie for the shortest combination you may return any one of them

This is an optimization problem


*/

//m = targetSum , n = number.length
//Brute Force approach => time: O(n^m * m), space: O(m*m) because for each stack frame we store an array of m length at worst for shortest

//Using memoization => time O(n*m*m), space O(m*m) we will have m keys and each key has a value of an array of m length at worst

const bestSum = (targetSum, numbers, table = {}) => {
  if (targetSum === 0) return [];
  if (targetSum < 0) return null;
  if (targetSum in table) return table[targetSum];
  let shortest = null;
  for (let num of numbers) {
    const remainder = targetSum - num;
    let result = bestSum(remainder, numbers, table);
    if (result !== null) {
      result = [...result, num];
      if (shortest == null || result.length < shortest.length) {
        shortest = result;
      }
    }
  }
  table[targetSum] = shortest;
  return table[targetSum];
};

// console.log(bestSum(7, [2, 3])); // [3,2,2]
// console.log(bestSum(7, [5, 3, 4, 7])); //[7]
// console.log(bestSum(7, [2, 4])); //null
// console.log(bestSum(8, [2, 3, 5])); //[5,3]
// console.log(bestSum(8, [1, 4, 5])); //[4,4]
// console.log(bestSum(100, [1, 2, 5, 25])); //[25,25,25,25]

//Using tabulation

const bestSum2 = (targetSum, numbers) => {
  const table = Array(targetSum + 1).fill(null);

  table[0] = [];

  for (let i = 0; i <= targetSum; i++) {
    if (table[i] !== null) {
      for (let num of numbers) {
        const newArr = [...table[i], num];
        if (table[i + num] == null || table[i + num].length > newArr.length) {
          table[i + num] = newArr;
        }
      }
    }
  }
  return table[targetSum];
};

console.log(bestSum2(7, [2, 3])); // [3,2,2]
console.log(bestSum2(7, [5, 3, 4, 7])); //[7]
console.log(bestSum2(7, [2, 4])); //null
console.log(bestSum2(8, [2, 3, 5])); //[5,3]
console.log(bestSum2(8, [1, 4, 5])); //[4,4]
console.log(bestSum2(100, [1, 2, 5, 25])); //[25,25,25,25]
