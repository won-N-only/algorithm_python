function lengthOfLongestSubstring(s: string): number {
  let res: number = 0;
  let sen: string = "";
  for (let i: number = 0; i < s.length; i++) {
    sen = s[i];
    for (let j: number = i + 1; j < s.length; j++) {
      if (sen.includes(s[j])) break;
      sen += s[j];
    }
    res = Math.max(res, sen.length);
    console.log(sen);
  }
  return res ;
}