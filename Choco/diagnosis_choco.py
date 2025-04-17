import subprocess
import os
import glob
import shutil

def get_linux_diagnosis(configuration_file_path):
    try:
        # change feature model file according to the feature model to be diagnosed
        # (e.g., linux-2.6.33.3.xml, busybox-1.18.0.xml, ea2468.xml, REAL-FM-4.sxfm)
        jar_path = os.path.join("LinuxConfiguration", "fm_diagnosis.jar")
        fm_path = os.path.join("LinuxConfiguration", "REAL-FM-4.sxfm")
        log_dir = os.path.join("LOGS")  # Change this to your desired log directory
        os.makedirs(log_dir, exist_ok=True)
        result = subprocess.run(["java", f"-Dlog.dir={log_dir}", "-jar",jar_path, fm_path, configuration_file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # move the logs to LOGS folder
        for log_file in glob.glob("*.log"):
            shutil.move(log_file, os.path.join(log_dir, log_file))
        for zip_file in glob.glob("*.zip"):
            shutil.move(zip_file, os.path.join(log_dir, zip_file))
        for tmp_file in glob.glob("*.tmp"):
            shutil.move(tmp_file, os.path.join(log_dir, tmp_file))
        # print(result.stdout)
        return result
    except:
        print('Subprocess did not answer! Continue with another try...')
        return None


