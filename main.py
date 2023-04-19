import random

names = [
    'guard_1', 'guard_2', 'guard_3', 'guard_4', 'guard_5', 'guard_6'
]
random.shuffle(names)

startTime = '20.00'
endTime = '08.50'

def find_gap(start, end):
    startHour = int(start[:2])
    endHour = int(end[:2])
    startMinute = int(start[3:])
    endMinute = int(end[3:])
    minuteGap = (endMinute - startMinute)
    if minuteGap < 0:
        hourGap = (endHour - startHour - 1) % 24
        minuteGap = minuteGap % 60
    else:
        hourGap = (endHour - startHour) % 24
    return hourGap, minuteGap

def personalGap(list, start, end):
    totalGap = find_gap(start, end)
    hourGap = totalGap[0] // len(list)
    hourGapRemains = totalGap[0] % len(list)
    totalMinutes =  totalGap[1] + (hourGapRemains * 60)
    minutesGap = totalMinutes // len(list)
    return hourGap, minutesGap

def makeList(list, start, end):
    dict = {list[0]: start}
    currentHour = (start[:2])
    currentMinute = (start[3:])
    for i in list[1:]:
        personal_gap = personalGap(list, start, end)
        hourGap = personal_gap[0]
        minuteGap = personal_gap[1]
        if int(currentMinute) + int(minuteGap) > 60:
            hourGap = hourGap + 1
            currentHour = (int(currentHour) + hourGap) % 24
            currentMinute = (int(currentMinute) + int(minuteGap)) % 60
            currentTime = str(currentHour).zfill(2)+':'+str(currentMinute).zfill(2)
        else:
            currentHour = (int(currentHour) + hourGap) % 24
            currentMinute = (int(currentMinute) + int(minuteGap)) % 60
            currentTime = str(currentHour).zfill(2)+':'+str(currentMinute).zfill(2)
        dict.update({i: currentTime})
    return dict

print("****************")
print("Shifts list:")
print("****************")
watchList = makeList(names, startTime, endTime)
#end = get_end(startTime, )
for i in watchList:
    print(i + ':', watchList[i])
print("****************")
