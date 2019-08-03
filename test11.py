even=odd=0
for i in range(1, 101):  # 1 ~ 100까지 반복
    if i % 2 == 0:  # i가 짝수일 경우
        even += i
    else:           # i가 홀수일 경우
        odd += i

print('짝수 합 : ', even)
print('홀수 합 : ', odd)


#part_sum=0
for a in range(1,10):
    print('---')
    sum_all=0
    for b in range(1,a,2):
        sum_all +=b
        print(b)
        print('sum is {}'.format(sum_all))

