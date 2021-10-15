from typing import List


class Item:
    def __init__(self, name:str, count:str, id:int):
        self.name = name
        self.count = count
        self.id = id

    def __repr__(self):
        return (f"Item({self.name},{self.count},{self.id})")


def filterMapReduce(items: List[Item]) -> int:
    """
    1. 过滤出来所有id>2的Item
    2. 将所有符合条件的Item的count转化为int
    3. 返回所有符合条件的Item的count之和
    要求需要使用filter和map、reduce高级的方法
    >>> itemList=[Item(str(i+10),str(i+100),i) for i in range(5)]
    >>> print(filterMapReduce(itemList))
    207
    :return:
    """
    pass

def sortedFunction(items:List[Item]) -> List[int]:
    """
    给输入的items进行排序，按照id逆序排序
    :param items:
    :return:
    >>> sortedFunction([Item(str(i+10),str(i+100),i) for i in range(5)])
    [4, 3, 2, 1, 0]
    """
    pass


def decoratorDemo():
    """
    实现自动给一个函数统计执行时间的方法
    :return:
    """
    pass

@decoratorDemo
def testDecoratorDemo():
    print(f"testDecoratorDemo runing")




def testPartitionDemo(f):
    """
    给一个两个参数的函数
    返回一个偏函数，其中第一个参数设置为10
    >>> f=lambda x,y:x+y
    >>> f10=testPartitionDemo(f)
    >>> f10(2)
    12
    :return:
    """
    pass

