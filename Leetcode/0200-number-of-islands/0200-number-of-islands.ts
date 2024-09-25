function numIslands(grid: string[][]): number {
  let cnt: number = 0;

  function bfs(i: number, j: number) {
    if (grid[i]?.[j] == "1") {
      grid[i][j] = "0";
      bfs(i - 1, j);
      bfs(i + 1, j);
      bfs(i, j - 1);
      bfs(i, j + 1);
    }
  }

  for (let i: number = 0; i < grid.length; i++)
    for (let j: number = 0; j < grid[0].length; j++) {
      if (grid[i][j]=="1") {bfs(i, j);
      cnt++;}
    }
  return cnt;
}