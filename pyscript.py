import csv
import re


def people_attended(slist):
    with open('attendance_sheet.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                fullname = row[1].title().strip() + " " + row[2].title().strip()
                slist.append(fullname)
    slist = sorted(slist)
    return slist


def formatting(name, num):
    if num == 1:
        name = name.split(",")
        lastname = name[1].strip()
        name = str(name[0]).strip() + " " + str(lastname)
    else:
        name = name.split(", ")
        # print(name)
        lastname = str(name[:-1]).strip()
        lastname = re.findall(r"'(.*?)'", lastname, re.DOTALL)
        name = str(name[-1].strip()) + " " + str(lastname)[2:-2]
    return name.title()


def main():
    slist = []
    extra = []
    masterlist = []

    with open("masterlist.csv", 'r') as fp:
        lines = len(fp.readlines())

    number_of_members = lines


    slist = people_attended(slist)
    # print(slist)

    with open("masterlist.csv", "rt") as masterlistfile:
        countspl = 0
        for name in masterlistfile:
            name = formatting(name, 1)
            masterlist.append(name)
        returndict = dict(zip(masterlist, [0] * len(masterlist)))
        for showed in slist:
            # print("showed", showed)
            split = showed.split(maxsplit=1)
            # print("last name", split[1])
            countspl = sum(s.count(split[1]) for s in masterlist)
            # print(countspl)
            if countspl >= 1:
                # print("count: 1" + split[1])
                returndict[showed] = 1
            else:
                extra.append(showed)

    # print("\n\nFull List of all Members", masterlist)

    # print("\n\nOrganized File:", returndict)
    # print("\n\nPeople who came but aren't in NJHS yet (might have minor errors in names too, so double check this):", extra)

    errors = dict(list(returndict.items())[number_of_members-1:])
    # print("\n\nErrors in spreadsheet (different names, typos in name, etc):", errors)

    counter = 0
    for i in returndict:
        if 1 == returndict[i]:
            counter += 1

    print("\n\nNumber of people who came to the meeting: ", counter)

    returndict = dict(list(returndict.items())[:number_of_members-1])

    with open("errors.txt", "w", newline="") as errorfile:
        errorfile.write("Student Name\n")
        for i in errors:
            errorfile.write(i + "\n")

    with open("returntable.csv", 'w', newline='') as file:
        file.write("Student Name,Attendance\n")
        for j in returndict:
            file.write(f"{j},{returndict[j]}\n")

    with open("extras.txt", "w", newline="") as extrafile:
        extrafile.write("Student Name\n")
        for i in extra:
            extrafile.write(i + "\n")
