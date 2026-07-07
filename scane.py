 
import os
import sys

# ۱. بررسی دسترسی روت
if os.geteuid() != 0:
    print("\n[-] Error: Please run this script with 'sudo'!")
    print("[*] Usage: sudo python3 lazy_scan.py\n")
    sys.exit()

print("""
==================================================
 🕵️♂️ LOCAL NETWORK INTRUSION DETECTOR v1.0 🕵️♂️
==================================================
""")

# ۲. گرفتن رنج شبکه از کاربر
print("[i] Since you are on NAT mode, use: 10.0.2.0/24")
subnet = input("[?] Enter your network subnet: ")

if not subnet:
    subnet = "10.0.2.0/24"

print(f"\n[*] Scanning network {subnet} for active devices... Please wait...\n")

# ۳. اجرای انمپ و فیلتر کردن آیپیهای روشن
output_file = "live_hosts.txt"
# این دستور انمپ پینگ اسکن انجام میدهد و خروجی را مرتب میکند
os.system(f"nmap -sn {subnet} -oG - | grep Up | awk '{{print $2}}' > {output_file}")

# ۴. خواندن و نمایش نتایج
if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
    with open(output_file, "r") as f:
        hosts = f.read().splitlines()

    print("-" * 50)
    print(f"🎉 Scan Complete! Found {len(hosts)} active devices:")
    print("-" * 50)

    for ip in hosts:
        print(f"[+] Device Online: {ip}")
    
    print("-" * 50)
    print(f"[i] IP list saved to '{output_file}'.")
else:
    print("[-] No devices found or Nmap scan failed.")

print("[*] Ready for GitHub repository!")
سسس
