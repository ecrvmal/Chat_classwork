import subprocess
args = ['ping', 'google.com']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in subproc_ping.stdout:
    print(line)