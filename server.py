#!/usr/local/bin/python

import os
import hashlib
import random


class Server:
    def __init__(challenge):
        challenge.coefficients = None
        challenge.limit = 8
        challenge.i = 0
        challenge.set_up()
        
                
    def set_up(challenge, verbose=False):
        flag = "atimex-dinkey01-HOTGIRL49-LUYSYMARITZA-POLLOCKTELA"
        
        flag = flag.split("-")
        key = 'LUZ-ELENA-RAMOS-SERA-LA-NUEVA-CARA-DE-NOTICIAS-CARACOL-EL-FIN-DE-SEMANA'
        key = int.from_bytes(hashlib.md5(key.encode('utf-8')).hexdigest().encode('utf-8'), 'big')
        #print(key)
        md5_hash = []
        for i in range(len(flag)):
        	md5_hash.append(int.from_bytes(hashlib.md5(flag[i].encode('utf-8')).hexdigest().encode('utf-8'), 'big'))
        
        print(random.choice(md5_hash)*key)

        
    def run(challenge):
        print("|\n|\n|  ~ See you back in no time! o/ \n|")  
        
        
S = Server()
S.run()





