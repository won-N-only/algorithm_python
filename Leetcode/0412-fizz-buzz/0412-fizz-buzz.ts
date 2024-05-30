function fizzBuzz(n: number): string[] {
  let ans: string[] = [];

  for (let i: number = 1; i <= n; i++) {
    let a: string = "";
    //5로 나눠질 때만 3으로 나누게 수정함
    if (!(i % 5)) {
      if (!(i % 3)) a = "FizzBuzz";
      else a = "Buzz";
    } else if (!(i % 3)) {
      a = "Fizz";
    } else {
      a = String(i);
    }
    ans.push(a);
  }
  return ans;
}

