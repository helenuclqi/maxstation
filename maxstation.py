import os
import subprocess
import ctypes
import psutil

class MaxStation:
    def __init__(self):
        self.system_drive = os.getenv("SystemDrive", "C:")

    def disable_startup_programs(self):
        print("Disabling unnecessary startup programs...")
        try:
            startup_folder = os.path.join(self.system_drive, "ProgramData", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
            for program in os.listdir(startup_folder):
                os.remove(os.path.join(startup_folder, program))
            print("Startup programs disabled.")
        except Exception as e:
            print(f"Error disabling startup programs: {e}")

    def clean_temp_files(self):
        print("Cleaning temporary files...")
        temp_folder = os.path.join(self.system_drive, "Windows", "Temp")
        try:
            for temp_file in os.listdir(temp_folder):
                file_path = os.path.join(temp_folder, temp_file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print("Temporary files cleaned.")
        except Exception as e:
            print(f"Error cleaning temporary files: {e}")

    def optimize_memory(self):
        print("Optimizing memory usage...")
        try:
            ctypes.windll.psapi.EmptyWorkingSet(os.getpid())
            print("Memory optimized.")
        except Exception as e:
            print(f"Error optimizing memory: {e}")

    def update_system(self):
        print("Updating system...")
        try:
            subprocess.run(["powershell", "-Command", "Start-Process", "cmd", "/c", "sfc /scannow"], check=True)
            print("System updated.")
        except subprocess.CalledProcessError as e:
            print(f"Error updating system: {e}")

    def improve_performance(self):
        print("Improving system performance...")
        self.disable_startup_programs()
        self.clean_temp_files()
        self.optimize_memory()
        self.update_system()
        print("System performance improved.")

if __name__ == "__main__":
    maxstation = MaxStation()
    maxstation.improve_performance()