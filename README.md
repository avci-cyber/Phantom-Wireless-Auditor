# Phantom-Wireless-Auditor
Kablosuz ağ güvenliği ve zafiyet analizi için sahte AP simülatörü

**Phantom Wireless Auditor**, kablosuz ağ güvenliği araştırmaları ve zafiyet analizleri için geliştirilmiş Python tabanlı bir ağ simülasyon aracıdır. Bu araç, `airbase-ng` kütüphanesini kullanarak aynı anda birden fazla Sahte Erişim Noktası (Rogue AP) oluşturmanıza ve ağ yayını yapmanıza olanak tanır.

## 🚀 Özellikler
- **Multi-SSID:** Tek bir komutla birden fazla (10-20+) sahte AP yayını başlatabilir.
- **Root Check:** Güvenli çalışma için sistem yetkilerini otomatik kontrol eder.
- **Modern Argparse:** Kullanıcı dostu komut satırı argümanları ile kolay yönetim.
- **Process Management:** Tüm alt süreçleri (Subprocess) güvenli bir şekilde yönetir ve tek komutla temizleme yapar.

## 🛠️ Gereksinimler
- Kali Linux veya Parrot OS
- `aircrack-ng` paketi (`sudo apt install aircrack-ng`)
- Monitör modunu destekleyen bir Wi-Fi adaptörü

## 📖 Kullanım
```bash
sudo python3 phantom_auditor.py -e "Ucretsiz_Internet" -i wlan0mon -c 5

Yasal Uyarı (Disclaimer)
Bu araç tamamen etik eğitim ve güvenlik testleri amacıyla geliştirilmiştir. Yetkiniz olmayan ağlarda kullanılması yasal sorumluluk doğurabilir. Kullanıcı, bu aracın kullanımından doğacak tüm yasal sonuçlardan kendisi sorumludur.
