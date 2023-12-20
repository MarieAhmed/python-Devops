import os
import subprocess

script_dir = os.path.dirname(__file__)
script_absolute_path = os.path.join(script_dir, "projet1/files/script_test.sh") 
subprocess.call(['sh', script_absolute_path])

param_script_absolute_path = os.path.join(script_dir, "projet1/files/param.sh")
subprocess.call(['sh', param_script_absolute_path, 'param1 param2'])
