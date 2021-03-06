#!/usr/bin/env python
#coding=UTF8
'''
    @author: devin
    @time: 2013-11-23
    @desc:
        timer
'''
import threading
import time

class Timer(threading.Thread):
    '''
        每隔一段时间执行一遍任务
    '''
    def __init__(self, seconds, fun, **args):
        '''
            seconds为间隔时间，单位为秒
            fun为定时执行的任务
            args为fun对应的参数
        '''
        self.sleep_time = seconds
        threading.Thread.__init__(self)
        self.fun = fun
        self.args = args
        self.is_run = True

    def run(self):
        while self.is_run:
            time.sleep(self.sleep_time)
            self.fun(**self.args)

    def stop(self):
        self.is_run = False
        time.sleep(0.1)

class CountDownTimer(Timer):
    '''
        一共执行指定次数
    '''
    def __init__(self, seconds, total_times, fun, **args):
        '''
            total_times为总共执行的次数
            其它参数同Timer
        '''
        self.total_times = total_times
        Timer.__init__(self, seconds, fun, args)
    
    def run(self):
        counter = 0
        while counter < self.total_times and self.is_run:
            time.sleep(self.sleep_time)
            self.fun(**self.args)
            counter += 1


if __name__ == "__main__":
    def test(s):
        print s
    timer = Timer(2, test, s="a")
    timer.start()

    time.sleep(10)
    timer.stop()
