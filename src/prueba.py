 @manifest = Document.new(File.new("muestras/"+@destino+"/AndroidManifest.xml"))
                xml = @manifest
                xml.elements.each("manifest/uses-permission"){
                        |permiso| puts "Permiso: " + permiso.attributes["android:name"]
                }
                xml.elements.each("manifest/uses-permission-sdk-m"){
                        |permiso| puts "Permiso android M: " + permiso.attributes["android:name"]
                }

                @paquete = xml.elements["manifest"].attributes["package"]
                @buildversion = xml.elements["manifest"].attributes["platformBuildVersionCode"]
                @buildname = xml.elements["manifest"].attributes["platformBuildVersionName"]
                puts "Nombre paquete: " + @paquete
                puts "Version construccion: " + @buildversion
                puts "Version plataforma: " + @buildname
