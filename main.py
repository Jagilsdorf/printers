import csv, subprocess, os, json; from datetime import datetime 

if 'OPTIONS' == 'OPTIONS':
    printing =      True    #Default: False | 
    update_json =   True   #Default: False | If true, printer.json will be deleted and replaced

if 'CONSTANTS' == 'CONSTANTS':   
    if datetime.now().strftime('%A') == 'Monday' or os.path.exists('printer.json') == False:
        update_json = True
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

    def get_ip_from_hostname_powershell(hostname):
        try:
            command = f"Resolve-DnsName {hostname}"
            output = subprocess.check_output(['powershell', '-Command', command], stderr=subprocess.STDOUT, text=True)
            for line in output.splitlines():
                if hostname in line and " A " in line:  # Ensure we are picking up only the IPv4 records
                    return line.split()[-1]
        except subprocess.CalledProcessError:
            pass
        return None

    def update_printer_DNS():
        all_printers = {'DEP': {}, 'KAN': {}, 'ONT': {}}

        for x in range(1, 256):  # Include ABC1P001 to ABC1P255
            formatted_name = f"{x:03}"  # Formats the number to 3 digits with leading zeros
            all_printers['DEP'][f'DEP1P{formatted_name}'] = {}
            all_printers['KAN'][f'KAN1P{formatted_name}'] = {}
            all_printers['ONT'][f'ONT1P{formatted_name}'] = {}

        for location in list(all_printers.keys()):
            for printer in list(all_printers[location].keys()):
                all_printers[location][printer] = {'ip':get_ip_from_hostname_powershell(printer)}
                json_rw('save',all_printers)


if 'INITIALIZE' == 'INITIALIZE':
    #Update json if needed & load into all_variable
    if update_json == True: update_printer_DNS()
    else: all_printers = json_rw('open', all_printers)


