'''
2048
'''
'''
# 把一个列表０元素放到末尾
# '''
import random
def get_zear_to_end(list01):
    '''
    调０元素到末尾
    :param lists: 列表
    :return: 返回新列表
    '''
    list02=[char for char in list01 if char!=0]
    for char in [char for char in list01 if char==0]:
        list02.insert(len(list02)+1,char)
    return list02
def get_and_number(lists):
    '''
    合并相邻元素
    :param lists:
    :return:
    '''
    get_zear_to_end(lists)
    for index in range(len(lists)-1):
        if lists[index]!=0 and lists[index] == lists[index + 1]:
            lists[index]+=lists[index + 1]
            lists[index + 1]=0
    return get_zear_to_end(lists)
def draw_2048_list(lists):
    '''
    将导入的列表　　打印为列表长度的方形
    :param lists:传入列表
    :return: 返回一个方形
    '''
    for line in range(len(lists)):
        for index in range(len(lists[line])):
            print(lists[line][index],end='\t')
        print()
def move_number_to_up(up_list):
    '''
    传入一个列表　　　取出列表的竖向正索引　　然后放入列表中　用相邻相加函数和０元素后移　形成一个新列表
    :param up_list: 传入列表
    :return:　返回一个新列表　利用画方形函数画出上移后的新列表
    '''
    for line in range(len(up_list)):
        list_merge = [up_list[index][line] for index in range(len(up_list[line]))]
        list_merge=get_and_number(list_merge)
        for index in range(len(up_list)):
            up_list[index][line]=list_merge[index]
    return up_list
def move_number_to_down(down_list):
    '''
    传入一个列表　　　取出列表的竖向反索引　　然后放入列表中　用相邻相加函数和０元素后移　形成一个新列表
    :param down_list: 传入列表
    :return: 返回一个新列表　利用画方形函数画出下移后的新列表
    '''
    for line in range(len(down_list)):
        list_merge = [down_list[len(down_list)-index-1][line] for index in range(len(down_list[line]))]
        list_merge=get_and_number(list_merge)
        for index in range(len(down_list)):
            down_list[len(down_list)-index-1][line]=list_merge[index]
    return down_list
def move_number_to_lift(lift_list):
    '''
    传入一个列表　　　取出列表的横向反索引　　然后放入列表中　用相邻相加函数和０元素后移　形成一个新列表
    :param lift_list: 传入列表
    :return: 返回一个新列表　利用画方形函数画出左移后的新列表
    '''
    for line in range(len(lift_list)):
        list_merge=[lift_list[line][index] for index in range(len(lift_list[line]))]
        list_merge = get_and_number(list_merge)
        for index in range(len(lift_list[line])):
            lift_list[line][index]=list_merge[index]
    return lift_list
def move_number_to_right(right_list):
    '''
    传入一个列表　　　取出列表的横向正索引　　然后放入列表中　用相邻相加函数和０元素后移　形成一个新列表
    :param right_list: 传入列表
    :return: 返回一个新列表　利用画方形函数画出右移后的新列表
    '''
    for line in range(len(right_list)):
        list_marge=[right_list[line][len(right_list[line])-1-index] for index in range(len(right_list[line]))]
        list_merge = get_and_number(list_marge)
        for index in range(len(right_list[line])):
            right_list[line][len(right_list[line]) - 1 - index]=list_merge[index]
    return right_list
def game_input(str_input,list_merge):
    if str_input=='w':
        move_number_to_up(list_merge)
    if str_input=='s':
        move_number_to_down(list_merge)
    if str_input=='a':
        move_number_to_lift(list_merge)
    if str_input=='d':
        move_number_to_right(list_merge)
def zero_random_2_4(list_target):
    '''
    传入列表　取出０元素放入临时列表　随机取一个随机生成２　４　返回新列表
    :param list_target: 传入列表
    :return: 返回新列表
    '''
    list_zero=[]
    for line in range(len(list_target)):
        for index in range(len(list_target)):
            if list_target[line][index] == 0:
                list_zero.append((line,index))#把０元素对应的索引放到元祖中后加到列表中
    temp_list=random.choice(list_zero)
    list_target[temp_list[0]][temp_list[1]]=random.choice([2,2,2,2,2,2,2,4])
    return list_target
def win_list(list_target):
    '''
    判断列表里索引有没有２０４８　　　有则胜利　　没有就判断有没有０　　没有则判断有没有相邻相同元素　　没有则失败
    :param list_target:
    :return:
    '''
    for line in range(len(list_target)):
        for index in range(len(list_target[line])):
            if list_target[line][index]==2048:
                return 2048
    for line in range(len(list_target)):
        for index in range(len(list_target[line])):
            if list_target[line][index]==0:
                return True
    for line in range(len(list_target)):
        for index in range(len(list_target[line])):
            if line==index:
                if list_target[line][index-1]==list_target[line][index] or list_target[line-1][index]==list_target[line][index]:
                    return True
            if line < index:
                if list_target[line][index]==list_target[line][index+1]:
                    return True
            if line > index:
                if list_target[line][index]==list_target[line-1][index]:
                    return True
    return False
def game_2048(list_target):
    win_list(list_target)#判断有没有２０４８
    draw_2048_list(list_target)#画出列表
    while 1:
        str_input=input('请输入wsad上下左右')
        if str_input not in ('w','s','a','d'):
            print('输入有误，重新输入')
        list_tmpe=list_target#给传入的列表重新赋值　　以便后面做比较
        list_target=game_input(str_input,list_tmpe)#输入对应的内容给到移动函数　
        if list_target==list_tmpe:
            continue
        list_target=zero_random_2_4(list_tmpe)#生成的新列表给到０元素生成２或者４函数中
        draw_2048_list(list_target)#随机生成２　或者４后画出来
        lists=win_list(list_target)#又把这个列表给到比较函数
        if lists == 2048:
            print('恭喜你赢了')
            break
        elif lists==False:
            print('你输了')
            break
list_target=[[0 ,0 ,0 ,0 ],[0 ,0 ,0 ,0 ],[0 ,0 ,0 ,0 ],[0 ,0 ,0 ,0]]
game_2048(list_target)