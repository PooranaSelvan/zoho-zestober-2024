const grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
];

let rows = grid.length;
let cols = grid[0].length;
let islandCount = 0;

for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
        if (grid[i][j] === 1) {
            islandCount++;
            let stack = [[i, j]];
            for (let k = 0; k < stack.length; k++) {
                let [currentRow, currentCol] = stack[k];
                grid[currentRow][currentCol] = 0;

                if (currentRow + 1 < rows && grid[currentRow + 1][currentCol] === 1) {
                    stack.push([currentRow + 1, currentCol]);
                }

                if (currentRow - 1 >= 0 && grid[currentRow - 1][currentCol] === 1) {
                    stack.push([currentRow - 1, currentCol]);
                }

                if (currentCol + 1 < cols && grid[currentRow][currentCol + 1] === 1) {
                    stack.push([currentRow, currentCol + 1]);
                }
                
                if (currentCol - 1 >= 0 && grid[currentRow][currentCol - 1] === 1) {
                    stack.push([currentRow, currentCol - 1]);
                }
            }
        }
    }
}

console.log(islandCount);
