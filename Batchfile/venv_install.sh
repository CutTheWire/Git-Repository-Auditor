#!/bin/bash

# UTF-8 설정
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# 가상 환경 디렉토리 설정
ENV_DIR=".venv"

# 가상 환경 생성
python3 -m venv $ENV_DIR

# 가상 환경 활성화
source $ENV_DIR/bin/activate

# pip 최신 버전으로 업그레이드
pip install --upgrade pip

pip install -r requirements.txt

echo "가상 환경이 성공적으로 설정되었습니다."
echo "가상 환경을 활성화하려면 다음 명령을 사용하세요:"
echo "source $ENV_DIR/bin/activate"