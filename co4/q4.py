class Time:
  def __init__(self, hr, minu ,sec):
    self.__hr = hr
    self.__minu = minu
    self.__sec = sec
  def __add__(self, other):
    t1 = ((self.__hr)*3600) + ((self.__minu)*60) + self.__sec
    t2 = ((other.__hr)*3600) + ((other.__minu)*60) + other.__sec
    return t1+t2
t1 = Time(int(input("Enter hour 1: ")), int(input("Enter minute 1: ")), int(input("Enter seconds 1: ")))
t2 = Time(int(input("Enter hour 2: ")), int(input("Enter minute 2: ")), int(input("Enter seconds 2: ")))
s = t1 + t2
hr = int(s/3600)
mi = int((s%3600)/60)
se = int((s%3600)%60)
print("{0} hr: {1} min: {2} sec".format(hr, mi, se))

