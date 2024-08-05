import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../internetbs')))

from host import Host

host = Host('testapi', 'testpass', test_mode=True)

def run_test(test_number):
    if test_number == 1:
        print("(1) Testing Domain/Host/Create")
        response = host.create_host('test.com', '127.0.0.1')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 2:
        print("(2) Testing Domain/Host/Info")
        response = host.get_host_info('test.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 3:
        print("(3) Testing Domain/Host/Update")
        response = host.update_host('test.com', '127.0.0.1')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 4:
        print("(4) Testing Domain/Host/Delete")
        response = host.delete_host('test.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    elif test_number == 5:
        print("(5) Testing Domain/Host/List")
        response = host.list_hosts('test.com')
        print("Status:", response['status'])
        print("Message:", response.get('message', ''))
    else:
        print("Invalid test number")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_number = int(sys.argv[1])
    else:
        test_number = 1 
    run_test(test_number)
