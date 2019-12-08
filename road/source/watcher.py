import sys, time, threading, serial
# from mbee import serialstar
from lib.data_classes import *
from lib.motor_controller import *
from lib.data_parser import *
from lib.lsm6ds3 import *
from lib.indicator import *
from lib.usound import *

import global_

#-------------------------------------------------------------------------------------#

class Writer(threading.Thread):
    def __init__(self, out=''):
        super().__init__()
        self.alive = True
        self.name = 'Writer'
        self.out = out

    def run(self):
        stringData = 't:\t{:3.2f}\tv:\t{:2.1f} | {:2.1f}\tB1:\t{:3.1f}\tB2:\t{:3.1f}\tmode:\t{}\tL:\t{:3.3f}\t\t{:s}'
        data = None
        while self.alive:
            # Get data for printing.
            global_.lock.acquire(blocking=True, timeout=1)
            data = global_.motor_thread.controller.get_data()
            global_.lock.release()

            if (data == None):
                data = (0,0,0,0,0,0,0,'',0)

            self.out = stringData.format(*data)+'\t'+str(global_.motor_thread.controller.HARD_STOP)+'\t'+str(global_.motor_thread.controller.AB_choose)+'\n'
            sys.stdout.write(self.out)
            sys.stdout.flush()
            time.sleep(0.05)
        self.off()

    def off(self):
        print('############  Writer stopped  #############')

#-------------------------------------------------------------------------------------#
""" Used to control the motor by Motor_controller class """
class Motor_thread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.alive = True
        self.name = 'Motor'
        self.controller = Controller()
        #   Indicator initialization
        try:
            self.portex = indicator_init()
            print('indicator init')
        except BaseException:
            self.portex = None

    def run(self):
        while self.alive:
            if self.portex and self.controller.t % 10 == 0:
                indicate(self.controller.motor.readV(), self.portex)

            self.controller.t_prev = self.controller.t
            self.controller.t = time.time() - self.controller.starttime
            self.controller.update()

            if self.controller.motor:
                self.controller.motor.dstep = self.controller.dstep

        self.off()


    def off(self):
        if self.portex:
            indicator_off(self.portex)
        self.controller.off()
        print('############  Motor released  #############')

#-------------------------------------------------------------------------------------#
""" Used to control all operations """
class Watcher(threading.Thread):
    def __init__(self):
        super().__init__()
        self.alive = True
        self.name = 'Watcher'
        self.accel = Accelerometer()
        self.accel.ctrl()

        # self.usound = USound()
        self.usound = None

    def run(self):
        while self.alive:
            # Usound.
            if self.usound:
                usound = self.usound.read()
                if (usound < 300):
                    global_.motor_thread.controller.soft_stop = 1
                    if (usound < 70):
                        global_.motor_thread.controller.HARD_STOP = 1

            if global_.motor_thread.alive:
                # Check accelerometer data.
                [x, y, z] = self.accel.getdata()
                thr = 5
                if (x > thr) or (z > thr):
                    global_.motor_thread.controller.HARD_STOP = 1
                    print('got')
                    print(x," ", y," ", z)

        self.off()

    def off(self):
        print('############  Watcher stopped  ############')
