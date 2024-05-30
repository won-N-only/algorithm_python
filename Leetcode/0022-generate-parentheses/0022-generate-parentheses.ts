function generateParenthesis(n: number): string[] {
  const ans: string[] = [];

  function bt(current: string, open: number, close: number) {
    if (current.length === 2 * n) {
      ans.push(current);
      return;
    }

    if (open < n) {
      bt(current + "(", open + 1, close);
    }
    if (close < open) {
      bt(current + ")", open, close + 1);
    }
  }

  bt("", 0, 0);
  return ans;
}