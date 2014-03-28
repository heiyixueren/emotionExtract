#-*- coding: utf-8 -*-
import sqlite3
import os
if __name__ == '__main__':
    curPath = os.path.dirname(__file__)
    dbFile = os.path.join(curPath, 'sqlite.db').replace('\\','/')
    cx= sqlite3.connect(dbFile)
    cu = cx.cursor()
    cu.execute("delete from emotionExtract_wordSet where wordname='说'")
    
    cx.commit()