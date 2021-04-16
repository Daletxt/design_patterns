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


