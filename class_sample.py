class Ball:
    color=""
    speed=0

    def setSpeed(self,value):
        self.speed=value


ball01=Ball()
ball01.color="Red"
ball01.setSpeed(10)



ball02=Ball()
ball02.color="Blue"
ball02.setSpeed(20)

print("Ball01 color:%s" %ball01.color)
print("Ball01 speed:%s" %ball01.speed)

print("Ball02 color:%s" %ball02.color)
print("Ball02 speed:%s" %ball02.speed)


