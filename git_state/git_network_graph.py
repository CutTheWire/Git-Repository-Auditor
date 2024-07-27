import dotenv
import os
import requests
import random
import networkx as nx
from pyvis.network import Network

# GitHub API에서 커밋 데이터를 가져오는 함수
def fetch_commits(owner, repo, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

# GitHub API에서 브랜치 정보를 가져오는 함수
def fetch_branches(owner, repo, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/branches'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching branches: {response.status_code}")
        return []
    return response.json()

# 특정 브랜치의 커밋을 가져오는 함수
def fetch_commits_for_branch(owner, repo, branch, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?sha={branch}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching commits for branch {branch}: {response.status_code}")
        return []
    return response.json()

# 파스텔 색상 생성 함수
def pastel_color():
    base_color = [random.random() for _ in range(3)]
    pastel_color = [(c + 0.5) / 2 for c in base_color]
    return pastel_color

# 브랜치의 커밋을 그래프에 추가하는 함수
def add_branch_commits_to_graph(G, branch_name, commits):
    for commit in commits:
        if isinstance(commit, dict):
            commit_sha = commit['sha'][:7]
            G.add_node(commit_sha, label=commit_sha, branch=branch_name)
            for parent in commit.get('parents', []):
                parent_sha = parent['sha'][:7]
                G.add_edge(parent_sha, commit_sha)

# 네트워크 그래프를 그리는 함수
def draw_network_graph(owner, repo, token):
    branches = fetch_branches(owner, repo, token)
    branch_commits = {}
    
    for branch in branches:
        if isinstance(branch, dict):
            branch_name = branch['name']
            branch_commits[branch_name] = fetch_commits_for_branch(owner, repo, branch_name, token)

    G = nx.DiGraph()
    branch_colors = {branch['name']: pastel_color() for branch in branches if isinstance(branch, dict)}

    # 각 브랜치의 커밋을 그래프에 추가
    for branch_name, commits in branch_commits.items():
        add_branch_commits_to_graph(G, branch_name, commits)

    # Pyvis 네트워크 생성
    net = Network(height='750px', width='100%', notebook=True, directed=True)

    # 노드 추가
    for node in G.nodes(data=True):
        node_id, data = node
        branch_name = data.get('branch')
        color = branch_colors.get(branch_name, (0.5, 0.5, 0.5))
        
        # 노드의 색상과 브랜치 이름을 표시하도록 설정
        net.add_node(node_id, 
                     label=node_id, 
                     title=f'Branch: {branch_name}', 
                     color=f'rgba({int(color[0]*255)}, {int(color[1]*255)}, {int(color[2]*255)}, 1)',
                     group=branch_name)  # 그룹으로 브랜치 이름 설정

    # 에지 추가
    for edge in G.edges():
        net.add_edge(edge[0], edge[1])

    # 그래프 시각화
    net.show("./Template/commit_network.html")

if __name__ == "__main__":
    dotenv.load_dotenv()  # .env 파일 로드
    URL = os.environ.get('REPO_URL')
    TOKEN = os.environ.get('GITHUB_TOKEN')
    path_parts = URL.strip("/").split("/")
    owner = path_parts[3]
    repo_name = path_parts[4].replace('.git', '')
    draw_network_graph(owner, repo_name, TOKEN)
