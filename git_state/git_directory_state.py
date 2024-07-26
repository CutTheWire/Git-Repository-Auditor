import os
import dotenv
import shutil
import stat
from git import Repo

def print_tree(path, prefix=""):
    """
    주어진 경로의 폴더 및 파일 구조를 출력합니다.
    """
    contents = os.listdir(path)
    for i, item in enumerate(contents):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if i == len(contents) - 1:
                print(f"{prefix} ┗ 📂 {item}")
                print_tree(item_path, f"{prefix}   ")
            else:
                print(f"{prefix} ┣ 📂 {item}")
                print_tree(item_path, f"{prefix} ┃ ")
        else:
            if i == len(contents) - 1:
                print(f"{prefix} ┗ 📜 {item}")
            else:
                print(f"{prefix} ┣ 📜 {item}")


def print_changes(repo_path, commit_hash):
    """
    git 기준 파일의 상태를 출력합니다.
    """
    repo = Repo(repo_path)
    commit = repo.commit(commit_hash)
    
    # 디렉토리 구조 출력
    print_tree(repo_path)
    print()
    
    # 변경된 파일 출력
    for changed_file in commit.stats.files:
        if commit.stats.files[changed_file]['deletions'] > 0 and commit.stats.files[changed_file]['insertions'] > 0:
            print(f"🔄 {changed_file} (수정)")
        elif commit.stats.files[changed_file]['deletions'] > 0:
            print(f"❌ {changed_file} (삭제)")
        elif commit.stats.files[changed_file]['insertions'] > 0:
            print(f"✅ {changed_file} (추가)")

def handle_remove_readonly(func, path, excinfo):
    """
    파일 권한을 변경하여 읽기 전용을 해제하고 다시 시도
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)  # 삭제를 다시 시도

if __name__ == "__main__":
    dotenv.load_dotenv() # .env 파일 로드
    URL = os.environ.get('REPO_URL')
    BRANCH = os.environ.get('BRANCH_NAME')
    SHA = os.environ.get('COMMIT_SHA')

    # 현재 스크립트의 상위 폴더 경로
    parent_dir = os.path.abspath(os.path.join(__file__,os.pardir,os.pardir,os.pardir))
    folder_name = 'Checking_folder'
    folder_path = os.path.join(parent_dir, folder_name)

    # 기존 폴더 삭제
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path, onerror=handle_remove_readonly)
        except Exception as e:
            print(f"폴더 삭제 중 오류 발생: {e}")

    if os.path.exists(folder_path): # 디렉토리 존재 여부 확인
        print("오류: 'Checking_folder'가 여전히 존재합니다. 수동으로 삭제하십시오.")
    else: # 리포지토리 클론 및 작업
        try:
            repo = Repo.clone_from(URL, folder_path)  # 상위 디렉토리에 클론할 디렉토리
            repo.git.checkout(BRANCH)  # 브랜치 전환
            print_changes(folder_path, SHA)  # 변경 내역 출력
        except Exception as e:
            print(f"오류 발생: {e}")
