/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x: number) {if(x<0)return false;
  let s_x: string = String(x);
  let len: number = s_x.length;
  for (let i: number = 0; i < len / 2; i++) {
    if (s_x[i] != s_x[len - i - 1]) return false;
  }
  return true;
};
