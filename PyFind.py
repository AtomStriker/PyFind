import sys
from json import loads
from time import sleep

import colorama
import requests

sys.argv.pop(0)
colorama.init()


def help():
    print(f"""
  {colorama.Fore.MAGENTA}PyFind:{colorama.Fore.RESET}
  -------------------------------------------------
    {colorama.Fore.LIGHTYELLOW_EX}[i]    PyFind is a simple tool to find geolocations of IP addresses.{colorama.Fore.RESET}
    {colorama.Fore.LIGHTRED_EX}[!]    DISCLAIMER: I am not responsible of any damage or exploitations caused by users of this program.{colorama.Fore.RESET}
    {colorama.Fore.LIGHTBLUE_EX}[*]    Note that if you don't supply an IP address, your current one will be .{colorama.Fore.RESET}
    
    [?] Usage: 
      {colorama.Fore.GREEN}# cd to PyFind/{colorama.Fore.RESET}
      {colorama.Fore.YELLOW}python3 py_find.py <ip>{colorama.Fore.RESET}

    If you are facing any issues, feel free to create an issue at the repository.
        """)


# TODO: Implement banner
def banner():
    pass


def get_ip_info(ip):
    if len(sys.argv) == 1:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,query"
        return loads(str(requests.get(url).text))
    else:
        url = "http://ip-api.com/json/?fields=status,message,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,org,as,asname,query"
        return loads(str(requests.get(url).text))


def main():
    ip_info = None

    if len(sys.argv) == 1:
        ip_info = get_ip_info(sys.argv[0])
    else:
        ip_info = get_ip_info(None)
        print(
            f"{colorama.Fore.LIGHTYELLOW_EX}[~] Using current IP address{colorama.Fore.RESET}")

    if ip_info["status"] == "fail":
        return print(f"{colorama.Fore.RED}[!] Error: {ip_info['message'].title()}{colorama.Fore.RESET}")

    print(
        f"{colorama.Fore.GREEN}[%] Getting info for {ip_info['query']}{colorama.Fore.RESET}")
    sleep(3)

    # TODO: Find a better way to handle this
    for key, value in ip_info.items():
        if key.title() == "Countrycode":
            print(
                f"{colorama.Fore.LIGHTBLUE_EX}[*] Country Code:{colorama.Fore.RESET} {value}")
        elif key.title() == "Regionname":
            print(
                f"{colorama.Fore.LIGHTBLUE_EX}[*] Region Name:{colorama.Fore.RESET} {value}")
        elif key == "district" and value == "":
            print(
                f"{colorama.Fore.YELLOW}[?] {key.title()}:{colorama.Fore.RESET} Unavailable")
        elif key.title() == "Isp":
            print(
                f"{colorama.Fore.LIGHTBLUE_EX}[*] ISP:{colorama.Fore.RESET} {value}")
        elif key.title() == "Org":
            print(
                f"{colorama.Fore.LIGHTBLUE_EX}[*] Organization:{colorama.Fore.RESET} {value}")
        elif key.title() == "As":
            print(
                f"{colorama.Fore.LIGHTBLUE_EX}[*] AS:{colorama.Fore.RESET} {value}")
        elif key.title() == "Asname":
            print(
                f"{colorama.Fore.LIGHTBLUE_EX}[*] AS Name:{colorama.Fore.RESET} {value}")
        else:
            print(
                f"{colorama.Fore.LIGHTBLUE_EX}[*] {key.title()}:{colorama.Fore.RESET} {value}")
        sleep(1)


if __name__ == '__main__':
    main()
