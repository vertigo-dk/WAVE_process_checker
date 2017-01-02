import subprocess, signal, os, time

refresh_rate = 2.0 # time in s between checks

def check_processes():
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE) # check all processes
    out, err = p.communicate()
    text_edit_running = False

    print('Checking processes...')

    for line in out.splitlines():
        if '/Applications/TextEdit.app/Contents/MacOS/TextEdit' in line:
            pid = int(line.split(None, 1)[0])
            print(pid)
            text_edit_running = True
            print('Text edit running')

    if(text_edit_running == False):
        os.system('open /Applications/TextEdit.app')
        print('Launching TextEdit')


if __name__ == "__main__":
    while True:
        os.system('sudo ./killunresponsive/killunresponsive ')
        check_processes()
        time.sleep(refresh_rate)
