Python Code Style GuideLine
============================


总体布局 
--------------

* 遵循 :pep:`8`
* 缩进:

  4个空格

* 单行最大字数:

  79个字符

* 长语句:

  用反斜杠`\`来断句, 和最后一个`.`, `=` 或者以4个空格缩进

  .. code-block:: python

    this_is_a_very_long(function_call, 'with many parameters') \
        .that_returns_an_object_with_an_attribute

    MyModel.query.filter(MyModel.scalar > 120) \
                 .order_by(MyModel.name.desc()) \
                 .limit(10)

  如果断句的语句中有括号和逗号, 和括号对齐

  .. code-block:: python

    this_is_a_very_long(function_call, 'with many parameters',
                        23, 42, 'and even more')

  对于长列表(lists)或者元组(tuples), 在中括号和逗号后断句::

    items = [
        'this is the first', 'set of items', 'with more items',
        'to come in this line', 'like this'
    ]

* 空行:

  全局方法和类都用两行空行来分隔，其他都用一行。::

    def hello(name):
        print 'Hello %s!' % name


    def goodbye(name):
        print 'See you %s.' % name


    class MyClass(object):
        """This is a simple docstring"""

        def __init__(self, name):
            self.name = name

        def get_annoying_name(self):
            return self.name.upper() + '!!!!111'

表达式和语句
-------------

* 一般空格原则

  - 一元运算符以及括号内侧不用空格 (e.g.: ``-``, ``~`` etc.)
  - 二元运算符号使用空格 

  Good::

    exp = -1.05
    value = (item_value / item_count) * offset / exp
    value = my_list[index]
    value = my_dict['key']

  Bad::

    exp = - 1.05
    value = ( item_value / item_count ) * offset / exp
    value = (item_value/item_count)*offset/exp
    value=( item_value/item_count ) * offset/exp
    value = my_list[ index ]
    value = my_dict ['key']

* 不要用常量与变量做比较， 通常是变量与常量做比较

  Good::

    if method == 'md5':
        pass

  Bad::

    if 'md5' == method:
        pass

* 比较

  - 比较任意类型: ``==`` 和 ``!=``
  - 对于单个变量用 ``is`` 和 ``is not`` (eg: ``foo is not
    None``)
  - 不要用 `True` 或者 `False` 来比较(比如不要 ``foo == False``,
    应该用 ``not foo``)

* 是否包含检查:

  用 ``foo not in bar`` 来代替 ``not foo in bar``

* 实例检查:

  用 ``isinstance(a, C)`` 来代替 ``type(A) is C``, 但是一般应该避免实例检查


命名约定
----------

- 类名: ``CamelCase``, 缩写词保持大写 (``HTTPWriter`` 而不是 ``HttpWriter``)
- 变量名: ``lowercase_with_underscores``
- 方法和函数名: ``lowercase_with_underscores``
- 常量名: ``UPPERCASE_WITH_UNDERSCORES``
- 预先编译的正则表达式: ``name_re``

"单下划线" 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
"双下划线" 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。

函数和方法的参数:
  - 类方法: ``cls`` 为第一个参数
  - 实例方法: ``self`` 为第一个参数
  - 属性中的 `lambdas` 表达式第一个参数替代 ``x``
    像 ``display_name = property(lambda x: x.real_name or x.username)``


文档字符串
----------
  格式: reStructuredText
  用三引号引起来::

    def foo():
        """This is a simple docstring"""


    def bar():
        """This is a longer docstring with so much information in there
        that it spans three lines.  In this case the closing triple quote
        is on its own line.
        """

  模块头包含一个uf8 encoding的声明和一个标准的文档字符串::

    # -*- coding: utf-8 -*-
    """
        package.module
        ~~~~~~~~~~~~~~

        A brief description goes here.

    """



注释
--------

::

    class User(object):
        #: the name of the user as unicode string
        name = Column(String)
        #: the sha1 hash of the password + inline salt
        pw_hash = Column(String)


Links
------

- `PEP8 <http://www.python.org/dev/peps/pep-0008/>`_ Style Guide for Python Code
- `Flask Styleguide <http://flask.pocoo.org/docs/styleguide/>`_
- `Google Python Style Guide <http://google-styleguide.googlecode.com/svn/trunk/pyguide.html>`_
