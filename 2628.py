# 위같은 배열에서
# 가로먼저자르고(점선간의 차이가 가장 큰걸로)
# 세로 다음에 잘라서 sum하면 될듯

a, b, = map(int, input().split())
line_count = int(input())
cols, rows = [], []
width, height = 0, 0

for i in range(line_count):
    line_input = list(map(int, (input().split())))
    if line_input[0] == 0:
        rows.append(line_input[1])
    else:
        cols.append(line_input[1])
rows = sorted(rows)
cols = sorted(cols)

if len(rows) == 1:
    width = max(b-rows[0], rows[0])
elif len(rows) > 1:
    rowslist = []
    for i in range(0, len(rows)-1):
        rowslist.append(-rows[i]+rows[i+1])
        max_rowslist = max(rowslist)
    width = max(b-rows[-1], max_rowslist, rows[0])
else:
    width = b
if len(cols) == 1:
    height = max(a-cols[0], cols[0])
elif len(cols) > 1:
    colslist = []
    for i in range(0, len(cols)-1):
        colslist.append(-cols[i]+cols[i+1])
        max_colslist = max(colslist)
    height = max(a-cols[-1], max_colslist, cols[0])
else:
    height = a
print((width*height))
