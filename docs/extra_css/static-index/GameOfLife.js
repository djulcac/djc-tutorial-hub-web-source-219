const rows = 10;
const cols = 10;
let grid = createGrid(rows, cols);
const gridContainer = document.getElementById('grid');

function createGrid(rows, cols) {
  const grid = [];
  for (let i = 0; i < rows; i++) {
    grid.push(Array(cols).fill(0));
  }
  return grid;
}

function generateRandomGrid() {
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      grid[i][j] = Math.random() > 0.5 ? 1 : 0;
    }
  }
  renderGrid();
}

function countNeighbors(grid, x, y) {
  let sum = 0;
  const directions = [
    [-1, 0], [1, 0], [0, -1], [0, 1],
    [-1, -1], [-1, 1], [1, -1], [1, 1]
  ];
  for (const [dx, dy] of directions) {
    const newX = x + dx;
    const newY = y + dy;
    if (newX >= 0 && newX < rows && newY >= 0 && newY < cols) {
      sum += grid[newX][newY];
    }
  }
  return sum;
}

function nextGeneration() {
  const newGrid = grid.map(row => [...row]);
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      const neighbors = countNeighbors(grid, i, j);
      if (grid[i][j] === 1 && (neighbors < 2 || neighbors > 3)) {
        newGrid[i][j] = 0;
      } else if (grid[i][j] === 0 && neighbors === 3) {
        newGrid[i][j] = 1;
      }
    }
  }
  grid = newGrid;
  renderGrid();
}

function toggleCellState(row, col) {
  grid[row][col] = grid[row][col] ? 0 : 1;
  renderGrid();
}

function renderGrid() {
  gridContainer.innerHTML = '';
  for (let i = 0; i < rows; i++) {
    const rowEl = document.createElement('div');
    rowEl.className = 'row';
    for (let j = 0; j < cols; j++) {
      const cellEl = document.createElement('div');
      cellEl.className = 'cell' + (grid[i][j] ? ' alive' : '');
      cellEl.addEventListener('click', () => toggleCellState(i, j));
      rowEl.appendChild(cellEl);
    }
    gridContainer.appendChild(rowEl);
  }
}

// Iniciar
generateRandomGrid();
setInterval(nextGeneration, 1000); // Nueva generación cada 1s
