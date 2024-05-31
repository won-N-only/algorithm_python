 
var minTimeToVisitAllPoints = function (points: number[][]): number {
  let time = 0;

  for (let i = 0; i < points.length - 1; i++) {
    let start = points[i];
    let end = points[i + 1];
    while (start[0] !== end[0] || start[1] !== end[1]) {
      if (start[0] < end[0]) start[0]++;
      else if (start[0] > end[0]) start[0]--;

      if (start[1] < end[1]) start[1]++;
      else if (start[1] > end[1]) start[1]--;

      time++;
    }
  }
  return time;
};
 