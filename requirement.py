import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#install("streamlit")  
install("streamlit_extras") 
