@echo off
chcp 65001
SETLOCAL

rem 가상 환경 디렉토리 설정
set ENV_DIR=.venv

rem 가상 환경 생성
python -m venv %ENV_DIR%

rem 가상 환경 활성화
call %ENV_DIR%\Scripts\activate.bat

rem pip 최신 버전으로 업그레이드
python -m pip install --upgrade pip

pip install -r requirements.txt

echo 가상 환경이 성공적으로 설정되었습니다.
echo 가상 환경을 활성화하려면 다음 명령을 사용하세요:
echo .\%ENV_DIR%\Scripts\Activate.ps1
