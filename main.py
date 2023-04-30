import random

#THE TIME SET BLOCK
print("****************")
print("Please write the time in four letters")
#for each start and end time, ask for input and confirm its in four letters
#if th input is not in four letters ask for it again
startTime = input("start time: ")
if len(startTime) != 4:
    print("Please write time in four letters")
    startTime = input("start time: ")
endTime = input("end time: ")
if len(endTime) != 4:
    print("Please write time in four letters")
    endTime = input("end time: ")

#THE NAMES LIST BLOCK
#choosing a list from a new/existing file or manual mode where you put each name manually
def find_list():
    # asking if the user want to use a file or manual mode
    readInputFromFile = input("From a file?    y for yes, n for no    |  ")
    print("****************")
    if readInputFromFile[0] == "y":
        list = []
        print("Please pick an existing file or create a new one")
        while len(list) == 0:
            newFileQuestion = input("Do you want to create a new file?  y for yes   |   ")
            if newFileQuestion[0] == "y":
                chooseFileName = input("Save as:    |    ")
                with open(chooseFileName, "a") as file:
                    name = ""
                    while name != "q":
                        print("Write each name separately, "
                              "When done type 'q' ")
                        name = input("Name: ")
                        if name != "q":
                            file.write(f"{name},")
            else:
                chooseFileName = input("File name?    |   ")
            try:
                with open(chooseFileName, "r") as file:
                    num = 0
                    po = file.read()
                    row = po.split(",")
                    for i in range(len(row) - 1):
                        list.append(row[num])
                        num = num + 1
            except FileNotFoundError:
                print("File not found")
#one-time list from input
    else:
        print("Write each name separately, "
              "When done type 'q' ")
        list = []
        inp = ""
        while inp != "q":
            inp = input("Name: ")
            if inp != "q":
                list.append(inp)
    return list

#finds the gap between a given start time & end time
def find_gap(start, end):
    startHour = int(start[:2])
    endHour = int(end[:2])
    startMinute = int(start[2:])
    endMinute = int(end[2:])
    minuteGap = (endMinute - startMinute)
    if minuteGap < 0:
        hourGap = (endHour - startHour - 1) % 24
        minuteGap = minuteGap % 60
    else:
        hourGap = (endHour - startHour) % 24
    return hourGap, minuteGap

#finds the gap per shift, using the previous find_gap function & given names list
def personalGap(list, start, end):
    totalGap = find_gap(start, end)
    hourGap = totalGap[0] // len(list)
    hourGapRemains = totalGap[0] % len(list)
    totalMinutes =  totalGap[1] + (hourGapRemains * 60)
    minutesGap = totalMinutes // len(list)
    return hourGap, minutesGap

#making a dict type, names are the keys, the start time of every shift is the value key
def makeList(list, start, end):
    random.shuffle(list)
    dict = {list[0]: start[:2]+":"+start[2:]}
    currentHour = (start[:2])
    currentMinute = (start[2:])
    for i in list[1:]:
        personal_gap = personalGap(list, start, end)
        hourGap = personal_gap[0]
        minuteGap = personal_gap[1]
        if int(currentMinute) + int(minuteGap) >= 60:
            hourGap = hourGap + 1
        currentHour = (int(currentHour) + hourGap) % 24
        currentMinute = (int(currentMinute) + int(minuteGap)) % 60
        currentTime = str(currentHour).zfill(2)+':'+str(currentMinute).zfill(2)
        dict.update({i: currentTime})
    return dict

#TESTS
print("****************")
print("Shifts list:")
print("****************")
names = find_list()
print("****************")
watchList = makeList(names, startTime, endTime)
for i in watchList:
    print(i + ':', watchList[i])
print("***************")