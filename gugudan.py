#구구단을 문자 포매팅을 이용해서 출력하는 프로그램이다.
for x in range(2,10):#for문을 통해서 숫자 2부터 9까지 출력한다.
    print("<{}단 출력>".format(x))#몇단인지를 출력한다.
    for y in range(1,10):#이중 for 문과 문자열 포매팅을 이용해서 구구단 출력                
      print("%s X %s = %s" % (x,y,x*y))
    
    
