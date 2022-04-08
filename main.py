import subprocess, sys
from platform import system

def ping_from_line(_ip_):
    _os_ = system().lower()
    if _os_ == 'windows':
        print()
        for i in range(1, len(_ip_)):
            try:
                ping_ = subprocess.check_output(f'ping -n 2 {_ip_[i]}').decode('utf-8')
                if 'host unreachable' in ping_:
                    print(f'{_ip_[i]}: HOST UNREACHABLE')
                else:
                    print(f'{_ip_[i]}: HOST IS UP')
            except subprocess.CalledProcessError:
                print(f'{_ip_[i]}: HOST UNREACHABLE')
        print()
list = sys.argv
ping_from_line(list)
