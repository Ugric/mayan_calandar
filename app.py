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

month = 0

tobreak = False

while not tobreak:
    month_times = [31, (29 if (year % 100 != 0 and year %
                    4 == 0) or (year % 400 == 0) else 28), 31,30,31,30,31,31, 30,31,30,31]
    tobreak = True
    for i in range(len(month_times)):
        month = i
        if days - month_times[i] < 0:
            break
        days -= month_times[i]
    else:
        year += 1
        tobreak = False

print(days+1, month+1, year)
