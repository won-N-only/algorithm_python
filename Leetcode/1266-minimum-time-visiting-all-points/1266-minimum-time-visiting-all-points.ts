
var minTimeToVisitAllPoints = function (points: number[][]): number {
  let time = 0;

  for (let i = 0; i < points.length - 1; i++) {
    let curr = points[i];
    let next = points[i + 1];

    while (curr[0] !== next[0] || curr[1] !== next[1]) {
      move_dir(curr, next);
      time++;
    }
  }
  return time;
};

function move_dir(curr: number[], next: number[]): number[] {
  if (curr[0] < next[0]) curr[0]++;
  else if (curr[0] > next[0]) curr[0]--;

  if (curr[1] < next[1]) curr[1]++;
  else if (curr[1] > next[1]) curr[1]--;

  return curr;
}
