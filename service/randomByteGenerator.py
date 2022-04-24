

import random

from flask import jsonify


class randomByteGenerator:
    def __init__(self,num,type):
        self.num = num
        self.type = type
    
    def geneRByte(self):
        switcher ={
                'binary': [(bin(random.randint(-(int(255)),int(255))).replace("0b", "")) for i in range(self.num) ],
                'octal' : [(oct(random.randint(-(int(255)),int(255))).replace("0o", "")) for i in range(self.num) ],
                'hexa' : [(hex(random.randint(-(int(255)),int(255))).replace("0x", "")) for i in range(self.num)],
                'decimal' : [(random.randint(-(int(255)),int(255))) for i in range(self.num)],
                'default' : [(random.randint(-(int(255)),int(255))) for i in range(self.num)]
            } 
        return jsonify(switcher.get(self.type, switcher['default']))