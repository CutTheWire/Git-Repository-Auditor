import os
import dotenv
import shutil
import stat
from git import Repo

# .env 파일 로드
dotenv.load_dotenv()

# 환경 변수에서 값 가져오기
URL = os.environ.get('REPO_URL')
BRANCH = os.environ.get('BRANCH_NAME')
SHA = os.environ.get('COMMIT_SHA')

def print_tree(path, prefix="", is_last=True):
    """
    주어진 경로의 디렉토리 구조를 마크다운 형식으로 출력합니다.
    
    Args:
        path (str): 탐색할 디렉토리 경로
        prefix (str): 현재 노드의 들여쓰기 접두사
        is_last (bool): 현재 노드가 마지막 노드인지 여부
    """
    contents = os.listdir(path)
    
    for i, item in enumerate(contents):
        item_path = os.path.join(path, item)
        
        # 폴더인 경우
        if os.path.isdir(item_path):
            print(f"{prefix}{' ┗ ' if is_last else ' ┣ '} 📂{item}/")
            
            # 재귀적으로 하위 폴더 출력
            if is_last:
                print_tree(item_path, f"{prefix}  ", True)
            else:
                print_tree(item_path, f"{prefix}  ", False)
        
        # 파일인 경우
        else:
            print(f"{prefix}{' ┗ ' if is_last and i == len(contents) - 1 else ' ┣ '} 📜{item}")



def print_changes(repo_path, commit_hash):
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
    # 파일 권한을 변경하여 읽기 전용을 해제하고 다시 시도
    os.chmod(path, stat.S_IWRITE)
    func(path)  # 삭제를 다시 시도

if __name__ == "__main__":
    # .env 파일 로드
    dotenv.load_dotenv()

    # 환경 변수에서 값 가져오기
    URL = os.environ.get('REPO_URL')
    BRANCH = os.environ.get('BRANCH_NAME')
    SHA = os.environ.get('COMMIT_SHA')

    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    folder_name = 'Checking_folder'
    folder_path = os.path.join(parent_dir, folder_name)

    # 기존 폴더 삭제
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path, onerror=handle_remove_readonly)
        except Exception as e:
            print(f"폴더 삭제 중 오류 발생: {e}")

    # 디렉토리 존재 여부 확인
    if os.path.exists(folder_path):
        print("오류: 'Checking_folder'가 여전히 존재합니다. 수동으로 삭제하십시오.")
    else:
        # 리포지토리 클론 및 작업
        try:
            repo = Repo.clone_from(URL, folder_path)  # 상위 디렉토리에 클론할 디렉토리
            repo.git.checkout(BRANCH)  # 브랜치 전환
            print_changes(folder_path, SHA)  # 변경 내역 출력
        except Exception as e:
            print(f"오류 발생: {e}")

    # 불러온 Checking_folder 디렉토리 삭제
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path, onerror=handle_remove_readonly)
