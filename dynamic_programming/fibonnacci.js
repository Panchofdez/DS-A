//recursive fibonnaci (O(2^N )) time complexity O(N) space complexity
const fib = (n) => {
  if (n <= 2) {
    return 1;
  }
  return fib(n - 1) + fib(n - 2);
};

// console.log(fib(6)); //8
// console.log(fib(7)); //13
// console.log(fib(8)); //21

//using dynamic programing with memoization O(N) time and space complexity

const fibDP = (n, table = {}) => {
  //creates a new object table at the initial call
  if (n in table) return table[n];
  if (n <= 2) return 1;

  table[n] = fibDP(n - 1, table) + fibDP(n - 2, table); //pass in table so you can keep the same object storing the values
  return table[n];
};

// console.log(fibDP(6));
// console.log(fibDP(50));

//Using tabulation

const fibTB = (n) => {
  const table = Array(n + 1).fill(0);

  table[1] = 1;
  for (let i = 2; i < n + 1; i++) {
    table[i] = table[i - 1] + table[i - 2];
  }
  return table[n];
};

console.log(fibTB(6));
console.log(fibTB(50));
