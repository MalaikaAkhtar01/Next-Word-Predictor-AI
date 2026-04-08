import tarfile
import os

# Aapki file ka bilkul sahi naam jo 'ls' mein nazar aaya
filename = 'aclImdb_v1 (1).tar.gz'

if os.path.exists(filename):
    print("Extracting dataset (aclImdb)... ")
    try:
        # 'r:gz' isliye taake .tar.gz file khul sakay
        with tarfile.open(filename, "r:gz") as tar:
            tar.extractall()
        print("Mubarak ho! 'aclImdb' folder extract ho gaya hai.")
    except Exception as e:
        print(f"Error: {e}")
else:
    print(f"Error: {filename} nahi mili. File ka naam check karein.")