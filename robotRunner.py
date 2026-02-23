# robotRunner.py
# C:\Users\user\PycharmProjects\exantring\robotRunner.py
# C:\Users\user\PycharmProjects\exantring\Tests


import subprocess
import sys

# Varsayılan tag değeri
tag = "loginLoyalFriendCare"

def run_tests(tag):
    # Test dosyalarının bulunduğu dizin
    test_directory = r'C:\Users\user\PycharmProjects\exantring\Tests'  # Dosya yolunu güncelledik

    # Robot Framework komutunu oluştur
    command = f'robot --include {tag} "{test_directory}"'  # Yolü tırnak içinde aldık

    # Komutu çalıştır
    process = subprocess.run(command, shell=True)

    # Çalıştırma sonucu
    if process.returncode == 0:
        print("Testler başarıyla çalıştırıldı.")
    else:
        print("Test çalıştırma sırasında hata oluştu.")


if __name__ == '__main__':
    # Komut satırından tag alınıyorsa, onu kullan
    if len(sys.argv) > 1:
        tag = sys.argv[1]

    run_tests(tag)

# python robotRunner.py loginLoyalFriendCare