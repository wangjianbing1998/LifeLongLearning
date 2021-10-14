from typing import Dict, List

def reverseStepStr(inputStr: str, n: int) -> str:
    '''
    请使用切片实现字符串逆序，且跳n格输出
    :param inputStr: 输入的字符串
    :return: 逆序且跳n格

    >>> reverseStepStr("01234567",2)
    '7531'
    '''
    return inputStr[::-n]



def deleteKeyOfMap(map: dict, key: str) -> Dict:
    '''
    从一个map中删除指定的key键值对，要求在原map上做操作
    这一题你回答的非常好，代码的执行效率也非常高，给你点一个赞赞
    我本来想考察的点是在边遍历map的时候边修改key，所以使用了list()将key都取出来建立了一个缓存，这样为了方便key值得修改和删除
    :param map:
    :param key:
    :return:
    >>> deleteKeyOfMap({"a":1,"b":2,"c":3},"b")
    {'a': 1, 'c': 3}
    '''
    for k in list(map.keys()):
        map.pop(k)
    return map


def convertStrList2CharList(inputStr: List) -> List:
    """
    使用列表生成式将一个字符串列表中的每一个字符串打散后组合在一起，并去重
    :param inputStr:
    :return:

    >>> convertStrList2CharList(["Hello","World","Name"])
    ['r', 'm', 'a', 'o', 'd', 'N', 'e', 'l', 'H', 'W']
    """
    return list(set([c for str in inputStr for c in str]))



def getnNumberGenerator(n: int):
    """
    返回一个能够产生n个自然数数的生成器
    :return:

    >>> generator=getnNumberGenerator(3)
    >>> print([x for x in generator])
    [0, 1, 2]
    """
    return (x for x in range(n))

