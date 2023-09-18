from extensions import jalali

def time_jalali(time):
    months=[
        'فروردین',
        'اردیبهشت',
        'خرداد',
        'تیر',
        'مرداد',
        'شهریور',
        'مهر',
        'آبان',
        'آذر',
        'دی',
        'بهمن',
        'اسفند',
    ]

    time_str='{},{},{}'.format(time.year,time.month,time.day)
    time_tuple=jalali.Gregorian(time_str).persian_tuple()
    time_list=list(time_tuple)

    for index , monht in enumerate(months):
        if time_list[1] == index + 1:
            time_list[1] == monht
            break
    output='{},{},{}_____{},{}'.format(
        time_list[2],
        time_list[1],
        time_list[0],
        time.hour,
        time.minute,
    )
    return output