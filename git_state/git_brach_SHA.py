import os
import requests
import dotenv

def get_network_graph(owner, repo_name):
    """
    주어진 GitHub 리포지토리의 네트워크 그래프를 가져오는 함수.
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # 요청 실패 시 예외 발생
        commits = response.json()

        # 커밋과 브랜치 매핑
        commit_graph = {}
        for commit in commits:
            sha = commit['sha']
            commit_graph[sha] = {
                'message': commit['commit']['message'],
                'author': commit['commit']['author']['name'],
                'date': commit['commit']['author']['date'],
                'parents': commit.get('parents', [])
            }

        return commit_graph
    except Exception as e:
        print(f"네트워크 그래프를 가져오는 중 오류 발생: {e}")
        return {}

def print_commit_graph(commit_graph):
    """
    커밋 그래프를 출력하는 함수.
    """
    for sha, commit_info in commit_graph.items():
        parents = commit_info['parents']
        parent_shas = [parent['sha'] for parent in parents] if parents else ['None']
        
        # 부모 커밋 출력
        if len(parent_shas) == 1 and parent_shas[0] == 'None':
            print(f"{sha}")
        else:
            print(f"{parent_shas[0]}")
            for i in range(1, len(parent_shas)):
                print(f"├──{parent_shas[i]}")
        
        # 자식 커밋 출력
        for i in range(len(parent_shas)):
            if i == len(parent_shas) - 1:
                print(f"└──{sha}")
            else:
                print(f"│  {sha}")
        
        # print(f"| 메시지: {commit_info['message']} | 작성자: {commit_info['author']} | 날짜: {commit_info['date']}")
        # print()

if __name__ == "__main__":
    dotenv.load_dotenv()  # .env 파일 로드
    URL = os.environ.get('REPO_URL')
    
    if URL is None:
        print("REPO_URL 환경 변수가 설정되지 않았습니다.")
        exit(1)

    path_parts = URL.strip("/").split("/")
    owner = path_parts[3]  # 소유자
    repo_name = path_parts[4].replace('.git', '')  # 리포지토리 이름 (확장자 제거)

    # 네트워크 그래프 가져오기
    commit_graph = get_network_graph(owner, repo_name)
    
    # 커밋 그래프 출력
    print_commit_graph(commit_graph)
