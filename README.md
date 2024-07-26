# Git-Repository-Auditor

Python을 사용하여 Github의 각종 정보(파일 변경 내역, 깃 브런치 라인, ... 등)를 제공합니다.

## 설치 및 실행
이 프로젝트를 실행하기 위해서는 가상 환경 설정이 필요합니다. 다음 단계를 따라 진행해 주세요.

### 1. 가상 환경 설정
Windows 사용자의 경우 `Batchfile/venv_setup.bat` 파일을 실행하세요.
Linux/macOS 사용자의 경우 `Batchfile/venv_setup.sh` 파일을 실행하세요.

- Windows OS
```powershell
& ./Batchfile/venv_setup.bat
```
- Linux OS
```shell
source Batchfile/venv_setup.sh
```

이 스크립트는 Python 3.11.2를 설치하고 가상 환경을 생성합니다.


### 2. 가상 환경 라이브러리 설치 
Windows 사용자의 경우 `Batchfile/venv_install.bat` 파일을 실행하세요.
Linux/macOS 사용자의 경우 `Batchfile/venv_install.sh` 파일을 실행하세요.

- Windows OS
```powershell
& ./Batchfile/venv_install.bat
```
- Linux OS
```shell
source Batchfile/venv_install.sh
```

### 3. 가상 환경 활성화

Windows 사용자의 경우 `call .venv/Scripts/activate.bat`를 실행하세요.
Linux/macOS 사용자의 경우 `source .venv/bin/activate`를 실행하세요.

- Windows OS
```powershell
.\.venv\Scripts\Activate.ps1
```
- Linux OS
```shell
source .venv/bin/activate
```

### 4. .env 설정


이제 프로젝트를 사용할 준비가 되었습니다. 즐겁게 사용하세요!
