#!/usr/bin/env python3
import subprocess
import argparse 
import time
import os
import sys

def show_banner():
    # Banner dosyasını kontrol eder veya varsayılan bir başlık basar
    banner = """
    #######################################
    #      Phantom Wireless Auditor       #
    #    Multi-SSID Beacon Simulation     #
    #        Created by avci-cyber        #
    #######################################
    """
    print(banner)

def parse_arguments():
    
    parser = argparse.ArgumentParser(description="Kablosuz ağ güvenliği ve zafiyet analizi için sahte AP simülatörü.")
    
    parser.add_argument("-e", "--essid", dest="essid", required=True, help="Oluşturulacak sahte ağın temel adı (SSID)")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Kullanılacak ağ arayüzü (Monitör modunda olmalıdır)")
    parser.add_argument("-c", "--count", dest="count", type=int, default=1, help="Kaç adet sahte ağ oluşturulacak?")

    return parser.parse_args()

def check_requirements(interface):
    # Kullanıcı root mu ve arayüz monitör modunda mı?
    if os.getuid() != 0:
        print("[-] HATA: Bu araç root yetkisi gerektirir (sudo).")
        sys.exit(1)
    
    # Airbase-ng kurulu mu kontrolü
    if not os.path.exists("/usr/sbin/airbase-ng"):
        print("[-] HATA: 'airbase-ng' sistemi üzerinde bulunamadı. Lütfen aircrack-ng paketini kurun.")
        sys.exit(1)

def start_fake_ap(essid, interface, count):
    processes = []
    print(f"[*] Operasyon Başlıyor: {interface} üzerinden {count} adet AP oluşturuluyor...")
    
    try:
        for num in range(count):
            ssid = f"{essid}_{num+1}"
            # airbase-ng komutunu arka planda çalıştırıyoruz
            p = subprocess.Popen(
                ["airbase-ng", "--essid", ssid, interface],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            processes.append(p)
            print(f"[+] Yayın Aktif: {ssid}")
            time.sleep(0.5)
        return processes
    except Exception as e:
        print(f"[-] Beklenmedik bir hata oluştu: {e}")
        return processes

def stop_fake_ap(processes):
    print("\n[*] Operasyon Sonlandırılıyor. Tüm süreçler kapatılıyor...")
    for p in processes:
        p.terminate()
    print("[+] Temizlik tamamlandı. Güvenli çıkış yapılıyor.")

def main():
    show_banner()
    args = parse_arguments()
    
    # Gereksinimleri kontrol et
    check_requirements(args.interface)
    
    processes = start_fake_ap(args.essid, args.interface, args.count)
    
    if not processes:
        print("[-] Süreçler başlatılamadı. Çıkış yapılıyor.")
        return

    print("\n[!] Tüm sahte ağlar yayında. Durdurmak için CTRL+C tuşuna basın.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_fake_ap(processes)

if __name__ == "__main__":
    main()
