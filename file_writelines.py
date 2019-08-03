lines=['안뇽하세요.\n','파이썬\n','코딩 도장입니다.\n','이장훈이 최고다 \n']

with open('hello.txt','w')as file:
    file.writelines(lines)