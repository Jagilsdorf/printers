import csv, subprocess, os, json; from datetime import datetime 

if 'OPTIONS' == 'OPTIONS':
    printing =      True    #Default: False | 
    update_json =   False   #Default: False | If true, printer.json will be deleted and replaced

if 'CONSTANTS' == 'CONSTANTS':   
    if datetime.now().day == 1 or os.path.exists('printer.json') == False: update_json = True
    all_printers = {}

if "FUNC" == "FUNC":
    def csv_write(path, headers, data):
        with open(path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

    def json_rw(save_or_open, dict):
        if save_or_open == "save":
            with open('printer.json', 'w') as file: json.dump(dict, file)
        else:
            dict = {}
            with open('printer.json', 'r') as file: dict = json.load(file)
        return dict

    def get_printers_from_UNC(UNC_name):
        output = subprocess.check_output(['powershell', '-Command', f"Get-Printer -ComputerName {UNC_name}"], stderr=subprocess.STDOUT, text=True)
        temp = {}
        for line in output.splitlines():
            if not line.strip() or line.startswith("Name"):
                continue
            else:
                location, hostname, ip = line.split()[0][:3], line.split()[0], line.split()[-4]
                print(location, hostname, ip)
                if ip.startswith('10.1'):
                    print(hostname)
                    if location not in list(temp.keys()): temp[location] = {}
                    if hostname not in list((temp[location]).keys()): temp[location][hostname] = {}
                    temp[location][hostname]['ip']= ip
                    json_rw('save',temp)
                    print('\n\n\n\n\n\n\n\n\n\n\n\n')
        return temp

if 'INITIALIZE' == 'INITIALIZE':
    if update_json == True: all_printers = (get_printers_from_UNC("print-us"))
    else: all_printers = json_rw('open', all_printers)
    