function minTimeToVisitAllPoints(points: number[][]): number {
  let time: number = 0;
  let me: number[] = points[0];

  for (let i: number = 1; i < points.length; i++) {
    const target = points[i];

    let dx = Math.abs(target[0] - me[0]);
    let dy = Math.abs(target[1] - me[1]);
    time += Math.max(dx, dy);

    me = target;
  }

  return time;
}

let points: number[][] = [
  [1, 1],
  [3, 4],
  [-1, 0],
];

console.log(minTimeToVisitAllPoints(points));
