
function trap(height: number[]): number {
  if (height.length == 0) return 0;

  let stack: number[] = [];
  let curr: number = 0;
  let sum: number = 0;

  // 일단 가능할때 돌아
  while (curr < height.length) {
    //스택 남아있으면 돌면서 pop
    while (
      stack.length !== 0 &&
      height[curr] > height[stack[stack.length - 1]]
    ) {
      //일단 무조건 top뽑아
      let top: number = stack.pop() ?? 0;

      //마지막이었으면 컷
      if (stack.length == 0) break;

      //넣은놈 최종거리
      let dist: number = curr - stack[stack.length - 1] - 1;
      let gap: number =
        Math.min(height[curr], height[stack[stack.length - 1]]) - height[top];

      sum += dist * gap;
    }

    //스택 없거나 내가작으면 push
    stack.push(curr);
    curr++;
  }

  return sum;
}