import sys, time, threading

import global_
from global_ import get_logger

from lib.data_classes import *
from lib.motor_controller import *
from lib.lsm6ds3 import *
from lib.indicator import *
from lib.usound import *


#-------------------------------------------------------------------------------------#
class Writer(threading.Thread):
    def __init__(self, out=''):
        super().__init__()
        self.alive = True
        self.name = 'Writer'
        self.out = out

        self.logger = get_logger('Writer')

    def run(self):
        stringData = 't:\t{:3.2f}\tv:\t{:2.1f} | {:2.1f}\tB1:\t{:3.1f}\tB2:\t{:3.1f}\tmode:\t{}\tL:\t{:3.3f}\t\t{:s}'
        data = None
        while self.alive:
            # Get data for printing.
            if global_.motor_thread.controller:
                global_.lock.acquire(blocking=True, timeout=1)
                data = global_.motor_thread.controller.get_data()
                global_.lock.release()

            if data is None:
                data = (0, 0, 0, 0, 0, 0, 0, '', 0, 0)

            self.out = stringData.format(*data)
            self.logger.info(self.out)
            time.sleep(0.2)
        self.off()

    def off(self):
        self.logger.info('############  Writer stopped  #############')

#-------------------------------------------------------------------------------------#
class MotorThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.alive = True
        self.name = 'Motor'
        self.logger = get_logger('Motor')

        self.controller = Controller()
        if self.controller.client is None:
            self.alive = False
            self.controller = None

        #   Indicator initialization
        try:
            self.portex = indicator_init()
        except BaseException as exc:
            self.logger.warning('# Indicator init failed')
            self.portex = None
            return

        self.logger.info('# Indicator OK')

    def run(self):
        while self.alive:
            if self.portex and self.controller.t % 10 == 0:
                indicate(self.controller.motor.readV()*10, self.portex)

            self.controller.t_prev = self.controller.t
            self.controller.t = time.time() - self.controller.starttime
            self.controller.update()

            if self.controller.motor:
                self.controller.motor.dstep = self.controller.dstep
            time.sleep(0.02)

        self.off()

    def off(self):
        if self.portex:
            indicator_off(self.portex)
        if self.controller:
            self.controller.off()
        self.logger.info('############  Motor released  #############')

#-------------------------------------------------------------------------------------#
class Watcher(threading.Thread):
    def __init__(self):
        super().__init__()
        self.alive = True
        self.name = 'Watcher'

        self.logger = get_logger('Watcher')

        try:
            self.accel = Accelerometer()
            self.accel.ctrl()
            self.logger.info('# Accelerometer OK')
        except BaseException:
            self.accel = None
            self.logger.warning('# Accelerometer init failed')

        try:
            self.usound = None
            # self.usound = USound()
            self.logger.info('# USound OK')
        except BaseException as exc:
            self.logger.warning('# USound init failed')
            self.usound = None

    def run(self):
        while self.alive:
            if self.usound:
                usound = self.usound.read()
                # print(usound)
                if (usound < 300):
                    global_.motor_thread.controller.soft_stop = 1
                    if (usound < 70):
                        global_.motor_thread.controller.HARD_STOP = 1

            if global_.motor_thread.alive:
                # Check accelerometer data.
                [x, y, z] = self.accel.getdata()
                thr = 12
                if (x > thr) or (z > thr):
                    global_.motor_thread.controller.HARD_STOP = 1
                    self.logger.info('got ', x, ' ', y, ' ', z)

            time.sleep(0.02)

        self.off()

    def off(self):
        self.logger.info('############  Watcher stopped  ############')
