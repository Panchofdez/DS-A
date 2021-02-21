/*
Write a function canConstruct(target, wordBank) that accepts a target string and an array of strings
The function should return a boolean inicating whether or not the 'target' can be constructed by concatenating elements of 
the 'wordBank' array

You may reuse elements of wordBank as many times as needed.
*/

//m = target, n = wordBank.length
//Brute Force approach => time: O(n^m * m) we multiply by m to account for splicing string,
//space: O(m*m) because for each stack frame we store a string of m length at worst when splicing

//Using memoization => time O(n*m*m), space O(m*m) we will have m keys and each key has a value of an array of m length at worst

const canConstruct = (target, wordBank, table = {}) => {
  if (target.length === 0) return true;
  if (target in table) return table[target];
  for (let word of wordBank) {
    if (target.indexOf(word) === 0) {
      //if the word in wordbank is found at the beginning of the target string (prefix) then we subtract it from the target and pass the suffix (whats left)
      if (canConstruct(target.slice(word.length), wordBank, table)) {
        table[target] = true;
        return table[target];
      }
    }
  }
  table[target] = false;
  return table[target];
};

console.log(
  canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) //false
);

console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])); //true

console.log(
  canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
  ])
);
//false

//USING TABULATION

const canConstruct2 = (target, wordBank) => {
  const table = Array(target.length + 1).fill(false);
  table[0] = true;

  for (let i = 0; i <= target.length; i++) {
    if (table[i] === true) {
      for (let word of wordBank) {
        //if the word matches the characters starting at position i
        if (target.slice(i).indexOf(word) === 0) {
          table[i + word.length] = true; //if so then at that point that prefix of the word can be constructed so true
        }
      }
    }
  }

  return table[target];
};

console.log(
  canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) //false
);

console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])); //true

console.log(
  canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
  ])
);
//false
