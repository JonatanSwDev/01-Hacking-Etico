This robot has been developed by EIPosgrados student Jonatan Gomez García.

Automation totally oriented towards the enumeration of possible vulnerabilities, with the aim of facilitating and speeding up part of the enumeration process automatically.

It is worth mentioning that the enumeration can be completed manually if the case requires it, allowing completely manual work.

To ensure proper functioning of the robot for NMAP scans it is important that the reports are placed in the Data/Script NMAP folder within the robot project.

To ensure the correct functioning of the robot, please generate NMAP reports as the output by executing the following commands.

sudo nmap -sV victim_ip > sV.txt
sudo nmap -sV -A --script=vuln victim_ip > Complete.txt

Alternatively, the desired report can be generated and the subsequent generation of the Python-based script to extract the desired information.

In order to run the robot, a UiPath account is required, along with the installation of UiPath Studio or UiPath Assistant.

Note that if you use UiPath Assistant, it is interesting that the data used by the robot is obtained from Orchestrator, and the project must be modified.

You need to have Python version 3.10 or any other version <= Python 3.11 installed.

It is necessary to have the Google Chrome browser installed.

You need to have .NET 5.0.17 installed:
https://dotnet.microsoft.com/en-us/download/dotnet/5.0

The modifications to be made to the code is the path to the python path in the Python Scope activity, located within Python_NMAP_Script.xaml

Automating NMAP results has two options: Extract data from PRION sources or not. Review the result of executing the NMAP vuln script carefully to decide the best option.
    #Example:
    #PRION:CVE-2015-5600	8.5	https://vulners.com/prion/PRION:CVE-2015-5600
    #CVE-2015-5600	8.5	https://vulners.com/cve/CVE-2015-5600
    #PRION:CVE-2020-16088	7.5	https://vulners.com/prion/PRION:CVE-2020-16088
    #PRION:CVE-2015-6564	6.9	https://vulners.com/prion/PRION:CVE-2015-6564
    #CVE-2015-6564	6.9	https://vulners.com/cve/CVE-2015-6564
    #CVE-2018-15919	5.0	https://vulners.com/cve/CVE-2018-15919