import sys
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

    def estaticos(self):
        self.hash_sha256 = hashlib.sha256("muestras/" + self.origen).hexdigest()
        self.hash_md5 = hashlib.md5("muestras/" + self.origen).hexdigest()
        print "SHA-256: " + str(self.hash_sha256)
        print "MD5: " + str(self.hash_md5)

#Utiliza la libreria para desempaquetar y decodificar los apk
    def desempaquetar(self):
        codigo = "sh src/decompiler.sh d -f muestras/" + self.origen + " -o muestras/" + self.destino
        result = os.system(codigo)

    def permisos(self):
        self.manifest = ET.parse('muestras/' + self.destino + '/AndroidManifest.xml')
        root = self.manifest.getroot()
        print root.tag


sample = Veneno(sys.argv[1], sys.argv[2])
#sample.desempaquetar()
sample.estaticos()
sample.permisos()
