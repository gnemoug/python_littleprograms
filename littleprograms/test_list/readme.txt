有这么一个列表：

original = [
    ('lilei', 24), ('hanmeimei', 23), ('dajiangyou', 23),
    ('jiaoshou', 1), ('zhuanjia', 1), ('mcshitou', 26),
    ('danteng', 25), ('jiyou', 26), ('papapa', 20), ('jiji', 26),
]
要求转换为：

[
('papapa', 20), ('lilei', 24), ('danteng', 25), 
(['jiaoshou', 'zhuanjia'], 1), (['dajiangyou', 'hanmeimei'], 23), 
(['jiji', 'jiyou', 'mcshitou'], 26)
]
原始列表中的元素为 元组，元组第一项为 人名，第二项为年龄。

转换规则如下：

1，按照 年龄 归类，将 年龄相同的 人名 合并到一起。
2，转换完的列表 首先按照 人数 来排序，只有一个人的排前面，人数多的排后面。
3，如果这个年龄的只有一个人，那么还是按照 字符串 的形式表示此人名
4，如果这个年龄有多个人，那么用列表的形式表示这些人名，并且列表元素按照人名进行排序。
