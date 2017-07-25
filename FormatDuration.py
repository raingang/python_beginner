def format_duration(seconds):
    if seconds == 0:
        return 'now'
    else:
        string = ''
        secs = seconds % 60
        mins = (seconds) // 60
        hours = mins//60
        mins -= hours*60
        days = hours//24
        hours -= days*24
        years = days//365
        days -= years*365
        integers = [years, days, hours, mins, secs]
        words = ['years', 'days', 'hours', 'minutes', 'seconds']
        result_arr = []
        for i in range(0, len(integers)):
            if integers[i] != 0:
                if integers[i] == 1:
                    result_arr.append(str(integers[i]) + ' ' + words[i][:-1])
                else:
                    result_arr.append(str(integers[i]) + ' ' + words[i])

        for i in range(0, len(result_arr) - 1):
            if (i == len(result_arr) - 2):
                result_arr[i] += ' and'

            else:
                result_arr[i] += ','

        return ' '.join(result_arr)

print(format_duration(1211212322))
