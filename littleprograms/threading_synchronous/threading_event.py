#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    使用threading.Event适合用于两个线程之间代码执行顺序的控制
'''
import threading

def DoWork(work, callback):
    def Task():
        print 'work begin...'
        work()
        print 'work done!'
        print 'callback begin...'
        callback()
        print 'callback done!'
    t = threading.Thread(target=Task)
    t.start()

def TestWorkAndDone():
    is_started = threading.Event()
    can_done = threading.Event()
    is_done = threading.Event()
    def Work():
        """it's not a good idea to use huge for loop here to kill time,
             because the start and end time are not under the control.
        """
        print '1'
        is_started.set()
        print '2'
        # block here until can_done.set() is called.
        can_done.wait(timeout=60)    # .await() in Java
        print '7'
    DoWork(work=Work, callback=lambda:is_done.set())
    print '3'
    # block here until is_started.set() is called.
    is_started.wait(timeout=60)
    print '4'
    if is_started.isSet():
        print 'SUCCESS: Work started'
    if is_done.isSet():
        print 'FAILD: Work hasnot done'
    print '5'
    can_done.set()    # Work() is unblock.
    print '6'
    # block here until callback() is called.
    # no need to use time.sleep(60) here.
    is_done.wait(timeout=60)
    if is_done.isSet():
        print '<mce:script type="text/javascript" src="http://hi.images.csdn.net/js/blog/tiny_mce/themes/advanced/langs/zh.js" mce_src="http://hi.images.csdn.net/js/blog/tiny_mce/themes/advanced/langs/zh.js"></mce:script><mce:script type="text/javascript" src="http://hi.images.csdn.net/js/blog/tiny_mce/plugins/syntaxhl/langs/zh.js" mce_src="http://hi.images.csdn.net/js/blog/tiny_mce/plugins/syntaxhl/langs/zh.js"></mce:script>SUCCESS: Work done'
# main
TestWorkAndDone()
