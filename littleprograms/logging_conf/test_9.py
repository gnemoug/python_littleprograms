#!/usr/bin/python
#-*-coding:utf8-*-
import logging.config  

logging.config.fileConfig("logging.conf")   

log = logging.getLogger('simpleExample')  

log.debug("log debug")  
log.info("log info")  
log.warning("log warning")  
log.error("log error")  
log.critical("log critical")  
