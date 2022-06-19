from http.client import OK
import os
import re

ip_list = []

with open("./ip_list.yml") as rf:
    lines = rf.readlines()

    for line in lines:
        if len(line) == 0:
            continue
        if line.startswith("-"):
            line = line.split(":")
            print("此时的line",line)
            ip = line[1].strip()     # 获取文件中的ip地址
            ip_list.append(ip)

    buffer = ""
    for ip in ip_list:
        result = ""
        a = os.system(f"ping -c4 {ip} > /dev/null")
        if a == 0:
            result = "ok"
        elif a == 256:
            result = "fail"
        buffer += f"- ip: {ip} \n"
        buffer += f"  status: {result} \n"
        buffer += f"\n"
    print(buffer)