function reverse(x: number): number {
  const rev_s = x.toString().split("").reverse().join("");
  const ans = parseInt(rev_s, 10);
  if (ans > 2 ** 31 - 1 || ans < -(2 ** 31)) return 0;
  return x < 0 ? -ans : ans;
}
