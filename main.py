import subprocess

# Bash script to run
bash_script = "bash <(wget -qO- https://gitlab.com/rwkgyg/CFwarp/raw/main/CFwarp.sh 2> /dev/null)"

# Run the Bash script as a subprocess
try:
    subprocess.run(bash_script, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
