@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

title Pasifik'in Altindaki Muhur - Sesli Kitap Olusturucu

echo ==================================================
echo   Pasifik'in Altindaki Muhur - Sesli Kitap
echo ==================================================
echo.

:: Python kontrolu
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [HATA] Python bulunamadi!
    echo.
    echo Lutfen Python'u su adresten indirip kurun:
    echo https://www.python.org/downloads/
    echo.
    echo Kurulum sirasinda "Add Python to PATH" kutucugunu isaretlemeyi unutmayin.
    echo.
    pause
    exit /b 1
)

echo Python bulundu.
echo.

:: Gerekli paketleri kur
echo Gerekli kutuphaneler kontrol ediliyor ve kuruluyor...
python -m pip install --upgrade pip --quiet
python -m pip install -r requirements.txt --quiet

if %errorlevel% neq 0 (
    echo.
    echo [HATA] Kutuphaneler kurulamadi!
    echo Lutfen internet baglantinizi kontrol edin.
    pause
    exit /b 1
)

echo.
echo Sesli kitap olusturuluyor...
echo Bu islem biraz surebilir (her bolum icin 1-3 dakika).
echo.

python generate_audiobook.py

echo.
echo ==================================================
echo Islem tamamlandi!
echo MP3 dosyalari "mp3" klasorunun icinde.
echo Playlist dosyasini VLC ile acabilirsiniz.
echo ==================================================
echo.
pause
