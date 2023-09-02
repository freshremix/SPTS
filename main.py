import subprocess

# Bash command to run (using curl)
bash_command = ["bash", "-c", 'curl -sSL https://gitlab.com/rwkgyg/CFwarp/raw/main/CFwarp.sh | bash']

# Run the Bash command as a subprocess
try:
    subprocess.run(bash_command, check=True, shell=False)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
