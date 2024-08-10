import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../internetbs')))

from dns import DNS

dns = DNS('testapi', 'testpass', test_mode=True)

def run_test(test_number):
    test_cases = [
        (1, "DNS/AddRecord", lambda: dns.add_record('pybs.com', 'A', '192.0.2.1')),
        (2, "DNS/RemoveRecord", lambda: dns.remove_record('pybs.com', 'A', '192.0.2.1')),
        (3, "DNS/UpdateRecord", lambda: dns.update_record('pybs.com', 'A', '192.0.2.1', '192.0.2.2')),
        (4, "DNS/ListRecords", lambda: dns.list_records('pybs.com')),
    ]

    if test_number == 0:
        for case in test_cases:
            test_num, test_name, test_func = case
            print(f"({test_num}) Testing {test_name}")
            try:
                response, url = test_func()
                print("Transaction ID:", response.transactid)
                print("Status:", response.status)
                if test_num == 4:
                    print("Records:", response.records)
                print("API URL:", url)
            except Exception as e:
                print("Exception occurred:", str(e))
            input("Press Enter to continue to the next test...")
    elif 1 <= test_number <= len(test_cases):
        test_num, test_name, test_func = test_cases[test_number - 1]
        print(f"({test_num}) Testing {test_name}")
        try:
            response, url = test_func()
            print("Transaction ID:", response.transactid)
            print("Status:", response.status)
            if test_num == 4:
                print("Records:", response.records)
            print("API URL:", url)
        except Exception as e:
            print("Exception occurred:", str(e))
    else:
        print("Invalid test number")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_number = int(sys.argv[1])
    else:
        test_number = 0
    run_test(test_number)
