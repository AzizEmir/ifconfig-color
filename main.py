import re
import subprocess

# ifconfig çıktısını al
ifconfig_output = subprocess.check_output(['ifconfig'], text=True)

# Regex desenleri ve renk kodlarını tutan bir sözlük
patterns_and_colors = {
    # 'prefixlen' değerini tespit et ve magenta (pembe) renkte vurgula
    r'(?<=prefixlen\s)\d+': "\033[38;2;255;0;255m",  # magenta 	#FF00FF rgb(255,0,255)
    
    # 'scopeid' değerini tespit et ve magenta (pembe) renkte vurgula
    r'(?<=scopeid\s0x)[a-fA-F0-9]+': "\033[38;2;255;0;255m",  # magenta 	#FF00FF rgb(255,0,255)
    
    # 'KiB' veya 'MiB' ile biten sayıları tespit et ve magenta (pembe) renkte vurgula
    r'\(\d+(\.\d+)?\s(KiB|MiB)\)': "\033[38;2;255;0;255m",  # magenta 	#FF00FF rgb(255,0,255)
    
    # Ağ yapılandırma ile ilgili anahtar kelimeleri (inet6, ether, prefixlen, vb.) sarı renkte vurgula
    r'\b(inet6|inet|netmask|broadcast|ether|prefixlen|scopeid|RX packets|TX packets)\b': "\033[38;2;255;200;0m",  # yellow #FF8C00 rgb(255,140,0)
    
    # IPv4 adreslerini tespit et ve magenta (pembe) renkte vurgula
    r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}': "\033[38;2;255;0;255m",  # magenta #FF00FF rgb(255,0,255)
    
    # Arayüz isimlerini (örneğin 'eth0', 'wlan0') tespit et ve mavi renkte vurgula
    r'^([\w-]+):': "\033[38;2;30;144;255m",  # rgb(30, 144, 255) mavi
    
    # MAC adreslerini tespit et ve yeşil renkte vurgula
    r'(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}': "\033[38;2;0;255;144m",  # rgb(0, 255, 144) yeşil

    # ipv6
    r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])) ':"\033[38;2;255;0;255m", # mediumpurple 	#9370DB 	rgb(147,112,219)
}

# Her bir regex deseni ve renk kodu için işlemleri uygula
highlighted_output = ifconfig_output

for pattern, color_code in patterns_and_colors.items():
    # Eşleşen kısımları renklendirmek için regex'i uygula
    highlighted_output = re.sub(pattern, lambda match: f"{color_code}{match.group(0)}\033[0m", highlighted_output, flags=re.M)

# Renklendirilmiş çıktıyı terminale yazdır
print(highlighted_output)
