/*
Write a function allConstruct(target, wordBank)

the function should return a 2d array containing all of the ways that the target can be constructed by concatenating elements of the wordBank array.
Each element of the 2D array should represent one combination that constructs the target

You may reuse elements

*/

const allConstruct = (target, wordBank, table = {}) => {
  if (target === "") return [[]];
  if (target in table) return table[target];

  let results = [];

  for (let word of wordBank) {
    if (target.indexOf(word) === 0) {
      let suffixWays = allConstruct(target.slice(word.length), wordBank, table);
      if (suffixWays.length != 0) {
        suffixWays = suffixWays.map((way) => [...way, word]);
        results.push(...suffixWays);
      }
    }
  }
  table[target] = results;
  return table[target];
};

console.log(
  allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
);

console.log(
  allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])
);

console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));

console.log(
  allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",
  ])
);

//USING TABULATION

const allConstruct2 = (target, wordBank) => {
  const table = Array(target.length + 1)
    .fill()
    .map(() => []);
  table[0] = [[]];

  for (let i = 0; i <= target.length; i++) {
    if (table[i].length !== 0) {
      for (let word of wordBank) {
        if (target.slice(i).indexOf(word) === 0) {
          const newCombinations = table[i].map((way) => [...way, word]);
          table[i + word.length].push(...newCombinations);
        }
      }
    }
  }
  return table[target.length];
};

console.log(
  allConstruct2("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
);

console.log(
  allConstruct2("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])
);

console.log(allConstruct2("purple", ["purp", "p", "ur", "le", "purpl"]));

console.log(
  allConstruct2("eeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])
);
