在运行一个python程序时，会首先将当前运行的程序的工作目录添加的python的路径中去，即sys.path中去；
因此要想在b.py中引用a.py中的内容需要将a.py的工作目录添加到sys.path中去;
