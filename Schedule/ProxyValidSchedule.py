# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ProxyValidSchedule.py  
   Description :  验证useful_proxy_queue中的代理,将不可用的移出
   Author :       JHao
   date：          2017/3/31
-------------------------------------------------
   Change Activity:
                   2017/3/31: 验证useful_proxy_queue中的代理
-------------------------------------------------
"""
import random

import time
from multiprocessing import Process

from DB.DbClient import DbClient

__author__ = 'JHao'

import sys

sys.path.append('../')

from Util.utilFunction import validUsefulProxy
from Manager.ProxyManager import ProxyManager
from Util.LogHandler import LogHandler


class ProxyValidSchedule(ProxyManager):
    def __init__(self):
        ProxyManager.__init__(self)
        self.db = DbClient()
        self.log = LogHandler('valid_schedule')

    def __validProxy(self):
        """
        验证代理
        :return:
        """
        time.sleep(60 * 0 * random.random())
        while True:
            self.db.changeTable(self.useful_proxy_queue)
            for each_proxy in self.db.getAll():
                if isinstance(each_proxy, bytes):
                    each_proxy = each_proxy.decode('utf-8')

                if validUsefulProxy(each_proxy):
                    # 成功计数器加1
                    self.db.inckey(each_proxy, 1)
                    self.log.debug('validProxy_b: {} validation pass'.format(each_proxy))
                else:
                    # 失败计数器减一
                    self.db.inckey(each_proxy, -1)
                    # self.db.delete(each_proxy)
                    self.log.info('validProxy_b: {} validation fail'.format(each_proxy))
                value = self.db.getvalue(each_proxy)
                if None != value and int(value) < -1:
                    # 计数器小于-5删除该代理
                    print "删除" + each_proxy
                    self.db.delete(each_proxy)
        self.log.info('validProxy_a running normal')

    def main(self):
        self.__validProxy()


def run():

    p_list = list()
    p1 = Process(target=ProxyValidSchedule, name='ProxyValidSchedule')
    p_list.append(p1)
    p2 = Process(target=ProxyValidSchedule, name='ProxyValidSchedule')
    p_list.append(p2)

    for p in p_list:
        p.start()
    for p in p_list:
        p.join()

    p = ProxyValidSchedule()
    p.main()


if __name__ == '__main__':
    p = ProxyValidSchedule()
    p.main()
