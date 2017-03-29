import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
redirect_ip = "127.0.0.1"
blocked_sites = ["www.facebook.com", "facebook.com", "www.facebook.com.br", "facebook.com.br"]

while True:
    min_threshold = dt(dt.now().year, dt.now().month, dt.now().day, 8)
    max_threshold = dt(dt.now().year, dt.now().month, dt.now().day, 18)

    print("Current time: " + str(dt.now()))

    if min_threshold < dt.now() < max_threshold:
        print("Working hours. Blocking sites...")

        with open(hosts_path, "r+") as file:
            content = file.read()
            for site in blocked_sites:
                if site not in content:
                    file.write(redirect_ip + " " + site + "\n")

    else:
        print("Happy hours!")

        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(site in line for site in blocked_sites):
                    file.write(line)

            file.truncate()

    time.sleep(5)
