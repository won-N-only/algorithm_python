function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  let grid: Map<number, number[]> = new Map();
  let inD: number[] = new Array(numCourses).fill(0);

  /**Map 만들고 indegree배열 만들기 */
  for (let i: number = 0; i < numCourses; i++) grid.set(i, []);
  for (let [i, j] of prerequisites) {
    grid.get(j)?.push(i);
    inD[i]++;
  }

  let q: number[] = [];
  for (let i: number = 0; i < numCourses; i++) if (!inD[i]) q.push(i);
  let curr: number;
  let next: number;
  while (q.length) {
    curr = q.pop()!;
    for (next of grid.get(curr)!) {
      inD[next]--;
      if (!inD[next]) {
        q.push(next);
      }
    }
  }

  return sum(...inD) > 0 ? false : true;
}

const sum = (...arr: number[]): number =>
  arr.reduce((acc, cur) => acc + cur, 0);
