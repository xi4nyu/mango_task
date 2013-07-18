# coding: utf-8

"""Demo task.

Test task.

"""

from datetime import datetime
from common.task_base import TaskBase


class DemoTask(TaskBase):
    def __init__(self):
        pass


    def __call__(self):
        print "It was called at %s." % datetime.now().isoformat(" ")


    @property
    def desc(self):
        return "Demo task."


    @property
    def cron(self):
        """
        ==================================
        Available fields
        ==================================
        ----------------------------------
        Field           Description
        ----------------------------------
        year            4-digit year number
        month           month number (1-12)
        day             day of the month (1-31)
        week            ISO week number (1-53)
        day_of_week     number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
        hour            hour (0-23)
        minute          minute (0-59)
        second          second (0-59)

        ==================================
        Expression types
        ==================================
        ---------------------------------
        Expression Field Description
        ----------------------------------
        *           any   Fire on every value
        */a         any   Fire every a values, starting from the minimum
        a-b         any   Fire on any value within the a-b range (a must be smaller than b)
        a-b/c       any   Fire every c values within the a-b range
        xth y       day   Fire on the x -th occurrence of weekday y within the month
        last x      day   Fire on the last occurrence of weekday x within the month
        last        day   Fire on the last day within the month
        x,y,z       any   Fire on any matching expression; can combine any number of any of the above expressions


        Example:
        
        1. Schedules job_function to be run on the third Friday
           of June, July, August, November and December at 00:00,
           01:00, 02:00 and 03:00
           
            month='6-8,11-12', day='3rd fri', hour='0-3' 


        2. Schedule a backup to run once from Monday to Friday at 5:30 (am)

            day_of_week='mon-fri', hour=5, minute=30
            
        """
        
        # return dict(seconds=3)
        return dict(day_of_week="mon-fri", second=0)
