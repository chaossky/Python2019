<<<<<<< HEAD
word=input('단어를 입력하세요 :  ')

is_palindrom=True
for i in range(len(word)//2):
    if word[i] != word[-1-i]:
        is_palindrom=False
        break

=======
word=input('단어를 입력하세요 :  ')

is_palindrom=True
for i in range(len(word)//2):
    if word[i] != word[-1-i]:
        is_palindrom=False
        break

>>>>>>> 18c0589cd863ddd50038bf9d112beb00982f3dfd
print(is_palindrom)