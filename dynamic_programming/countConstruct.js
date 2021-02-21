/*
Write a function countConstruct(target, wordBank) that accepts a target string an array of strings
The function should return the number of ways that the target can be constructed by concatenating elements of the wordBank array

you may reuse elements of wordBank as many times needed.
*/

const countConstruct = (target, wordBank, table = {}) => {
  if (target.length === 0) return 1;
  if (target in table) return table[target];

  let sum = 0;

  for (let word of wordBank) {
    if (target.indexOf(word) === 0) {
      //if the word in wordbank is found at the beginning of the target string (prefix) then we subtract it from the target and pass the suffix (whats left)
      sum += countConstruct(target.slice(word.length), wordBank, table); //add the number of ways to create the rest of string
    }
  }
  table[target] = sum;
  return table[target];
};

console.log(
  countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) //0
);

console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])); //1

console.log(
  countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
  ])
);
//0

console.log(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])); //2
console.log(
  countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) //4
);

const countConstruct2 = (target, wordBank) => {
  const table = Array(target.length + 1).fill(0);
  table[0] = 1;

  for (let i = 0; i <= target.length; i++) {
    if (table[i] !== 0) {
      for (let word of wordBank) {
        //if the word matches the characters starting at position i
        if (target.slice(i).indexOf(word) === 0) {
          table[i + word.length] += table[i]; //if so then at that point that prefix of the word can be constructed so add how many ways it takes to make that previous prefix including all the other ways
        }
      }
    }
  }
  return table[target.length];
};

console.log(
  countConstruct2("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) //0
);

console.log(countConstruct2("abcdef", ["ab", "abc", "cd", "def", "abcd"])); //1

console.log(
  countConstruct2("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
  ])
);
//0

console.log(countConstruct2("purple", ["purp", "p", "ur", "le", "purpl"])); //2
console.log(
  countConstruct2("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]) //4
);
