
import re
from collections import defaultdict
import argparse

parser = argparse.ArgumentParser(description="User log raport")
parser.add_argument("-f", "--file_in", type=str)
parser.add_argument("-o", "--output", type=str)

args = parser.parse_args()

in_file = args.file_in
out_file = args.output

print(f"in: {in_file}, out: {out_file}")

user_log_pattern = re.compile("\w+-\d+;(LOGIN|LOGOUT);\d+")
user_last_login = {}
user_total_time = defaultdict(int)


def parse_line(line):
    if user_log_pattern.match(line):
        user, action, t = line.split(";")
        t = int(t)
        if action == "LOGIN":
            user_last_login[user] = t
        elif action == "LOGOUT":
            user_total_time[user] += t - user_last_login[user]

def read_logs():
    with open(in_file) as logs:
        for line in logs:
            parse_line(line)
                
def create_report():
    with open(out_file, 'w') as report:
        report.write("Czas przebywania w systemie:\n\n")
        for u, t in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
            report.write(f"{u:12}: {t} s\n")
                

def main():
    read_logs()
    create_report()
    
    
if __name__ == "__main__":
    main()

    
