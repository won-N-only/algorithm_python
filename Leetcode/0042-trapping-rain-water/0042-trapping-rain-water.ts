// function findMax(arr: number[]): number | null {
//   if (arr.length === 0) return null;

//   let max = arr[0];
//   let index = 0;

//   for (let i = 1; i < arr.length; i++) {
//     if (arr[i] > max) {
//       index = i;
//     }
//   }

//   return arr.length - index;
// }

// function trap(height: number[]): number {
//   let start: number = 0;
//   let sum: number = 0;
//   let idx: number = 1;

//   // 이상인거 만날때까지 start는 불변

//   start = height.pop() ?? 0; // 이렇게쓰면 undefined나 null일때 0 할당함 ㅎㅎ
//   let cnt: number = height.length;
//   let max_idx: number = findMax(height) ?? 0;
//   let cnt_idx: number = findMax(height) ?? 0;

//   for (let i: number = 0; i < cnt; i++) {
//     let next: number = height.pop() ?? 0;
//     // start보다 높으면 그대로 keep going
//     if (next >= start) {
//       cnt_idx = 1;
//       start = next;
//       continue;
//     }

//     // 최댓값 찾아감
//     if (idx == max_idx) {
//       sum += start - next;
//       height.pop() ?? 0;

//       let one: number = height.at(-1) ?? 0;
//       let two: number = height.at(-2) ?? 0;
//       if (one >= two) {
//         sum -= (start - one) * idx;
//       }
//     }
//     sum += start - next;
//     idx += 1;
//   }
//   return sum;
// }

///////////////////////////////////////////////////////////

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
      let gap: number = curr - stack[stack.length - 1] - 1;
      let dist: number =
        Math.min(height[curr], height[stack[stack.length - 1]]) - height[top];

      console.log(dist);
      console.log(gap);
      sum += dist * gap;
    }

    //스택 없거나 내가작으면 push
    stack.push(curr);
    curr++;
  }

  return sum;
}

let height: number[] = [4, 2, 0, 3, 2, 5, 1];
console.log(trap(height));
