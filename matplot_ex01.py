<<<<<<< HEAD
# -*- coding: utf-8 -*-
# 한글을 입력하기 위한 코드이다....
# 몇가지 라이브러리를 임포트하여 사용한다.
# matplotlib , numpy, pandas

import matplotlib
import matplotlib.pyplot as plt
# (참조)https://matplotlib.org/api/pyplot_api.html#Matplotlib.pyplot.plot
import numpy as np
import pandas as pd

# 
# randn()은 가우시안 표준 정규 분포에서 난수 matrix array를 생성한다.
# cf. rand()는 0과 1 사이의 균일 분포에서 난수 matrix array를 생성

# cumsum()은 배열에서 주어진 축에 따라 누적되는 원소들의 누적합을 계산하는 함수이다.
# 참조 https://docs.scipy.org/doc/numpy/reference/generated/numpy.cumsum.html
# numpy.arange([start, ] stop, [step, ] dtype=None)

"""
numpy 모듈의 arange()함수는 반열린구간 [start, stop) 에서
step 의 크기만큼 일정하게 떨어져 있는 숫자들을 array 형태로 반환해 주는 함수다.
stop 매개변수의 값은 반드시 전달되어야 하지만 start 는 step 은 꼭 전달되지 않아도 된다.
start 값이 전달되지 않았다면 0 을 기본값으로 가지며, step 값이 전달되지 않았다면 1 값을 기본값으로 갖게 된다.

"""

# s=pd.Series(np.random.randn(100).cumsum(), index=np.arange(0,100,1))
# s=pd.Series(np.random.randn(100).cumsum(), index=np.arange(100))
s=pd.Series(np.random.randn(100).cumsum(), index=np.arange(0,100,1))

'''
데이터를 리스트나 1차원 배열 형식으로 Series 클래스 생성자에 넣어주면 시리즈 클래스 객체를 만들 수 있다. 
인덱스의 길이는 데이터의 길이와 같아야 한다. 
다음 예에서 이 "서울", "부산" 등의 문자열이 인덱스의 값이다. 
그래프에서 한글이 나오지 않아서 영문으로 표기
인덱스의 값을 인덱스 라벨(label)이라고도 한다. 
인덱스 라벨은 문자열 뿐 아니라 날짜, 시간, 정수 등도 가능하다.
'''
#s=pd.Series([9904312, 3448737, 2890451, 2466052],index=['Seoul','Busan','Incheon','Daegu'])

#print(s)
plt.xlabel('X value')
plt.ylabel('Y value')
plt.title('Random No.')
plt.plot(s,'r')


plt.annotate('this point',xy=(10,2),xytext=(20,5),arrowprops={'color':'green'})

"""
다음은 어노테이션이라는 기능으로, 
그래프에 화살표를 그린후, 그 화살표에 문자열을 출력하는 기능이다. 
예를들어 “이값이 최소값" 이런식으로 화살표를 그려서 표현할때 사용하는데 plt.annotate 함수를 사용하면 된다.

plt.annotate(‘문자열',xy,xytext,arrowprops) 식으로 사용한다.

문자열은 어노테이션에서 나타낼 문자열이고, 
xy는 화살표가 가르키는 점의 위치, 
xytext는 문자열이 출력될 위치, 
arrowprops는 화살표의 속성으로 칼라등을 정의한다.

출처: https://bcho.tistory.com/1201 [조대협의 블로그]

"""
plt.show()

#plot()메소드의 x,y값을 일일히 지정하거나
#시리즈를 통해 생성한 값을 넣어서 점을 찍듯이 그래프를 그림
#캐릭터 문자 입력으로 색깔을 바꿀수 있다.
# 'b'-blue  / 'g'- Green / 'r'- Red /'c'-Cyan
# 'm'-magenta / 'y'-Yellow / 'k'-black / 'w'-White
# 선종류 변경
#라벨
#타이틀

#https://bcho.tistory.com/1201
=======
# -*- coding: utf-8 -*-
# 한글을 입력하기 위한 코드이다....
# 몇가지 라이브러리를 임포트하여 사용한다.
# matplotlib , numpy, pandas

import matplotlib
import matplotlib.pyplot as plt
# (참조)https://matplotlib.org/api/pyplot_api.html#Matplotlib.pyplot.plot
import numpy as np
import pandas as pd

# 
# randn()은 가우시안 표준 정규 분포에서 난수 matrix array를 생성한다.
# cf. rand()는 0과 1 사이의 균일 분포에서 난수 matrix array를 생성

# cumsum()은 배열에서 주어진 축에 따라 누적되는 원소들의 누적합을 계산하는 함수이다.
# 참조 https://docs.scipy.org/doc/numpy/reference/generated/numpy.cumsum.html
# numpy.arange([start, ] stop, [step, ] dtype=None)

"""
numpy 모듈의 arange()함수는 반열린구간 [start, stop) 에서
step 의 크기만큼 일정하게 떨어져 있는 숫자들을 array 형태로 반환해 주는 함수다.
stop 매개변수의 값은 반드시 전달되어야 하지만 start 는 step 은 꼭 전달되지 않아도 된다.
start 값이 전달되지 않았다면 0 을 기본값으로 가지며, step 값이 전달되지 않았다면 1 값을 기본값으로 갖게 된다.

"""

# s=pd.Series(np.random.randn(100).cumsum(), index=np.arange(0,100,1))
# s=pd.Series(np.random.randn(100).cumsum(), index=np.arange(100))
s=pd.Series(np.random.randn(100).cumsum(), index=np.arange(0,100,1))

'''
데이터를 리스트나 1차원 배열 형식으로 Series 클래스 생성자에 넣어주면 시리즈 클래스 객체를 만들 수 있다. 
인덱스의 길이는 데이터의 길이와 같아야 한다. 
다음 예에서 이 "서울", "부산" 등의 문자열이 인덱스의 값이다. 
그래프에서 한글이 나오지 않아서 영문으로 표기
인덱스의 값을 인덱스 라벨(label)이라고도 한다. 
인덱스 라벨은 문자열 뿐 아니라 날짜, 시간, 정수 등도 가능하다.
'''
#s=pd.Series([9904312, 3448737, 2890451, 2466052],index=['Seoul','Busan','Incheon','Daegu'])

#print(s)
plt.xlabel('X value')
plt.ylabel('Y value')
plt.title('Random No.')
plt.plot(s,'r')


plt.annotate('this point',xy=(10,2),xytext=(20,5),arrowprops={'color':'green'})

"""
다음은 어노테이션이라는 기능으로, 
그래프에 화살표를 그린후, 그 화살표에 문자열을 출력하는 기능이다. 
예를들어 “이값이 최소값" 이런식으로 화살표를 그려서 표현할때 사용하는데 plt.annotate 함수를 사용하면 된다.

plt.annotate(‘문자열',xy,xytext,arrowprops) 식으로 사용한다.

문자열은 어노테이션에서 나타낼 문자열이고, 
xy는 화살표가 가르키는 점의 위치, 
xytext는 문자열이 출력될 위치, 
arrowprops는 화살표의 속성으로 칼라등을 정의한다.

출처: https://bcho.tistory.com/1201 [조대협의 블로그]

"""
plt.show()

#plot()메소드의 x,y값을 일일히 지정하거나
#시리즈를 통해 생성한 값을 넣어서 점을 찍듯이 그래프를 그림
#캐릭터 문자 입력으로 색깔을 바꿀수 있다.
# 'b'-blue  / 'g'- Green / 'r'- Red /'c'-Cyan
# 'm'-magenta / 'y'-Yellow / 'k'-black / 'w'-White
# 선종류 변경
#라벨
#타이틀

#https://bcho.tistory.com/1201
>>>>>>> 18c0589cd863ddd50038bf9d112beb00982f3dfd
