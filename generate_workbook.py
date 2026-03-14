#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Git 입문 교재 워크북 생성 스크립트
각 장별 실습 문제와 정답지를 생성합니다.
"""

import os
import re

# 각 장별 문제 템플릿
CHAPTER_PROBLEMS = {
    1: [
        {
            "type": "객관식",
            "question": "Git의 가장 기본적인 역할은 무엇인가요?",
            "options": ["파일 압축", "버전 관리", "파일 복사", "프로그래밍 언어"],
            "answer": "B",
            "difficulty": "⭐"
        },
        {
            "type": "단답형",
            "question": "Git을 설치하고 버전을 확인하는 명령어는?",
            "answer": "git --version",
            "difficulty": "⭐"
        },
        {
            "type": "객관식",
            "question": "git config --global user.name의 역할은?",
            "options": ["컴퓨터 이름 설정", "사용자 이름 전역 설정", "파일명 설정", "저장소 이름 설정"],
            "answer": "B",
            "difficulty": "⭐"
        },
        {
            "type": "실습",
            "question": "첫 번째 Git 저장소 만들기",
            "steps": [
                "mkdir git-practice",
                "cd git-practice",
                "git init",
                "git status로 확인"
            ],
            "difficulty": "⭐"
        },
        {
            "type": "서술형",
            "question": "Local Repository와 Remote Repository의 차이를 설명하세요.",
            "hint": "로컬은 내 컴퓨터, 리모트는...",
            "difficulty": "⭐⭐"
        },
        {
            "type": "객관식",
            "question": "다음 중 Git을 사용하는 가장 큰 이유는?",
            "options": ["프로그래밍을 쉽게", "변경 이력 관리", "컴퓨터 성능 향상", "파일 크기 감소"],
            "answer": "B",
            "difficulty": "⭐"
        },
        {
            "type": "단답형",
            "question": "새로운 Git 저장소를 초기화하는 명령어는?",
            "answer": "git init",
            "difficulty": "⭐"
        },
        {
            "type": "객관식",
            "question": "git status 명령어의 역할은?",
            "options": ["파일 삭제", "저장소 상태 확인", "파일 이동", "커밋"],
            "answer": "B",
            "difficulty": "⭐"
        },
    ],
    2: [
        {
            "type": "객관식",
            "question": "git add의 역할은?",
            "options": ["파일을 저장소에 저장", "변경사항을 스테이징 영역에 추가", "파일을 원격 저장소에 업로드", "브랜치를 생성"],
            "answer": "B",
            "difficulty": "⭐"
        },
        {
            "type": "단답형",
            "question": "모든 변경사항을 스테이징 영역에 추가하는 명령어는?",
            "answer": "git add .",
            "difficulty": "⭐"
        },
        {
            "type": "객관식",
            "question": "git commit의 역할은?",
            "options": ["파일 생성", "스테이징 된 변경사항을 저장소에 저장", "파일 삭제", "브랜치 생성"],
            "answer": "B",
            "difficulty": "⭐"
        },
        {
            "type": "실습",
            "question": "파일 수정 및 커밋하기",
            "steps": [
                "README.md 파일 생성",
                "git add README.md",
                "git commit -m '초기 커밋'",
                "git log로 확인"
            ],
            "difficulty": "⭐"
        },
        {
            "type": "단답형",
            "question": "원격 저장소로 코드를 업로드하는 명령어는?",
            "answer": "git push",
            "difficulty": "⭐⭐"
        },
        {
            "type": "객관식",
            "question": "git pull의 역할은?",
            "options": ["파일을 삭제", "원격 저장소의 최신 코드를 가져오기", "커밋 생성", "브랜치 생성"],
            "answer": "B",
            "difficulty": "⭐"
        },
        {
            "type": "서술형",
            "question": "add, commit, push의 순서와 각각의 역할을 설명하세요.",
            "hint": "스테이징 → 저장 → 업로드",
            "difficulty": "⭐⭐"
        },
        {
            "type": "단답형",
            "question": "커밋 메시지를 남기면서 커밋하는 명령어는?",
            "answer": "git commit -m '메시지'",
            "difficulty": "⭐"
        },
        {
            "type": "객관식",
            "question": "git log의 역할은?",
            "options": ["파일 생성", "커밋 이력 확인", "파일 수정", "저장소 삭제"],
            "answer": "B",
            "difficulty": "⭐"
        },
        {
            "type": "실습",
            "question": "원격 저장소와 연결하기",
            "steps": [
                "GitHub에 저장소 생성",
                "git remote add origin <URL>",
                "git push -u origin main",
                "git status로 확인"
            ],
            "difficulty": "⭐⭐"
        },
    ],
    3: [
        {
            "type": "객관식",
            "question": "브랜치의 역할은?",
            "options": ["파일 삭제", "독립적인 작업 공간 생성", "코드 압축", "파일 이동"],
            "answer": "B",
            "difficulty": "⭐"
        },
        {
            "type": "단답형",
            "question": "새로운 브랜치를 생성하는 명령어는?",
            "answer": "git branch <브랜치명>",
            "difficulty": "⭐"
        },
        {
            "type": "실습",
            "question": "브랜치 생성 및 전환하기",
            "steps": [
                "git branch feature",
                "git checkout feature",
                "파일 수정",
                "git status로 확인"
            ],
            "difficulty": "⭐"
        },
        {
            "type": "객관식",
            "question": "git merge의 역할은?",
            "options": ["브랜치 생성", "다른 브랜치의 변경사항을 현재 브랜치에 병합", "파일 복사", "저장소 삭제"],
            "answer": "B",
            "difficulty": "⭐⭐"
        },
        {
            "type": "서술형",
            "question": "merge conflict가 발생했을 때 해결하는 방법을 설명하세요.",
            "hint": "파일을 열어서 충돌 부분을 수정",
            "difficulty": "⭐⭐⭐"
        },
        {
            "type": "단답형",
            "question": "현재 브랜치를 확인하는 명령어는?",
            "answer": "git branch",
            "difficulty": "⭐"
        },
        {
            "type": "객관식",
            "question": "Pull Request(PR)의 역할은?",
            "options": ["파일 생성", "코드 리뷰 및 병합 요청", "브랜치 삭제", "저장소 생성"],
            "answer": "B",
            "difficulty": "⭐⭐"
        },
        {
            "type": "실습",
            "question": "브랜치 병합하기",
            "steps": [
                "git checkout main",
                "git merge feature",
                "git log로 확인",
                "git branch -d feature로 브랜치 삭제"
            ],
            "difficulty": "⭐⭐"
        },
        {
            "type": "단답형",
            "question": "특정 브랜치로 전환하는 명령어는?",
            "answer": "git checkout <브랜치명>",
            "difficulty": "⭐"
        },
        {
            "type": "서술형",
            "question": "협업 시 브랜치 전략의 중요성을 설명하세요.",
            "hint": "동시 작업, 충돌 방지",
            "difficulty": "⭐⭐⭐"
        },
    ],
    4: [
        {
            "type": "객관식",
            "question": "git revert의 역할은?",
            "options": ["파일 삭제", "이전 커밋을 새로운 커밋으로 되돌리기", "브랜치 생성", "저장소 삭제"],
            "answer": "B",
            "difficulty": "⭐⭐"
        },
        {
            "type": "단답형",
            "question": "특정 커밋을 되돌리는 안전한 명령어는?",
            "answer": "git revert <커밋해시>",
            "difficulty": "⭐⭐"
        },
        {
            "type": "객관식",
            "question": "git reset의 역할은?",
            "options": ["파일 복사", "HEAD를 특정 커밋으로 이동", "브랜치 생성", "파일 이동"],
            "answer": "B",
            "difficulty": "⭐⭐⭐"
        },
        {
            "type": "서술형",
            "question": "git reset과 git revert의 차이를 설명하세요.",
            "hint": "history 변경 여부",
            "difficulty": "⭐⭐⭐"
        },
        {
            "type": "실습",
            "question": "실수로 add한 파일 취소하기",
            "steps": [
                "파일 수정",
                "git add .",
                "git reset HEAD <파일명>",
                "git status로 확인"
            ],
            "difficulty": "⭐⭐"
        },
        {
            "type": "단답형",
            "question": "변경사항을 임시 저장하는 명령어는?",
            "answer": "git stash",
            "difficulty": "⭐⭐"
        },
        {
            "type": "객관식",
            "question": "git stash의 역할은?",
            "options": ["파일 생성", "현재 변경사항을 임시로 저장", "파일 삭제", "커밋"],
            "answer": "B",
            "difficulty": "⭐⭐"
        },
        {
            "type": "단답형",
            "question": "stash에 저장된 변경사항을 복원하는 명령어는?",
            "answer": "git stash pop",
            "difficulty": "⭐⭐"
        },
    ],
    5: [
        {
            "type": "서술형",
            "question": "상황: 실수로 main에 merge했을 때 복구 방법을 설명하세요.",
            "hint": "git revert 또는 git reset",
            "difficulty": "⭐⭐⭐"
        },
        {
            "type": "시뮬레이션",
            "question": "여러 커밋을 하나로 정리해야 할 때의 방법은?",
            "options": ["git rebase -i", "git cherry-pick", "git stash", "git reset"],
            "answer": "A",
            "difficulty": "⭐⭐⭐"
        },
        {
            "type": "서술형",
            "question": "파일을 실수로 삭제했을 때 복구하는 방법을 설명하세요.",
            "hint": "git checkout 또는 이전 커밋 복구",
            "difficulty": "⭐⭐"
        },
        {
            "type": "시뮬레이션",
            "question": "브랜치를 실수로 삭제했을 때 복구 방법은?",
            "options": ["git reflog", "git log", "git status", "git branch"],
            "answer": "A",
            "difficulty": "⭐⭐⭐"
        },
        {
            "type": "실습",
            "question": "cherry-pick으로 특정 커밋 적용하기",
            "steps": [
                "git log에서 적용할 커밋 해시 확인",
                "git cherry-pick <커밋해시>",
                "git log로 확인"
            ],
            "difficulty": "⭐⭐⭐"
        },
        {
            "type": "서술형",
            "question": "대규모 프로젝트에서 협업할 때 주의할 사항 3가지를 쓰세요.",
            "hint": "병합, 충돌, 커밋 메시지",
            "difficulty": "⭐⭐⭐"
        },
        {
            "type": "시뮬레이션",
            "question": "원격 저장소와 로컬이 동기화되지 않았을 때 해결 방법은?",
            "options": ["git pull", "git fetch", "git reset", "git status"],
            "answer": "A",
            "difficulty": "⭐⭐"
        },
        {
            "type": "서술형",
            "question": "좋은 커밋 메시지의 작성 기준 3가지를 설명하세요.",
            "hint": "명확한 제목, 상세한 설명, 일관성",
            "difficulty": "⭐⭐"
        },
        {
            "type": "실습",
            "question": "협업 시나리오: 두 명이 같은 파일 수정",
            "steps": [
                "브랜치 A, B 생성",
                "각각 파일 수정 및 커밋",
                "main에 merge",
                "conflict 해결"
            ],
            "difficulty": "⭐⭐⭐"
        },
        {
            "type": "서술형",
            "question": "자신이 배운 Git의 가장 유용한 기능 3가지와 이유를 작성하세요.",
            "hint": "자유로운 작성",
            "difficulty": "⭐"
        },
    ],
}

def create_html_workbook():
    """각 장별 워크북 HTML 생성"""

    for chapter_num in range(1, 6):
        problems = CHAPTER_PROBLEMS.get(chapter_num, [])

        html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Git 입문 교재 - {chapter_num}장 워크북</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
        }}
        h1 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        .problem {{
            margin: 30px 0;
            padding: 20px;
            border-left: 4px solid #667eea;
            background-color: #f9f9f9;
            border-radius: 5px;
        }}
        .problem-title {{
            font-weight: bold;
            font-size: 16px;
            color: #333;
            margin-bottom: 10px;
        }}
        .problem-type {{
            display: inline-block;
            background-color: #667eea;
            color: white;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 12px;
            margin-right: 10px;
        }}
        .difficulty {{
            font-size: 14px;
            color: #ff9800;
        }}
        .question {{
            margin-top: 10px;
            font-weight: 500;
            color: #333;
        }}
        .options {{
            margin: 15px 0;
            padding-left: 30px;
        }}
        .option {{
            margin: 8px 0;
        }}
        .blank {{
            border-bottom: 2px solid #333;
            display: inline-block;
            width: 400px;
            margin: 0 5px;
        }}
        .step {{
            margin: 10px 0;
            padding-left: 30px;
        }}
        .answer {{
            margin-top: 20px;
            padding: 15px;
            background-color: #e8f5e9;
            border-left: 4px solid #4caf50;
            border-radius: 3px;
            display: none;
        }}
        .answer.show {{
            display: block;
        }}
        .page-break {{
            page-break-after: always;
            margin: 50px 0;
        }}
        @media print {{
            .problem {{ page-break-inside: avoid; }}
            .page-break {{ page-break-after: always; }}
        }}
    </style>
</head>
<body>
    <h1>✏️ {chapter_num}장 워크북</h1>
    <p>다음 문제들을 풀고 자신의 이해도를 점검하세요.</p>
"""

        for i, problem in enumerate(problems, 1):
            html += f"""    <div class="problem">
        <div class="problem-title">
            <span class="problem-type">{problem['type']}</span>
            <span class="difficulty">{problem['difficulty']}</span>
        </div>
        <div class="question">Q{i}. {problem['question']}</div>
"""

            if problem["type"] == "객관식":
                html += '        <div class="options">\n'
                for j, option in enumerate(problem["options"], 1):
                    html += f'            <div class="option">{"ABCD"[j-1]}. {option}</div>\n'
                html += '        </div>\n'
                html += f'        <div class="blank"></div>\n'
                html += f'        <div class="answer"><strong>정답:</strong> {problem["answer"]}</div>\n'

            elif problem["type"] == "단답형":
                html += f'        <div class="blank"></div>\n'
                html += f'        <div class="answer"><strong>정답:</strong> {problem["answer"]}</div>\n'

            elif problem["type"] == "서술형":
                html += f'        <div style="margin: 10px 0; height: 100px; border: 1px solid #ddd; padding: 10px;"></div>\n'
                if "hint" in problem:
                    html += f'        <small style="color: #999;">💡 힌트: {problem["hint"]}</small>\n'

            elif problem["type"] == "실습":
                html += '        <div class="step"><strong>실습 단계:</strong></div>\n'
                html += '        <div class="options">\n'
                for step in problem["steps"]:
                    html += f'            <div class="option">□ {step}</div>\n'
                html += '        </div>\n'

            elif problem["type"] == "시뮬레이션":
                html += '        <div class="options">\n'
                for j, option in enumerate(problem.get("options", []), 1):
                    html += f'            <div class="option">{"ABCD"[j-1]}. {option}</div>\n'
                html += '        </div>\n'
                html += f'        <div class="blank"></div>\n'
                html += f'        <div class="answer"><strong>정답:</strong> {problem.get("answer", "자유 답변")}</div>\n'

            html += '    </div>\n'

        html += """
</body>
</html>
"""

        # 저장
        output_dir = "output/workbook"
        os.makedirs(output_dir, exist_ok=True)
        output_file = f"{output_dir}/chapter{chapter_num}_workbook.html"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"[OK] Chapter {chapter_num} 워크북 생성 완료: {output_file}")

def create_answer_key():
    """정답지 생성"""

    html = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Git 입문 교재 - 정답지</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.8;
            color: #333;
        }}
        h1 {{ color: #667eea; border-bottom: 3px solid #667eea; padding-bottom: 10px; }}
        h2 {{ color: #333; margin-top: 30px; }}
        .answer-block {{
            background-color: #e8f5e9;
            border-left: 4px solid #4caf50;
            padding: 15px;
            margin: 15px 0;
            border-radius: 3px;
        }}
        .question {{
            font-weight: bold;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <h1>📋 Git 입문 교재 - 정답지</h1>
    <p>본 정답지는 강사용 자료입니다.</p>
"""

    for chapter_num in range(1, 6):
        problems = CHAPTER_PROBLEMS.get(chapter_num, [])
        html += f'<h2>{chapter_num}장 정답</h2>\n'

        for i, problem in enumerate(problems, 1):
            html += f'<div class="answer-block">\n'
            html += f'<div class="question">Q{i}. {problem["question"]}</div>\n'

            if "answer" in problem:
                html += f'<strong>정답:</strong> {problem["answer"]}\n'

            if "hint" in problem:
                html += f'<div><strong>해설:</strong> {problem["hint"]}</div>\n'

            html += '</div>\n'

    html += """
</body>
</html>
"""

    output_file = "output/workbook/answer_key.html"
    os.makedirs("output/workbook", exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"[OK] 정답지 생성 완료: {output_file}")

def generate_workbook():
    """워크북 생성 메인 함수"""

    print("[*] Git 입문 교재 워크북 생성 시작...")
    create_html_workbook()
    create_answer_key()
    print("\n[OK] 워크북 생성 완료!")

if __name__ == "__main__":
    generate_workbook()
