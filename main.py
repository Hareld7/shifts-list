import random

print("****************")
print("Please write the time in four letters")
startTime = input("start time: ")
endTime = input("end time: ")

#choosing a list from a file or creating a new one
def find_list():
    readInputFromFile = input("From a file? y for yes, n for no.    ")
    print("****************")
    if readInputFromFile[0] == "y":
        newFileInput = input("New File? y for yes, n for no.   ")
        print("****************")
        if newFileInput[0] == "y":
            list = input("Save file as: ")+".csv"
            print("****************")
        else:
            chooseFileInput = input("Choose file: ")
            print("****************")
            try:
                list = open(chooseFileInput, "r")
            except FileNotFoundError:
                print("File does not exists, please create a new one")
                print("****************")
                list = input("Save file as: ")+".csv"
                print("****************")
        with open(list, "a") as file:
            print("Write each name separately, When done write 'q'")
            name = ""
            while name != "q":
                name = input("Name: ")
                if name != "q":
                    file.write(f"{name},")

        with open(list, "r") as file1:
            num = 0
            list = []
            po = file1.read()
            row = po.split(",")
            for i in range(len(row) - 1):
                list.append(row[num])
                num = num + 1
#one-time list from input
    else:
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
random.shuffle(names)
print("****************")
watchList = makeList(names, startTime, endTime)
for i in watchList:
    print(i + ':', watchList[i])
print("***************")