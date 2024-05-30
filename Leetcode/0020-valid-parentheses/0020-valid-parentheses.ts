function isValid(s: string): boolean {
  let arr: string[] = [];
  let temp: string[] = [];
  for (let i: number = 0; i < s.length; i++) {
    if (arr.at(-1) == "(" && s[i] == ")") {
      arr.pop();
      continue;
    } else if (arr.at(-1) == "{" && s[i] == "}") {
      arr.pop();
      continue;
    } else if (arr.at(-1) == "[" && s[i] == "]") {
      arr.pop();
      continue;
    }
    arr.push(s[i]);
  }
  if (!arr.pop()) return true;
  return false;
}