from typing import Dict, List


def reverseStepStr(inputStr: str, n: int) -> str:
    '''
    请使用切片实现字符串逆序，且跳n格输出
    :param inputStr: 输入的字符串
    :return: 逆序且跳n格

    >>> reverseStepStr("01234567",2)
    '7531'
    '''
    pass


def deleteKeyOfMap(map: dict, key: str) -> Dict:
    '''
    从一个map中删除指定的key键值对，要求在原map上做操作
    :param map:
    :param key:
    :return:
    >>> deleteKeyOfMap({"a":1,"b":2,"c":3},"b")
    {'a': 1, 'c': 3}
    '''
    pass


def convertStrList2CharList(inputStr: List) -> List:
    """
    使用列表生成式将一个字符串列表中的每一个字符串打散后组合在一起，并去重
    :param inputStr:
    :return:

    >>> convertStrList2CharList(["Hello","World","Name"])
    ['r', 'm', 'a', 'o', 'd', 'N', 'e', 'l', 'H', 'W']
    """
    pass


def getnNumberGenerator(n: int):
    """
    返回一个能够产生n个自然数数的生成器
    :return:

    >>> generator=getnNumberGenerator(3)
    >>> print([x for x in generator])
    [0, 1, 2]
    """
    pass
