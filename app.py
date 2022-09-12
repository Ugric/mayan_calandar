def mayan_calandar(baktun: int, katun: int, tun: int, uninal: int, kin: int):
    katun += 20*baktun
    tun += 20*katun
    uninal += 18*tun
    kin += 20*uninal
    return kin


epoch = 2018843  # 1/1/2000

calandar_input = input('input: ').split(' ')
output = []

for i in range(len(calandar_input)):
    output.append(int(calandar_input[i]))


current = mayan_calandar(output[0], output[1], output[2], output[3], output[4])

difference = (current - epoch)
year = 2000
days = difference

month = ""

while True:
    month = "January"
    remove = 31
    if days - remove < 0:
        break
    days -= remove

    month = "February"
    remove = 29 if (year % 100 != 0 and year %
                    4 == 0) or (year % 400 == 0) else 28
    if days - remove < 0:
        break
    days -= remove

    month = "March"
    remove = 31
    if days - remove < 0:
        break
    days -= remove

    month = "April"
    remove = 30
    if days - remove < 0:
        break
    days -= remove

    month = "May"
    remove = 31
    if days - remove < 0:
        break
    days -= remove

    month = "June"
    remove = 30
    if days - remove < 0:
        break
    days -= remove

    month = "July"
    remove = 31
    if days - remove < 0:
        break
    days -= remove

    month = "August"
    remove = 31
    if days - remove < 0:
        break
    days -= remove

    month = "September"
    remove = 30
    if days - remove < 0:
        break
    days -= remove

    month = "October"
    remove = 31
    if days - remove < 0:
        break
    days -= remove

    month = "November"
    remove = 30
    if days - remove < 0:
        break
    days -= remove

    month = "December"
    remove = 31
    if days - remove < 0:
        break
    days -= remove
    year += 1

print(days+1, month, year)
