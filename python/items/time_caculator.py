'''
Author: dingdingtao
Date: 2021-01-26 18:10:05
LastEditTime: 2021-03-15 14:20:48
LastEditors: dingdingtao
Description: caculator days
'''
import time
import calendar
import datetime
import argparse
import re

def year_days(year):
    '''
    if year is leap return 366 else return 365
    '''
    return 366 if calendar.isleap(int(str(year))) else 365


def parse_time(_time):
    '''
    parse time format 'yyyy-MM-dd' as timestamps
    '''
    return time.localtime(time.mktime(time.strptime(_time,"%Y-%m-%d")))


def time_caculator(method, arg1, arg2):
    ''''''
    def count_days(start, end):
        '''
        input format yyyy-MM-dd
        return the days number, from start to end
        '''
        start_time = parse_time(start)
        start_yds = year_days(start_time.tm_year)

        end_time = parse_time(end)
        end_yds = year_days(end_time.tm_year)
        
        if start_time.tm_year < end_time.tm_year:
            '''
            if start_year < end_year 
            return start year left days + end year pass days
            '''
            year_diff = end_time.tm_year - start_time.tm_year
            year_diff_days = 0
            diff_counter = 1
            while diff_counter < year_diff:
                year = int(start_time.tm_year) + diff_counter
                year_diff_days += year_days(year)
                diff_counter += 1
            return (end_time.tm_yday) + (start_yds - start_time.tm_yday) + (year_diff_days)
        elif start_time.tm_year == end_time.tm_year:
            '''
            if start_year = end_year
            return year end day - year start day
            '''
            if start_time.tm_mon > end_time.tm_mon:
                raise ValueError("month input error.")
            if start_time.tm_mon == end_time.tm_mon:
                if start_time.tm_mday > end_time.tm_mday:
                    raise ValueError("day input error.")
            return end_time.tm_yday - start_time.tm_yday
        elif start_time.tm_year > end_time.tm_year:
            '''
            if start_year > end_year
            error. start must <= end
            '''
            raise ValueError("year input error.")
    
    def plus_days(start, days):
        '''return the date of start date plus days'''
        day = 60*60*24
        start_timestamp = time.mktime(time.strptime(start,"%Y-%m-%d"))
        start_timestamp = start_timestamp + day*days
        result_date = time.localtime(start_timestamp)
        return "{year}-{month}-{day}".format(year=result_date.tm_year, month=result_date.tm_mon, day=result_date.tm_mday)

    def reduce_days(end, days):
        '''return the date of end date reduce days'''
        day = 60*60*24
        end_timestamp = time.mktime(time.strptime(end,"%Y-%m-%d"))
        end_timestamp = end_timestamp - day*days
        result_date = time.localtime(end_timestamp)
        return "{year}-{month}-{day}".format(year=result_date.tm_year, month=result_date.tm_mon, day=result_date.tm_mday)

    if method == 'count_days':
        start = arg1
        end = arg2
        r = count_days(start, end)
        return r
    elif method == 'plus_days':
        start = arg1
        days = arg2
        r = plus_days(start, days)
        return r
    elif method == 'reduce_days':
        end = arg1
        days = arg2
        r = reduce_days(end, days)
        return r


def check_date(date):
    '''check the date format.'''
    flag = False
    if flag:
        raise ValueError("date fromat error.")
    return date


def check_days(days):
    '''check the days format.'''
    flag = False
    if days < 0:
        raise ValueError("days input error.")
    return days


def parser_argument_list():
    '''config the argument list'''
    today = time.strftime("%Y-%m-%d", time.localtime())
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--count_method", help="the count method of this function.", default='count_days', choices=['count_days','plus_days','reduce_days'])
    parser.add_argument("-sd", "--start_date", help="the start date, fromat yyyy-MM-dd. default today.", default=today)
    parser.add_argument("-ed", "--end_date", help="the end date, fromat yyyy-MM-dd. default today.", default=today)
    parser.add_argument("-d", "--days", help="the days you want to addition or subtraction.", default=0, type=int)
    args = parser.parse_args()
    return args


def run():
    '''argument list'''
    args = parser_argument_list()
    
    try:
        start = check_date(args.start_date)
        end = check_date(args.end_date)
        method = args.count_method
        days = check_days(args.days)
        if args.count_method == 'count_days':
            result_days = time_caculator(method, start, end)
            print('from', start, 'to', end, 'total days:', result_days)
        elif args.count_method == 'plus_days':
            result_date = time_caculator(method, start, days)
            print(start, "plus", days, "day is", result_date)
        elif args.count_method == 'reduce_days':
            result_date = time_caculator(method, end, days)
            print(start, "reduce", days, "day is", result_date)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    run()