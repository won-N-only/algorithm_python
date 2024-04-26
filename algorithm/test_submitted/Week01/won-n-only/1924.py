def today(x, y):
    # day 일련번호구해서
    day_total = 0
    for i in range(0, x):
        if i in end_day28:
            day_total += 28
        if i in end_day30:
            day_total += 30
        if i in end_day31:
            day_total += 31
    #나누고 출력
    whatday = (day_total + y) % 7
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(days[whatday])


x, y = map(int, input().split())

end_day30 = [4, 6, 9, 11]
end_day31 = [1, 3, 5, 7, 8, 10, 12]
end_day28 = [2]
today(x, y)
