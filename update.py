#!/usr/bin/env python

import os
from urllib import parse

HEADER = """# 
# 리트코드, 백준 문제 풀이 목록

git actions을 사용해 만들었습니다.
리트코드에선 TypeScript, 백준에서는 Python3을 이용해 풀이했습니다.
"""

def main():
    content = ""
    content += HEADER
    
    directories = []
    solveds = []

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        
        if category == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            continue
            
        if directory not in directories:
            if directory in ["백준", "프로그래머스","Leetcode"]:
                content += "## 📚 {}\n".format(directory)
            else:
                content += "### 🚀 {}\n".format(directory)
                content += "<details>\n<summary>문제 목록 보기</summary>\n\n"
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
            directories.append(directory)

        for file in files:
            content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root, file)))

        # 디렉토리 목록이 끝나면 <details> 태그를 닫음
        if directory not in ["백준", "프로그래머스","Leetcode"]:
            content += "\n</details>\n"

    with open("README.md", "w") as fd:
        fd.write(content)
        
if __name__ == "__main__":
    main()
