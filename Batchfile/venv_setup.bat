@echo off
chcp 65001
SETLOCAL

rem Python 설치 경로 설정 (Python 3.11.2)
set PYTHON_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python311\python.exe

rem Python 3.11.2가 설치되어 있는지 확인
if not exist "%PYTHON_PATH%" (
    echo "Python 3.11.2이(가) 설치되어 있지 않습니다. 설치를 진행합니다."
    
    rem Python 3.11.2 다운로드
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe' -OutFile 'python-3.11.2-amd64.exe'"
    
    rem 설치
    start /wait python-3.11.2-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-3.11.2-amd64.exe
) else (
    echo "Python 3.11.2이(가) 이미 설치되어 있습니다."
)

rem 가상 환경 디렉토리 이름 설정
set ENV_DIR=.venv

rem 가상 환경 생성
"%PYTHON_PATH%" -m venv %ENV_DIR%

echo 가상 환경 활성화 중...

rem PowerShell에서 가상 환경 활성화
powershell -Command ".\%ENV_DIR%\Scripts\Activate.ps1"

echo 가상 환경이 성공적으로 생성되고 활성화되었습니다.
echo 가상 환경을 활성화하려면 다음 명령을 사용하세요:
echo .\%ENV_DIR%\Scripts\Activate.ps1
