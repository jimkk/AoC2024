from utils.file import read_file

def main():
    reports = read_file('Day2/input.txt')

    reports = [[int(x) for x in x.split(' ')] for x in reports]


    part_1 = 0
    part_2 = 0
    for report in reports:
        steps = report.copy()
        for i in range(len(report)-1):
            steps[i] = steps[i+1] - steps[i]
        steps.pop(-1)

        increasing = 1 if steps[0] > 0 else -1

        consistent_trend = True
        for step in steps:
            if step * increasing <= 0:
                consistent_trend = False
                break
        if consistent_trend and  len([x for x in steps if abs(x) > 3]) == 0:
            part_1 += 1

        for i in range(len(report)):
            reduced_report = report.copy()
            reduced_report.pop(i)

            steps = []
            for i in range(len(reduced_report)-1):
                steps.append(reduced_report[i+1] - reduced_report[i])

            increasing = 1 if steps[0] > 0 else -1

            consistent_trend = True
            for step in steps:
                if step * increasing <= 0:
                    consistent_trend = False
                    break
            if consistent_trend and  len([x for x in steps if abs(x) > 3]) == 0:
                part_2 += 1
                break
        

    print('Part 1:', part_1)
    print('Part 2:', part_2)

if __name__ == '__main__':
    main()
