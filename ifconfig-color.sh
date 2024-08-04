#!/bin/bash

ifconfig | awk '
BEGIN {
    # Renk kodları
    BRIGHT_YELLOW="\033[93m"    # Parlak altın sarısı
    BRIGHT_MAGENTA="\033[95m"   # Parlak mor
    BRIGHT_BLUE="\033[94m"      # Parlak mavi
    BRIGHT_GREEN="\033[92m"     # Parlak yeşil
    RESET="\033[0m"
}
{
    # Arayüz isimlerini parlak mavi renkle
    if (match($0, /^[a-zA-Z0-9:_]+:/)) {
        interface_name = substr($0, 1, RLENGTH)
        rest_of_line = substr($0, RLENGTH + 1)
        print BRIGHT_BLUE interface_name RESET rest_of_line
    } else {
        # RX packets ve TX packets başlıklarını parlak yeşil ile renklendir
        gsub(/RX packets/, BRIGHT_GREEN "&" RESET)
        gsub(/TX packets/, BRIGHT_GREEN "&" RESET)
        
        # Boyut bilgilerini parlak yeşil ile renklendir
        gsub(/\([0-9.]+ [KMGTPE]iB\)/, BRIGHT_GREEN "&" RESET)
        
        # "ether" ve MAC adresini renklendir
        gsub(/ether /, BRIGHT_YELLOW "&" RESET)
        gsub(/[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}/, BRIGHT_MAGENTA "&" RESET)
        
        # "inet", "netmask", ve "broadcast" kelimelerini parlak altın sarı ile renklendir
        gsub(/inet |netmask |broadcast /, BRIGHT_YELLOW "&" RESET)
        
        # IP adreslerini parlak mor ile renklendir
        gsub(/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/, BRIGHT_MAGENTA "&" RESET)

        print
    }
}
'
