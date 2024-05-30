
function merge(intervals: number[][]): number[][] {
  const ans: number[][] = [];
  intervals.sort((a, b) => a[0] - b[0]);

  let start: number[] = intervals[0];
  for (let i = 1; i < intervals.length; i++) {
    if (start[1] >= intervals[i][0]) {
      start = [start[0], Math.max(start[1], intervals[i][1])];
    } else {
      ans.push(start);
      start = intervals[i];
    }
  }

  ans.push(start);

  return ans;
}