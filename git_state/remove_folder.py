import os
import stat
import shutil

def handle_remove_readonly(func, path, excinfo):
    """
    파일 권한을 변경하여 읽기 전용을 해제하고 다시 시도
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)  # 삭제를 다시 시도

if __name__ == "__main__":
    parent_dir = os.path.abspath(os.path.join(__file__,os.pardir,os.pardir,os.pardir))
    folder_name = 'Checking_folder'
    folder_path = os.path.join(parent_dir, folder_name)

    # 기존 폴더 삭제
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path, onerror=handle_remove_readonly)
        except Exception as e:
            print(f"폴더 삭제 중 오류 발생: {e}")