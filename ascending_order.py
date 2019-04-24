'''
冒泡排序
'''
def ascending(target):
    '''
    冒泡排序  在循环前比较时设置默认初始标识位,
    :param target:目标数据
    :return:
    '''
    for item in range(len(target)):#每次走访的数据
        flag = False#设置初始默认标识位是False
        for index in range(len(target)-1):#对应走访数据比较的次数
            if target[index] > target[index+1]:
                target[index],target[index+1] = target[index+1],target[index]
                flag = True#交换flag为True
        if flag == False:#如果每次比较一轮后没有交换数据就退出此次循环,不在比较下去
            break
    print("hjs",item+1)

if __name__=="__main__":
    target = [198,1, 6,8,7,5,4,3,2,0,88,66,55,44,77,99]
    ascending(target)
    print(target)