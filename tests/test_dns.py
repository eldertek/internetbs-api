import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../internetbs')))

from dns import DNS

dns = DNS('testapi', 'testpass', test_mode=True)

def run_test(test_number):
    if test_number == 1:
        print("(1) Testing DNS/AddRecord")
        response = dns.add_record('pybs.com', 'A', '192.0.2.1')
        print("Transaction ID:", response.transactid)
        print("Status:", response.status)
    elif test_number == 2:
        print("(2) Testing DNS/RemoveRecord")
        response = dns.remove_record('pybs.com', 'A', '192.0.2.1')
        print("Transaction ID:", response.transactid)
        print("Status:", response.status)
    elif test_number == 3:
        print("(3) Testing DNS/UpdateRecord")
        response = dns.update_record('pybs.com', 'A', '192.0.2.1', '192.0.2.2')
        print("Transaction ID:", response.transactid)
        print("Status:", response.status)
    elif test_number == 4:
        print("(4) Testing DNS/ListRecords")
        response = dns.list_records('pybs.com')
        print("Transaction ID:", response.transactid)
        print("Status:", response.status)
        print("Records:", response.records)
    else:
        print("Invalid test number")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_number = int(sys.argv[1])
    else:
        test_number = 1 
    run_test(test_number)
