function numSpecial(mat: number[][]): number {
  //문제는 행렬의 posi가 고유한지
  //당장 생각나는건 summ 돌리는거
  //tricky한게있을거같은데
  let mine_i: number[] = [];
  let mine_j: number[] = [];
  let summ: number = 0;
  let res: number = 0;
  for (let i: number = 0; i < mat.length; i++) {
    for (let j: number = 0; j < mat[i].length; j++) {
      if (mat[i][j] == 0) continue;
      summ = -1;
      for (let row: number = 0; row < mat.length; row++) {
        summ += mat[row][j];
      }
      for (let col: number = 0; col < mat[i].length; col++) {
        summ += mat[i][col];
      }
      if (summ == 1) res += 1;
    }
  }
  return res;
}