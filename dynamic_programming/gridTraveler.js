/*Say that you are a traveler on a 2D grid. 
You begin in the top-left corner and your goal is to travel to the bottom right corner.
You may only move down or right

In how many ways can you travel to the goal on a grid with dimensions m * n? 
*/

//time and space complexity O(m*n)
const gridTraveler = (m, n, table = {}) => {
  const key = [m, n]; //the key that we are storing in our table (position in our grid)
  if (m == 0 || n == 0) return 0; //invalid grid or nowhere to go
  if (m == 1 && n == 1) return 1; //reached destination =  1 way
  if (key in table) return table[key]; //it doesnt matter the order a (1,2) grid will have the same amount of ways as a (2,1) grid
  table[key] = gridTraveler(m - 1, n, table) + gridTraveler(m, n - 1, table); //either go down or right

  return table[key];
};

console.log(gridTraveler(1, 1));
console.log(gridTraveler(2, 3)); //6
console.log(gridTraveler(3, 2)); //3
console.log(gridTraveler(3, 3)); //3
console.log(gridTraveler(18, 18)); //2333606220

//USING TABULATION
const gridTraveler2 = (m, n) => {
  const table = Array(m + 1)
    .fill()
    .map(() => Array(n + 1).fill(0));
  table[1][1] = 1; //in a 1 by 1 grid there is always 1 way
  for (let i = 0; i <= m; i++) {
    for (let j = 0; j <= n; j++) {
      const current = table[i][j];
      //add current value to right and down neighbour
      if (j + 1 <= n) table[i][j + 1] += current;
      if (i + 1 <= m) table[i + 1][j] += current;
    }
  }
  return table[m][n];
};

console.log(gridTraveler2(1, 1)); //1
console.log(gridTraveler2(2, 3)); //6
console.log(gridTraveler2(3, 2)); //3
console.log(gridTraveler2(3, 3)); //3
console.log(gridTraveler2(18, 18)); //2333606220
