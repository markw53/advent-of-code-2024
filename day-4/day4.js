const fs = require('fs');

function countXMAS(grid) {
  const rows = grid.length;
  const cols = grid[0].length;
  let count = 0;

  function isXMAS(x, y) {
    const patterns = [
      [[-1, -1], [1, 1], [1, -1], [-1, 1]], 
      [[-1, 1], [1, -1], [1, 1], [-1, -1]]  
    ];

    for (const pattern of patterns) {
      const [M1, S1, M2, S2] = pattern;
      const [M1x, M1y] = [x + M1[0], y + M1[1]];
      const [S1x, S1y] = [x + S1[0], y + S1[1]];
      const [M2x, M2y] = [x + M2[0], y + M2[1]];
      const [S2x, S2y] = [x + S2[0], y + S2[1]];

      if (
        M1x >= 0 && M1x < rows && M1y >= 0 && M1y < cols &&
        S1x >= 0 && S1x < rows && S1y >= 0 && S1y < cols &&
        M2x >= 0 && M2x < rows && M2y >= 0 && M2y < cols &&
        S2x >= 0 && S2x < rows && S2y >= 0 && S2y < cols &&
        grid[M1x][M1y] === 'M' &&
        grid[S1x][S1y] === 'S' &&
        grid[M2x][M2y] === 'M' &&
        grid[S2x][S2y] === 'S' &&
        grid[x][y] === 'A'
      ) {
        return true;
      }
    }

    return false;
  }

  for (let x = 0; x < rows; x++) {
    for (let y = 0; y < cols; y++) {
      if (isXMAS(x, y)) {
        count++;
      }
    }
  }

  return count;
}

fs.readFile('input4.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }

  const grid = data.split('\n').map(line => line.trim().split(''));

  const occurrences = countXMAS(grid);

  console.log(`The X-MAS pattern appears ${occurrences} times in the grid.`);
});
