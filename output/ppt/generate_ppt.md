# PPT 생성 가이드 (Google Slides 수동 방식)

## 🎯 목표
HTML 교재 → Google Slides PPT로 변환

## 📋 각 장별 슬라이드 구성

### Chapter 1: 시작하기 (15장)

**슬라이드 1**: 제목 슬라이드
```
제목: 1️⃣ Git 시작하기
부제: Git의 기초부터 첫 저장소까지
```

**슬라이드 2-4**: 1.1 Git이란?
```
슬라이드 2:
- Git = 버전 관리 시스템
- "Word 파일을 v1, v2...로 저장하는 대신"

슬라이드 3:
- Git의 장점 5가지
  • 변경 기록 관리
  • 이전 버전 복구
  • 협업 용이
  • 브랜치 기능
  • 안전한 작업

슬라이드 4:
- Git 구조
  Local Repository ↔️ Remote Repository
```

**슬라이드 5-8**: 1.2 설치하기
```
슬라이드 5: Windows
- git-scm.com 방문
- 기본 설정으로 설치
- 스크린샷: [installation screenshot]

슬라이드 6: macOS
- brew install git
- 명령어 입력만 하면 됨

슬라이드 7: Linux
- sudo apt-get install git (Ubuntu)
- sudo yum install git (Fedora)

슬라이드 8: 설치 확인
- git --version
- ✅ 완료!
```

**슬라이드 9-10**: 1.3 사용자 정보 설정
```
슬라이드 9:
- git config --global user.name "이름"
- git config --global user.email "이메일"

슬라이드 10:
- 설정 확인
- git config user.name
- git config user.email
```

**슬라이드 11-15**: 1.4 첫 저장소 만들기
```
슬라이드 11: Step 1
- mkdir my-first-project

슬라이드 12: Step 2
- cd my-first-project

슬라이드 13: Step 3
- git init

슬라이드 14: 확인하기
- git status
- 화면 캡처

슬라이드 15: 축하합니다!
- 🎉 첫 Git 저장소 생성 완료!
- 다음: 2장 기본 작업
```

---

## 🎨 디자인 가이드

### 색상 (Chapter 1)
- 주색: #667eea (보라)
- 보조색: #764ba2 (진보라)
- 텍스트: #333333 (어두운 회색)
- 배경: #ffffff (흰색)

### 폰트
- 제목: 24-32pt (굵음)
- 본문: 18-20pt (보통)
- 코드: 14pt (monospace)

### 레이아웃
- 왼쪽: 이미지/코드 (60%)
- 오른쪽: 텍스트 설명 (40%)

---

## 📊 전체 슬라이드 수

| 장 | 슬라이드 |
|----|---------|
| 1 | 15장 |
| 2 | 20장 |
| 3 | 22장 |
| 4 | 18장 |
| 5 | 20장 |
| **합계** | **95장** |

---

## 🛠️ 자동 생성 (Python + pptxgenjs)

```python
# generate_ppt.py
from pptx import Presentation
from pptx.util import Inches, Pt
from html.parser import HTMLParser
import re

# HTML 파일 읽기
def extract_sections(html_file):
    """HTML에서 섹션 추출"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # <section> 태그 파싱
    sections = re.findall(r'<section>(.*?)</section>', content, re.DOTALL)
    return sections

# PPT 생성
def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # 각 장별로
    for chapter in range(1, 6):
        sections = extract_sections(f'chapter{chapter}.html')

        for i, section in enumerate(sections):
            # 제목 슬라이드
            slide = prs.slides.add_slide(prs.slide_layouts[1])
            title = slide.shapes.title
            title.text = f"Section {i+1}"

            # 내용 슬라이드
            content = slide.placeholders[1].text_frame
            # HTML에서 텍스트 추출하여 추가
            ...

    prs.save('output/ppt/Git_입문_강의.pptx')

# 실행
create_presentation()
```

---

## 📝 생성 후 체크리스트

- [ ] 각 슬라이드 텍스트 확인
- [ ] 코드 블록 형식 확인
- [ ] 이미지 삽입 확인
- [ ] 색상 일관성 확인
- [ ] 페이지 번호 추가
- [ ] 스피커 노트 추가
- [ ] 최종 검토

---

**생성 일자**: 2026-03-14
**상태**: 준비 완료 ✅
