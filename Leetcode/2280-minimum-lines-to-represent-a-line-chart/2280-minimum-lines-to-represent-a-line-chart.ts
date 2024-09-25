function minimumLines(stockPrices: number[][]): number {
  stockPrices.sort((a, b) => a[0] - b[0]);

  if (stockPrices.length === 1) return 0;

  let cnt: number = 1;

  for (let i = 1; i < stockPrices.length - 1; i++) {
    const [x1, y1] = stockPrices[i - 1].map(BigInt);
    const [x2, y2] = stockPrices[i].map(BigInt);
    const [x3, y3] = stockPrices[i + 1].map(BigInt);

    // 두 기울기가 같은지 확인하기 위해 분수 비교
    const dx1 = x2 - x1;
    const dy1 = y2 - y1;

    const dx2 = x3 - x2;
    const dy2 = y3 - y2;

    //bigint니까 나누기안하고 곱하기로함
    if (dy1 * dx2 !== dy2 * dx1) {
      cnt++;
    }
  }

  return cnt;
}