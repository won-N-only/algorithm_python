c = int(input())
score = []
score_sum = 0
for i in range(c):
    score = [j for j in map(int, input().split())]
    score.remove(score[0])
    score_aver = sum(score)/len(score)
    score_s = [x for x in score if x > score_aver]
    aver_percent = len(score_s)/len(score)
    print(aver_percent*100,"%")
