function longestCommonPrefix(strs: string[]): string {
  let result: string = "";
  strs.sort((a, b) => a.length - b.length);
  let size: number = strs.length;
  let elem_len: number = strs[0].length;

  //문자별로 돌면서 같은지 검색
  for (let i: number = 0; i < elem_len; i++) {
    let elem: string = strs[0][i];
    for (let j: number = 1; j < size; j++) {
      //다른문자 생기면 바로 리턴
      if (strs[j][i] != elem) return result;
    }
    result += elem;
  }
  return result;
}

