import subprocess

# Bash command to run (split into individual arguments)
bash_command = ["bash", "-c", 'wget -qO- https://gitlab.com/rwkgyg/CFwarp/raw/main/CFwarp.sh | bash']

# Run the Bash command as a subprocess
try:
    subprocess.run(bash_command, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
