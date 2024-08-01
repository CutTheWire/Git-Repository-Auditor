import os
import dotenv
from git import Repo
from typing import List

class DirectoryAnalyzer:
    def __init__(self, path: str):
        self.path = path
        self.tree_lines = []
        self.changes = []

    def process_item(self, item: str, is_last: bool, prefix: str, is_recording: bool):
        icon = "📂" if os.path.isdir(os.path.join(self.path, item)) else "📜"
        connector = "┗" if is_last else "┣"
        line = f"{prefix} {connector} {icon} {item}"
        if is_recording:
            self.tree_lines.append(line)

        return "  " if is_last else " ┃ "

    def directory_tree(self, sub_path: str = "", prefix: str = "", is_recording: bool = False) -> list:
        contents = os.listdir(os.path.join(self.path, sub_path))
        
        for i, item in enumerate(contents):
            is_last = i == len(contents) - 1
            new_prefix = self.process_item(item, is_last, prefix, is_recording)
            
            full_path = os.path.join(self.path, sub_path, item)
            if os.path.isdir(full_path):
                self.directory_tree(os.path.join(sub_path, item), prefix + new_prefix, is_recording)

        return self.tree_lines

    def changes_state(self, commit_hash: str) -> list:
        repo = Repo(self.path)
        commit = repo.commit(commit_hash)

        for changed_file, stats in commit.stats.files.items():
            if stats['deletions'] > 0 and stats['insertions'] > 0:
                self.changes.append(f"🔄 {changed_file} (수정)")
            elif stats['deletions'] > 0:
                self.changes.append(f"❌ {changed_file} (삭제)")
            elif stats['insertions'] > 0:
                self.changes.append(f"✅ {changed_file} (추가)")

        return self.changes

    def save_to_md(self, repo_name: str) -> None:
        """
        트리 구조와 변경 사항을 markdown 파일로 저장합니다.
        """
        # Template 폴더에 markdown 파일로 저장
        template_folder = os.path.join('./Template')
        os.makedirs(template_folder, exist_ok=True)
        md_file_path = os.path.join(template_folder, 'changes.md')

        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write("# Git state\n\n")
            f.write("- 디렉토리 구조\n\n")
            f.write("```\n")
            f.write(f"📦{repo_name}\n")
            f.write("\n".join(self.tree_lines))
            f.write("\n")
            f.write("```\n\n")

            
            f.write("- 변경 사항\n\n")
            f.write("```\n")
            for change in self.changes:
                f.write(f"{change}\n")
            f.write("```\n\n")

if __name__ == "__main__":
    dotenv.load_dotenv()  # .env 파일 로드
    URL = os.environ.get('REPO_URL')
    BRANCH = os.environ.get('BRANCH_NAME')
    SHA = os.environ.get('COMMIT_SHA')
    path_parts = URL.strip("/").split("/")
    repo_name = path_parts[4].replace('.git', '')  # 리포지토리 이름 (확장자 제거)
    
    # 현재 스크립트의 상위 폴더 경로
    parent_dir = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))
    folder_name = 'Checking_folder'
    folder_path = os.path.join(parent_dir, folder_name)

    if os.path.exists(folder_path):  # 디렉토리 존재 여부 확인
        print("오류: 'Checking_folder'가 여전히 존재합니다. 수동으로 삭제하십시오.")
    else:  # 리포지토리 클론 및 작업
        try:
            repo = Repo.clone_from(URL, folder_path)  # 상위 디렉토리에 클론할 디렉토리
            repo.git.checkout(BRANCH)  # 브랜치 전환
            
            DA = DirectoryAnalyzer(folder_path)  # DirectoryAnalyzer 인스턴스 생성
            tree_lines = DA.directory_tree(is_recording=True)
            changes = DA.changes_state(SHA)
            DA.save_to_md(repo_name)
        except Exception as e:
            print(f"오류 발생: {e}")

