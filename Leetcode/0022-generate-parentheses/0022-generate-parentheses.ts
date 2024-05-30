type stack = {curr: string; open: number; close: number};
function generateParenthesis(n: number): string[] {
  let ans: string[] = [];
  let stack: stack[] = [];

  stack.push({curr: "", open: 0, close: 0});

  while (stack.length) {
    let {curr, open, close} = stack.pop()!;
    console.log("이게 stack %s", JSON.stringify(stack));

    if (curr.length == 2 * n) {
      ans.push(curr);
      continue;
    }

    if (open < n) {
      stack.push({curr: curr + "(", open: open + 1, close});
    }
    if (close < open) {
      stack.push({curr: curr + ")", open, close: close + 1});
    }
  }

  return ans;
}