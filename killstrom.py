import os
import requests
import time

# Colors
RED = '\033[1;31m'
GREEN = '\033[1;32m'
BLUE = '\033[1;34m'
CYAN = '\033[1;36m'
YELLOW = '\033[1;33m'
WHITE = '\033[1;37m'
RESET = '\033[0m'

def banner():
    os.system('clear')
    print(f"{CYAN}======================================")
    print(f"{BLUE}       KILLSTROM SIM DATABASE TOOL")
    print(f"{CYAN}======================================")
    print(f"{WHITE}      Powered By Mudassar Emperor")
    print(f"{CYAN}======================================{RESET}\n")

def open_whatsapp():
    print(f"{GREEN}[+] Redirecting to WhatsApp...{RESET}")
    os.system("termux-open-url https://whatsapp.com/channel/0029Vb6wpB8EVccOvGA5Lt1d")
    time.sleep(2)

def fetch_pak_data(query):
    clean_number = query.lstrip('0')
    print(f"{BLUE}[*] Searching Pakistan Database for {clean_number}...{RESET}")
    api_url = f"https://fam-official.serv00.net/api/database.php?number={clean_number}"

    try:
        response = requests.get(api_url, timeout=15)
        json_data = response.json()
        if json_data.get("success") and "data" in json_data:
            records = json_data["data"].get("records", [])
            if records:
                print(f"\n{GREEN}--- PAKISTAN RECORDS FOUND ---{RESET}")
                for record in records:
                    print(f"{CYAN}Name:    {RESET}{record.get('full_name', 'N/A')}")
                    print(f"{CYAN}Mobile:  {RESET}{record.get('phone', 'N/A')}")
                    print(f"{CYAN}CNIC:    {RESET}{record.get('cnic', 'N/A')}")
                    print(f"{CYAN}Address: {RESET}{record.get('address', 'N/A')}")
                    print(f"{BLUE}---------------------{RESET}")
            else:
                print(f"{RED}[!] No records found.{RESET}")
        else:
            print(f"{RED}[!] API Error or No Record Found.{RESET}")
    except:
        print(f"{RED}[!] Connection Error.{RESET}")
    input(f"\n{YELLOW}Press Enter to return...{RESET}")

def fetch_india_data(query):
    print(f"{BLUE}[*] Searching India Database for {query}...{RESET}")
    api_url = f"https://source-code-api.vercel.app/?num={query}"

    try:
        response = requests.get(api_url, timeout=15)
        json_data = response.json()
        if json_data.get("success") and "result" in json_data:
            records = json_data["result"]
            if records:
                print(f"\n{GREEN}--- INDIA RECORDS FOUND ---{RESET}")
                for r in records:
                    print(f"{CYAN}Name:     {RESET}{r.get('𝐍𝐚𝐦𝐞', 'N/A')}")
                    print(f"{CYAN}Father:   {RESET}{r.get('𝐅𝐚𝐭𝐡𝐞𝐫\'𝐬 𝐍𝐚𝐦𝐞', 'N/A')}")
                    print(f"{CYAN}Mobile:   {RESET}{r.get('𝐌𝐨𝐛𝐢𝐥𝐞', 'N/A')}")
                    print(f"{CYAN}Address:  {RESET}{r.get('𝐀𝐝𝐝𝐫𝐞𝐬𝐬', 'N/A')}")
                    print(f"{CYAN}Circle:   {RESET}{r.get('𝐂𝐢𝐫𝐜𝐥𝐞', 'N/A')}")
                    print(f"{BLUE}---------------------{RESET}")
            else:
                print(f"{RED}[!] No records found.{RESET}")
        else:
            print(f"{RED}[!] Record not found in India database.{RESET}")
    except:
        print(f"{RED}[!] Connection Error.{RESET}")
    input(f"\n{YELLOW}Press Enter to return...{RESET}")

def main_menu():
    while True:
        banner()
        print(f"{WHITE}1.{RESET} Join WhatsApp Channel")
        print(f"{WHITE}2.{RESET} Search SIM")
        print(f"{WHITE}3.{RESET} Search CNIC")
        print(f"{WHITE}4.{RESET} Search Another")
        print(f"{WHITE}5.{RESET} Search India")
        print(f"{RED}00.{RESET} Exit")
        
        choice = input(f"\n{CYAN}Select an option: {RESET}")

        if choice == '1':
            open_whatsapp()
        elif choice in ['2', '3', '4']:
            val = input(f"{YELLOW}[?] Enter Number/CNIC: {RESET}").strip()
            fetch_pak_data(val)
        elif choice == '5':
            val = input(f"{YELLOW}[?] Enter India Number: {RESET}").strip()
            fetch_india_data(val)
        elif choice == '00':
            print(f"{GREEN}Exiting... Goodbye!{RESET}")
            break
        else:
            print(f"{RED}[!] Invalid Choice{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
