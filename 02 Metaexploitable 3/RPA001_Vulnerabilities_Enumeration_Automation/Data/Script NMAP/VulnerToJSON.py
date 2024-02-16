import re
import json

# Texto completo con las secciones y los CVEs
with open("./Complete.txt", "r") as archivo:
    texto_completo = archivo.read()

# Lista de secciones
with open("./sV.txt", "r") as archivo:
    sv = archivo.read()

# Buscar los puertos y sus versiones
secciones = re.findall(r'(\d+\/tcp\s+open+\s+\S+\s+.+)', sv)

# Dividir el texto en secciones usando expresiones regulares
patron_seccion = r"\d+\/tcp\s+.*?(?=\d+\/tcp|\Z)"
secciones_encontradas = re.findall(patron_seccion, texto_completo, re.DOTALL)

# Crear un diccionario para almacenar las secciones y su contenido
diccionario_secciones = {}
for i, seccion in enumerate(secciones):
    diccionario_secciones[seccion] = []
    if i < len(secciones_encontradas):
        contenido = secciones_encontradas[i].strip()
        # Utilizar expresiones regulares para extraer los CVEs y sus enlaces
        
        # Dividir el contenido por líneas
        lineas_contenido = contenido.split('\n')
        
        #Generar variables auxiliares
        complete_data = {"CVE":"","URL":""}
        exploit_URL = []
        
        #Recorrer cada linea individualmente para mejor control
        for linea in lineas_contenido:
            #Buscar el comienzo de un nuevo CVE 
            cve_url = re.search(r'(CVE-\d+-\d+)\s+\d+\.\d+\s+(https://vulners\.com/cve/\1)', linea)
            #En caso de haber encontrado una nuevo CVE
            if not cve_url == None :
                #Además si el CVE no es el primero encontrado se guarda toda la información recogida para después procesar el siguiente.
                if not complete_data["CVE"] == "" :
                    complete_data["EXPLOIT"] = " | ".join(exploit_URL)
                    diccionario_secciones[seccion].append(complete_data)
                #Se guardan los datos encontrados para la nueva sección
                complete_data ={"CVE":cve_url.group(1),"URL":cve_url.group(2)}
                exploit_URL = []
                
            #En caso de que no sea una nueva sección se buscan los exploits asociados al CVE
            else:
                exploit = re.search(r'https://[^*\s]+(?=\s*\*EXPLOIT\*)', linea)
                if not exploit == None :
                    exploit_URL.append(exploit.group(0))
        #Por último se guarda la información del último CVE encontrado ántes de comenzar con la siguiente sección
        if not complete_data["CVE"] == "":
            complete_data["EXPLOIT"] = " | ".join(exploit_URL)
            diccionario_secciones[seccion].append(complete_data)
                    
# Guardar el diccionario como un archivo JSON
with open('secciones_cves.json', 'w') as archivo_json:
    json.dump(diccionario_secciones, archivo_json, indent=4)
