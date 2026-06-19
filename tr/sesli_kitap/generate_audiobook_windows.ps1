# Pasifik’in Altındaki Mühür - Windows Sesli Kitap Üretici
#
# edge-tts kullanır (en iyi Türkçe kalite)
# Native Windows TTS çok kötü olduğu için önerilmez.
#
# Kullanım:
#   PowerShell'de:
#   .\generate_audiobook_windows.ps1
#
# Gereksinim:
#   pip install edge-tts

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$chapterDir = Join-Path $scriptDir "metinler"
$outputDir = Join-Path $scriptDir "mp3"
$voice = "tr-TR-EmelNeural"
$rate = "-12%"

New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

Write-Host "========================================"
Write-Host "  Pasifik’in Altındaki Mühür - Windows"
Write-Host "  edge-tts ile Türkçe ses"
Write-Host "========================================"
Write-Host ""

$python = "python"
if (-not (Get-Command $python -ErrorAction SilentlyContinue)) {
    $python = "python3"
}

& $python (Join-Path $scriptDir "generate_audiobook.py")