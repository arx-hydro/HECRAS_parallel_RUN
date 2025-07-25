# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 09:12:45 2025

@author: Siamak.Farrokhzadeh
"""

import os
import time
import shutil
import tempfile
from multiprocessing import Process
import win32com.client
import pythoncom

def run_hecras_plan(project_path, plan_name):
    try:
        pythoncom.CoInitialize()

        ras = win32com.client.Dispatch("RAS66.HECRASController")
        ras.ShowRas()

        print(f"Opening project: {project_path}")
        ras.Project_Open(project_path)
        time.sleep(5)

        print(f"Setting plan: {plan_name}")
        ras.Plan_SetCurrent(plan_name)

        print(f"Running simulation: {plan_name}")
        ras.Compute_CurrentPlan()

        while ras.Compute_Complete() == 0:
          print(f"Waiting for plan: {plan_name} to complete...")
          time.sleep(5)

        print(f"Simulation completed for plan: {plan_name}")
        ras.Project_Close()

    except Exception as e:
        print(f"Error running plan '{plan_name}': {e}")
        import traceback
        traceback.print_exc()

def copy_project_to_temp(original_project_path):
    original_folder = os.path.dirname(original_project_path)
    temp_dir = tempfile.mkdtemp(prefix="HECRAS_")
    print(f"Copying project to temporary folder: {temp_dir}")

    # Copy all files from original project folder
    for item in os.listdir(original_folder):
        s = os.path.join(original_folder, item)
        d = os.path.join(temp_dir, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

    temp_project_path = os.path.join(temp_dir, os.path.basename(original_project_path))
    return temp_project_path

def copy_results_to_main_project(temp_project_path, main_project_dir, suffix):
    important_exts = ['p', 'u', 'x', 'g', 'c', 'b', 'bco', 'dss', 'ic.o']
    temp_dir = os.path.dirname(temp_project_path)
    
    for file in os.listdir(temp_dir):
        for ext in important_exts:
            expected_suffix = f".{ext}{suffix}"
            if file.lower().endswith(expected_suffix.lower()):
                src = os.path.join(temp_dir, file)
                dst = os.path.join(main_project_dir, file)
                shutil.copy2(src, dst)
                print(f"Copying {file} → {main_project_dir}")
        
        if file.endswith(f".p{suffix}.hdf"):
            src = os.path.join(temp_dir, file)
            dst = os.path.join(main_project_dir, file)
            shutil.copy2(src, dst)
            print(f"Copying {file} → {main_project_dir}")        
            
def run_simulations():
    # Original project path and plan names
    original_project_path = r"C:\Test\PRtest1.prj"
    main_project_dir = os.path.dirname(original_project_path)
    plan1 = "plan01"
    plan2 = "plan02"
    suffix1 = "01"
    suffix2 = "02"

    # Copy project into two separate temp folders
    project_path_1 = copy_project_to_temp(original_project_path)
    project_path_2 = copy_project_to_temp(original_project_path)

    # Create two separate processes for the plans
    p1 = Process(target=run_hecras_plan, args=(project_path_1, plan1))
    p2 = Process(target=run_hecras_plan, args=(project_path_2, plan2))

    # Start and wait for both
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Both simulations completed.")
    # Copy results back to main project folder
    copy_results_to_main_project(project_path_1, main_project_dir, suffix1)
    copy_results_to_main_project(project_path_2, main_project_dir, suffix2)

if __name__ == "__main__":
    run_simulations()
