# -*- coding: utf-8 -*-
# !/usr/bin/env python

'''
self.name为Redis中的一个key
2017/4/17 修改pop
'''

import json

import redis

from Util.GetConfig import GetConfig


class RedisClient(object):
    """
    Reids client
    """

    def __init__(self, name,host,port,password):
        """
        init
        :param name:
        :param host:
        :param port:
        :return:
        """
        self.config = GetConfig()
        self.name = name
        print self.config.db_host
        print self.config.db_port
        print self.config.db_password
        self.__conn = redis.Redis(host=self.config.db_host,
                                  port=self.config.db_port,
                                  db='0',
                                  password=self.config.db_password)

    def get(self):
        """
        get random result
        :return:
        """
        return self.__conn.srandmember(name=self.name).decode('utf-8')         #redis return bytes

    def put(self, value):
        """
        put an  item
        :param value:
        :return:
        """
        value = json.dumps(value) if isinstance(value, (dict, list)) else value
        return self.__conn.sadd(self.name, value)

    def pop(self):
        """
        pop an item
        :return:
        """
        return self.__conn.spop(self.name).decode('utf-8')                    #redis return bytes

    def delete(self, value):
        """
        delete an item
        :param key:
        :return:
        """
        self.__conn.srem(self.name, value)

    def getAll(self):
        return self.__conn.smembers(self.name)

    def get_status(self):
        return self.__conn.scard(self.name)

    def changeTable(self, name):
        self.name = name


if __name__ == '__main__':
    gg = GetConfig()
    print(gg.db_type)
    print(gg.db_name)
    print(gg.db_host)
    print(gg.db_port)
    print(gg.db_password)

    redis_con = RedisClient(gg.db_name, gg.db_host, gg.db_port, gg.db_password)
    redis_con.put('abc')
    redis_con.put('123')
    # redis_con.put('123.115.235.221:8800')
    # redis_con.put(['123', '115', '235.221:8800'])
    # print(redis_con.getAll())
    # redis_con.delete('abc')
    # print(redis_con.getAll())

    # print(redis_con.getAll())
    redis_con.changeTable('raw_proxy')
    redis_con.pop()

    # redis_con.put('132.112.43.221:8888')
    # redis_con.changeTable('proxy')
    print(redis_con.get_status())
    print(redis_con.getAll())