#!/usr/bin/python
#-*- coding:utf-8 -*-

import gettext

t = gettext.translation('example','locale',fallback=True)

_ = t.ugettext
print "DenormalizedField "*10
class DenormalizedField(object):
    def __init__(self, manager, *args, **kwargs):
        self.manager = manager
        self.filter = (args, kwargs)

print "ModelBase "*10
class ModelBase(type):
    """
    Metaclass for all models.
    """
    print "global"
    #使用name, bases, attrs是为了利用type()函数创建类
    #type is essentially a dynamic form of the class statement.
    def __new__(cls, name, bases, attrs):
        print 'bases:',bases
        print "in modelbase"
        super_new = super(ModelBase, cls).__new__
        parents = [b for b in bases if isinstance(b, ModelBase)]
        if not parents:
        #因为Modle是用__metaclass__实现的，他的类调用本身相当于一个ModelBase的实例
        #在OSQA中，他是继承了此函数，则直接返回，不做任何特殊处理
            # If this isn't a subclass of Model, don't do anything special.
            return super_new(cls, name, bases, attrs)
        #此处的name指的是最初导致调用的类名称，bases是直接的父类，而非间接父类,而且若此处参数是*args,**kwargs,则
        # Create the class.
        else:
            cls.hello='hello'
            return super_new(cls, name, bases, attrs)

print "BaseMetaClass "*10
class BaseMetaClass(ModelBase):
    to_denormalize = []

    def __new__(cls, *args, **kwargs):
        new_cls = super(BaseMetaClass, cls).__new__(cls, *args, **kwargs)
        print "in BaseMetaClass"
#此时是在__new__中写方法,所以应该调用BaseMetaClass
        BaseMetaClass.to_denormalize.extend(
            [(new_cls, name, field) for name, field in new_cls.__dict__.items() if isinstance(field, DenormalizedField)]
        )

        return new_cls
print "NodeMetaClass "*10
class NodeMetaClass(BaseMetaClass):
    types = {}

    def __new__(cls, *args, **kwargs):
        new_cls = super(NodeMetaClass, cls).__new__(cls, *args, **kwargs)
        print "in NodeMetaClass new"
        return new_cls
print "Model "*10
class Model(object):
    __metaclass__ = ModelBase
    _deferred = False
    print "in model"
    print __metaclass__
    
    def __init__(self, *args, **kwargs):
        model = 'model'
print "NodeContent "*10
class NodeContent(Model):
    print "in NodeContent"
    title      = "title"
#可以充当属性使用
    def __new__(cls,*args,**kwargs):
        print "in NodeContent new"
#        return 2
        return super(NodeContent,cls).__new__(cls,*args,**kwargs)

    def __init__(self, *args, **kwargs):
        super(NodeContent, self).__init__(*args, **kwargs)
        print "in NodeContent init"
    @property
    def user(self):
        return self.author

    @property
    def html(self):
        return self.body

    @classmethod
    def aclassmethod(cls):
        print "in NodeContent classmethod"

    @property
    def headline(self):
        return self.title

    class Meta:
        abstract = True
        app_label = 'forum'
print "BaseModel "*10
class BaseModel(Model):
    a = 1
    print "in BaseModel"
    def __new__(cls,*args,**kwargs):
        print "in BaseModel new"
#        return 1
        return super(BaseModel,cls).__new__(cls,*args,**kwargs)
    __metaclass__ = BaseMetaClass
#注意此时既有__metaclass__,又有基类models.Model,则会首先调用基类，使其具有基类的属性,然后调用__metaclass__去创建类

    class Meta:
        abstract = True
        app_label = 'forum'
#因为此文件名不为models.py
    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        print "in BaseModel init"
print "Node "*10
class Node(BaseModel, NodeContent):
    def __new__(cls,*args,**kwargs):
        print "in Node new"
        return super(Node,cls).__new__(cls,*args,**kwargs)
    __metaclass__ = NodeMetaClass
#__metaclass__是在调用类Node时就执行，eg:a = Node，就返回调用NodeMetaClass的__new__,和__init__的对象，所以一般含有__metaclass__的类都不含有__init__函数，若想进一步使用a = Node(),则此时调用的是NodeMetaClass的__call__函数，若不含__metaclass__则，在调用执行Node时，不执行任何函数(eg:__init__和__new__)
#注意此处既有继承又有控制对象产生过程的__metaclass__，则先执行父类，但不执行任何函数(eg:__init__和__new__)
#__metaclass__用来控制一个对象的创造过程（非初始化），而__init__函数用来控制对象的初始化过程,由__new__返回的对象来判断是调用哪一个对象的__init__函数
    node_type            = 'node'
    comment_count = DenormalizedField("children", node_type="comment", canceled=False)
    flag_count = DenormalizedField("flags")

    friendly_name = _("post")
    def __unicode__(self):
        return self.headline

    @classmethod
    def get_type(cls):
        return cls.__name__.lower()
print "Question "*10
class Question(Node):

    def __new__(cls,*args,**kwargs):
        print "in Question new"
        return super(Question,cls).__new__(cls,*args,**kwargs)

    class Meta(Node.Meta):
        proxy = True
    print "in Question"
    answer_count = DenormalizedField("children", node_type="answer")
    accepted_count = DenormalizedField("children", node_type="answer", marked=True)
    favorite_count = DenormalizedField("actions", canceled=False)

    @property
    def closed(self):
        return self.nis.closed

print "&"*50
a = Question()
print dir(a)
print type(a)
b = Question()
print id(a)
print id(b)

