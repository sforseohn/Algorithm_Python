money = 1000 - int(input())

values = (500, 100, 50, 10, 5, 1) # 배수 -> 그리디

ans = 0
for i in range(len(values)):
    if money == 0:
        break
    ans += money // values[i]
    money %= values[i]
    
print(ans)