import os
import configparser

class Config(object):
    def __init__(self, filename):
        self.__conf = configparser.ConfigParser()
        self.__conf.read(filename, encoding='GBK')

    def getConfig(self, section, item):
        try:
            itemDict = dict(self.__conf.items(section))
            if item in itemDict:
                return itemDict[item]
            return None
        except Exception as e:
            return None
        


if __name__ == '__main__':
    conf = Config(os.getcwd() + '/conf/conf.ini')
    print(conf.getConfig('APP', 'name'))
    print(conf.getConfig('USER', 'name'))
    print(conf.getConfig('TITLE', 'title1'))
    print(conf.getConfig('TITLE', 'title2'))
    print(conf.getConfig('TITLE', 'title3'))