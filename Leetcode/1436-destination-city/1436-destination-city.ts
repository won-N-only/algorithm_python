function destCity(paths: string[][]): string {
  let s_grid: Map<string, string> = new Map();
  let e_grid: Map<string, string> = new Map();

  paths.forEach(([start, end]) => {
    s_grid.set(start, end);
    e_grid.set(end, start);
  });

  for (let end of e_grid.keys()) {
    if (!s_grid.has(end)) return end;
  }
  return "";
}
