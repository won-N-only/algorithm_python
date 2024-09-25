function climbStairs(n: number): number {
  if (n == 1) return 1;
  let n1: number = 1,
    n2: number = 2;
  for (let i: number = 3; i <= n; i++) {
    let temp: number = n1;
    n1 = n2;
    n2 = n1 + temp;
  }
  return n2;
}
