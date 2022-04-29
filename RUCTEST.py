import subprocess
import shutil
import os
import time as time

# Setting general environment variables
# Path variables for tools that are local to the build environment
PATH_AS45 = "C:/BrAutomation/AS45/"
PATH_AS = "C:/BrAutomation/AS/"
PATH_PVI45 = "C:/BrAutomation/PVI/V4.5/"
PATH_TEMP = "C:/Users/PC/Desktop/RUCpack/AS_Target_Simulink_Test_0413/"
PATH_SCRIPTS = "C:/Users/PC/Desktop/RUCpack/AS_Target_Simulink_Test_0413/Script"

# Project specific variables
# PATH_PROJECT = os.environ["WORKSPACE"] + '/'
PATH_PROJECT = "C:/Users/PC/Desktop/RUCpack/AS_Target_Simulink_Test_0413/"
NAME_PROJECT = "AS_Target_Simulink_Test.apj"
NAME_HMI = "ci-test"
CONFIG = "Config1"
CPU = "PC"
AR_VERSION = "D4.52"
AR_VERSION_STRING = "D0452"
CONFIG_ID = "ci-test"
CONFIG_VERSION = "1.0.0"

# Support functions
def CreateRUC():
	argList = []
	# C:\BrAutomation\AS45\Bin-en\BR.AS.RUCPackageCreator.exe
	argList.append(PATH_AS45 + "Bin-en/BR.AS.RUCPackageCreator.exe")
	# -o ***.zip
	argList.append("-o")
	argList.append(PATH_TEMP + "RUCPackage.zip")
	# -include ***
	argList.append("-include")
	argList.append(PATH_PROJECT + "Binaries/" + CONFIG + "/" + CPU + "/")
	# -f ***.lst
	argList.append("-f")
	argList.append(PATH_PROJECT + "Binaries/" + CONFIG + "/" + CPU + "/Transfer.lst")
	# -systemDirectory ***
	argList.append("-systemDirectory")
	argList.append(PATH_AS + "System/" + AR_VERSION_STRING + "/SG4/IA32/")
	# -d ***
	argList.append("-d")
	argList.append(PATH_PROJECT + "Temp/Transfer/" + CONFIG + "/" + CPU + "/FilesToTransfer/")
	# -configurationId ***
	argList.append("-configurationId")
	argList.append(CONFIG_ID)
	# -configurationVersion *.*.*
	argList.append("-configurationVersion")
	argList.append(CONFIG_VERSION)
	# -v **.**
	argList.append("-v")
	argList.append(AR_VERSION)
	# -S AR000
	argList.append("-S")
	argList.append("AR000")
	# -moduleSystem SAFE
	argList.append("-moduleSystem")
	argList.append("SAFE")
	# -OrderNumber ***
	argList.append("-OrderNumber")
	argList.append(CPU) # *** evidently this has to be the name of the PLC folder in the Configuration ***
	# -loggerModuleSize 819200
	argList.append("-loggerModuleSize")
	argList.append("819200")
	# -userPartitionSize 0
	argList.append("-userPartitionSize")
	argList.append("0")
	# -RuntimeType ARSim
	argList.append("-RuntimeType")
	argList.append("ARSim")
	# -compatibleCpuCode ARSim
	argList.append("-compatibleCpuCode")
	argList.append("")
	# -C "/IF=COM1 /BD=57600 /PA=2 /IT=20 /RS=0 /RT=1000 /AM=*"
	argList.append("-C")
	argList.append("/IF=COM1 /BD=57600 /PA=2 /IT=20 /RS=0 /RT=1000 /AM=*")
	subprocess.run(argList)
	
def OfflineInstall():
    argList = []
    argList2 = []
    # C:/BrAutomation/PVI/V4.5/PVI/Tools/PVITransfer/PVITransfer.exe
    argList.append(PATH_PVI45 + "PVI/Tools/PVITransfer/PVITransfer.exe")
    #argList2.append(PATH_PVI45 + "PVI/Tools/PVITransfer/PVITransfer.exe")
    # -C:/Users/PC/Desktop/RUCpack/AS_Target_Simulink_Test_0413/Script/NewPIL.pil
    argList.append("-silent" + "-" + PATH_SCRIPTS + "NewPIL.pil")
    #argList.append("-silent" + PATH_SCRIPTS + "OFFLINEINSTALL.pil")
    # -C:/Users/PC/Desktop/RUCpack/AS_Target_Simulink_Test_0413/Script/PVILog.txt
    argList.append("-" + PATH_SCRIPTS)
    #argList2.append("-"+"CreateARsimStructure"+"-"+"C:/Users/PC/Desktop/RUCpack/AS_Target_Simulink_Test_0413/RUCPackage.zip"+"C:/Users/PC/Desktop/PIL"+"Start=1")
    subprocess.run(argList)
    
def ARSIM():
    argList = []
    argList.append("C:/BrAutomation/AS45/Bin-en/BR.AS.FinalizeBuild.exe")
    argList.append("-" + PATH_SCRIPTS + "NewPIL.pil")


# STEP 4: Create RUC package
CreateRUC()
time.sleep(5);
OfflineInstall() # = ARSim 
print("Done")