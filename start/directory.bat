@echo off
chcp 65001
SETLOCAL

REM remove_folder.py 실행
python .\git_state\remove_folder.py
IF ERRORLEVEL 1 (
    echo remove_folder.py 실행 중 오류 발생
    exit /b 1
)

REM git_directory_state.py 실행
python .\git_state\git_directory_state.py
IF ERRORLEVEL 1 (
    echo git_directory_state.py 실행 중 오류 발생
    exit /b 1
)

REM remove_folder.py 다시 실행
python .\git_state\remove_folder.py
IF ERRORLEVEL 1 (
    echo remove_folder.py 다시 실행 중 오류 발생
    exit /b 1
)

echo 모든 작업이 성공적으로 완료되었습니다.
exit /b 0
