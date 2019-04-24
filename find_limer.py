'''
顺序查找
'''
def linear(value,key):
    '''
    查找函数  顺序查找
    :param value: 要查找的对象
    :param key: 带查找的内容
    :return:
    '''
    for i in range(len(value)):
        if value[i] == key:
            return i#查找成功,返回索引
    return -1#查找失败返回非法索引
if __name__=="__main__":
    value = [1,9,8,2,4,3,5,7,6,10,12,11,13]
    key=7#待查数据
    if linear(value,key) == -1:
        print("over")
    else:
        print("ok",linear(value,key))



'''
二分法  递归实现查找
'''
def binary(value,key,lift,right):
    '''
    递归查找
    :param value: 原始数据 升序数据
    :param key: 待查找数据
    :param lift: 当前查找范围左侧数据对应索引
    :param right: 当前查找范围右侧数据对应索引
    :return:
    '''
    if lift > right:
        return -1#查找结束返回非法索引
    #获取中间值
    middle = (lift + right) // 2
    #比较目标数和中间只对应的数据
    if value[middle] == key:
        return middle
    elif value[middle] > key:
        #中间数据大于目标值在左侧查找
        #继续在左侧重复查找
        #查找范围缩小,左侧不变,右侧中间值小1
        return binary(value,key,lift,middle-1)
    else:
        #中间数据小目标值
        #在右侧继续查找
        #查找范围缩小,右侧不变,左侧是中间值,从中间值+1开始
        return binary(value,key,middle+1,right)

if __name__ == "__main__":
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    key = 6  # 待查数据
    request = binary(value, key, 0, len(value) - 1)
    if request == -1:
        print("over")
    else:
        print("ok", request)
'''
二分法查找  循环实现查找
'''
def binary(value,key):
    '''
    循环查找
    :param value:原始数据
    :param key:待查找的数据
    :return:
    '''
    #获取左右侧数据对应索引
    lift = 0
    right = len(value)-1
    #如果存在合法范围就继续
    while lift <= right:
        middle = (lift + right) // 2#去中间值
        #判断是否查找到
        if value[middle] == key:
            return middle
        elif value[middle] > key:
            right =middle - 1
        else:
            lift = middle +1
    return -1



if __name__=="__main__":
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    key=6#待查数据
    request = binary(value,key)
    if  request ==-1:
        print("over")
    else:
        print("ok",request)