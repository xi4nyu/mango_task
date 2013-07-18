# coding: utf-8

"""Task loader

Load task.

"""

from inspect import isclass
from apscheduler.scheduler import Scheduler

from task_base import TaskBase
from common import utility


def get_tasks():
    tasks = utility.get_members("tasks",
                                member_filter=lambda o: isclass(o)
                                and issubclass(o, TaskBase)
                                and o is not TaskBase)

    return tasks



def run():
    tasks = get_tasks()
    scheduler = Scheduler(standalone=True)
    print "执行任务:"
    for k, v in tasks.iteritems():
        t = v()
        print "%s: %s" % (t.desc, t.cron)
        scheduler.add_cron_job(t, **t.cron)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print "exit ..."
