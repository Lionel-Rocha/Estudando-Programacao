import datetime
from datetime import time

#minha solução pessoal
def timeConversion(s):
    pm = "PM" in s
    stripped_time = s.strip("PM")
    time = datetime.datetime.strptime(stripped_time, '%H:%M:%S')
    

    if (pm):
      time_change = datetime.timedelta(hours=12) 
      time = time + time_change  

    time = time.time()
    print(time)
    return time

#a solução """""certa"""". Não gostei!
def timeConversion(s):
    arr = s.split(":")

    if "AM" in s:
        if arr[0] == "12":
            arr[0] = "00"
    else:
        if arr[0] != "12":
            arr[0] = str(12+int(arr[0]))
    arr[2] = arr[2][:2]

    return ":".join(arr)

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
