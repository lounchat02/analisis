import sys
import hashlib

class Veneno(object):
	def __init__(self,origen,destino):
		self.origen = origen
		self.destino = destino
#		manifest
		self.hash_md5 = ""
#		hash_sha256
#		paquete
#		buildversion
#		builname
	
        def estaticos(self):
#                self.hash_sha256 = Digest::SHA256.hexdigest File.read "muestras/" + @origen
		print "muestras/" + str(self.origen)
		self.hash_md5 = hashlib.md5("muestras/" + self.origen).hexdigest()
#                puts "SHA-256: " + @hash_sha256
                print "MD5: " + str(self.hash_md5)

##Utiliza la libreria para desempaquetar y decodificar los apk
"""        def desempaquetar(self):
                codigo = "sh src/decompiler.sh d -f muestras/"+@origen+" -o muestras/"+@destino
                result = exec(codigo)
"""
sample = Veneno(sys.argv[1],sys.argv[2])
#sample.desempaquetar
sample.estaticos()
#sample.permisos



	
