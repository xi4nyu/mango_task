# coding: utf-8

"""Demo2

"""

from common.task_base import TaskBase



class DemoTask2(TaskBase):
    def __call__(self):
        print "demo2 was called."

        
    @property
    def desc(self):
        return "demo2"


    @property
    def cron(self):
        return dict(day_of_week="mon-fri", second=2)
