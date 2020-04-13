'''
기본(default) 생성자
- 생성자를 생략하면 기본 생성자가 만들어진다.
- 묵시적 생성자

'''

class default_cost:
    def data(self,x,y):
        self.x = x
        self.y = y
    def mul(self):
        result = self.x * self.y
        return result

tmp = default_cost()
tmp.data(10,15)
print(tmp.mul())

class TV:
    channel = volume = 0
    power = False #off -> on
    color = None
    def volumeup(self):
        self.volume += 1

    def volumedown(self):
        if self.volume > 0 :
            self.volume -= 0

    def channelup(self):
        self.channel += 1

    def channeldown(self):
        self.channel -= 1

    def chpower(self):
        self.power = not(self.power)

    def data(self, channel , volume,color):
        self.channel = channel
        self.volume = volume
        self.color = color

    def display(cls):
        print( f"{cls.power}, {cls.volume} , {cls.channel} , {cls.color}")
'''
    def display(self):
        print( f"{self.power}, {self.volume} , {self.channel} , {self.color}")
'''
tmp = TV()
#tmp.data(10, 8 , "black")
#tmp.channelup()

print(tmp.power)
tmp.display()

import sys
print(sys.version)