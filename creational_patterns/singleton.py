# -*- coding: utf-8 -*-
"""
单例模式意图：
确保类有且只有一个对象被创建。
为对象提供一个访问点，以使程序可以全局访问该对象。
控制共享资源的并行访问。
"""


class Singleton(object):
    """
    该类完成两件事：
    1. 只允许Singleton类生成一个实例。
    2. 如果已经有一个实例了，我们会重复提供同一个对象。
    """
    def __new__(cls):
        """通过覆盖__new__方法（Python用于实例化对象的特殊方法）来控制对象的创建。"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print('Object created', s)
s1 = Singleton()
print('Object created', s1)


class Singleton2:
    """懒汉式实例化：确保在实际需要时才创建对象，是一种节约资源并仅在需要时才创建它们的方式。"""
    __instance = None

    def __init__(self):
        if not Singleton2.__instance:
            print("__init__ method called...")
        else:
            print('Instance already created:', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton2()
        return cls.__instance


ss = Singleton2()
print("Object created", Singleton2.getInstance())
ss1 = Singleton2()
ss2 = Singleton2()

