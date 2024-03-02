Este robot ha sido desarrollada por el alumno de EIPosgrados Jonatan Gomez García.

La automatización totalmente orientada a la enumeración de posibles vulnerabilidades, con el objetivo de facilitar y agilizar parte del proceso de enumeración de forma automática. 

Cabe mencionar que la enumeración se puede completar de forma manual si así lo requiere el caso, permitiendo un trabajo completamente manual.

Para asegurar el correcto funcionamiento del robot para los escaneos de NMAP es importante que los informes se coloquen en la carpeta Data/Script NMAP dentro del proyecto del robot.

Para asegurar el correcto funcionamiento del robot se ruega que la generación de informes de NMAP sea el output mediante la ejecución de los siguientes comandos.

sudo nmap -sV ip_victima > sV.txt
sudo nmap -sV -A --script=vuln ip_victima > Complete.txt

Alternativamente se puede generar el informe deseado y la posterior generación del script basado en Python para extraer la información deseada.

Para poder ejecutar el robot es necesaria una cuenta de UiPath, junto con la instalación de UiPath Studio o UiPath Assistant.

Tenga en cuenta que si usa UiPath Assistant es interesante que los datos usados por el robot se obtengan de Orchestrator, debiendo modificar el proyecto.

Es necesario tener instalada la versión 3.10 de Python o cualquier otra <= Python 3.11.

Es necesario tener instalado el navegador de Google Crhome.

Es necesario tener .NET 5.0.17 instalado:
https://dotnet.microsoft.com/en-us/download/dotnet/5.0

Las modificaciones que se han de realizar en el código es la ruta hacia el path de python en la actividad Python Scope, ubicada dentro de Python_NMAP_Script.xaml

La automatización de los resultados de NMAP cuenta con dos opciones: Extraer datos de fuentes PRION o no hacerlo. Revise bien el resultado de la ejecución del script vuln de NMAP para decidir la mejor opción.
    #Ejemplo:
    #PRION:CVE-2015-5600	8.5	https://vulners.com/prion/PRION:CVE-2015-5600
    #CVE-2015-5600	8.5	https://vulners.com/cve/CVE-2015-5600
    #PRION:CVE-2020-16088	7.5	https://vulners.com/prion/PRION:CVE-2020-16088
    #PRION:CVE-2015-6564	6.9	https://vulners.com/prion/PRION:CVE-2015-6564
    #CVE-2015-6564	6.9	https://vulners.com/cve/CVE-2015-6564
    #CVE-2018-15919	5.0	https://vulners.com/cve/CVE-2018-15919