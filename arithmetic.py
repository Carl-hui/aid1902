'''
算法模块，主要有查询算法，排序算法
'''
class ALG:
    @staticmethod
    def find(value,key):
        '''
        顺序查找
        :param value:目标数据
        :param key: 要查找的数据
        :return:
        '''
        for index in value:
            if index == key:
                return True
        return False
    @staticmethod
    def brnary(value,key,lift,right):
        '''
        二分法查找 递归方法
        :param value: 目标数据
        :param key: 查找的数据
        :param lift: 最左边下标
        :param right: 最右边下标
        :return: 返回索引
        '''
        if lift > right:
            return False
        middle = (lift + right) // 2
        if value[middle] == key:
            return middle
        elif value[middle] > key:
            return ALG.brnary(value,key,lift,middle-1)
        else:
            return ALG.brnary(value,key,middle+1,right)
    @staticmethod
    def ascending(value):
        '''
        冒泡排序
        :param value:目标数据
        :return:
        '''
        for index in range(len(value)):
            status = False
            for item in range(len(value)-1):
                if value[item] > value[item+1]:
                    value[item],value[item+1] = value[item+1],value[item]
                    status = True
            if status == False:
                break
    @staticmethod
    def insert_sort(value):
        '''
        插入排序
        :param value:
        :return:
        '''
        for index in range(1,len(value)):
            temp = value[index]
            insert  =index
            for item in range(index-1,-1,-1):
                if value[item] > temp:
                    value[item+1] = value[item]
                    insert = item
                else:
                    insert= item +1
            value[insert] = temp
    @staticmethod
    def quict(value):
        '''
        快速排序
        :param value:
        :return:
        '''
        temp=value[0]
        if len(value) <2:
            return value
        smaller = [i for i in value if i < temp]
        bigger = [i for i in value if i > temp]
        eq = [i for i in value if i == temp]
        return ALG.insert_sort(smaller) + eq +ALG.insert_sort(bigger)
