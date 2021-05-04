import datetime


def create_schedule(start_date, end_date, start_time, end_time):
    delta = datetime.timedelta(days=1)
    enter_delta = datetime.timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
    exit_delta = datetime.timedelta(hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second)
    delta2 = exit_delta - enter_delta
    ret = []
    if enter_delta > exit_delta:
        while start_date < end_date:
            start = datetime.datetime(start_date.year,start_date.month,start_date.day,start_time.hour,start_time.minute)
            start_date = start_date + delta
            end = datetime.datetime(start_date.year,start_date.month,start_date.day,end_time.hour,end_time.minute)
            ret.append((start, end))
        return ret
    else:
        while start_date <= end_date:
            start = datetime.datetime(start_date.year,start_date.month,start_date.day,start_time.hour,start_time.minute)
            end = start + delta2
            ret.append((start,end))
            start_date = start_date + delta
        return ret
