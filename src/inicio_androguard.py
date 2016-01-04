import sys
import json

from optparse import OptionParser
from androguard.core import *
from androguard.core.analysis.analysis import *
from androguard.decompiler.decompiler import *
from androguard.session import Session
from androguard.util import *
from androguard.misc import *

import os
import hashlib
import xml.etree.ElementTree as ET


class Veneno(object):
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino
        self.hash_md5 = ""
        self.hash_sha256 = ""
        self.manifest = ""
        self.bicho = None
        self.nombre = None

    def estaticos(self):
        self.hash_sha256 = hashlib.sha256("muestras/" + self.origen).hexdigest()
        self.hash_md5 = hashlib.md5("muestras/" + self.origen).hexdigest()
        #print "SHA-256: " + str(self.hash_sha256)
        #print "MD5: " + str(self.hash_md5)
        origen = "../" \
                 "muestras/" + self.origen
        destino = "muestras/" + self.destino
        a = APK(origen)
        self.bicho = a.get_permissions()
        self.nombre = a.get_package()
    # Utiliza la libreria para desempaquetar y decodificar los apk
    def desempaquetar(self):
        codigo = "sh src/decompiler.sh d -f muestras/" + self.origen + " -o muestras/" + self.destino
        result = os.system(codigo)

   # def permisos(self):
        #for permisos in self.bicho:
        #       print (permisos)
        #print(self.nombre)

def jdefault(o):
    return o.__dict__

sample = Veneno(sys.argv[1], sys.argv[2])
# sample.desempaquetar()
sample.estaticos()
#sample.permisos()

print(json.dumps(sample,default=jdefault))


