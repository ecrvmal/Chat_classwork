import subprocess
args = ['ping', 'google.com']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

def update_line(line):
    line += ' checked'
    return line

for line in subproc_ping.stdout:
    # print(line)      # output as bytes
    # print(line.decode('cp866'))      # output as string
    l = line.decode('cp866')
    l = update_line(l)
    print(type(l), l)
    encoded_data = l.encode('UTF-8')
    print(encoded_data)

