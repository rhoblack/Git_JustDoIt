# 산출물 생성 가이드

## 📊 3가지 산출물

### 1️⃣ 강의 PPT (output/ppt/)
- **도구**: LibreOffice Impress 또는 Google Slides
- **형식**: .pptx
- **각 슬라이드**: 1개 섹션당 1-2개 슬라이드
- **포함 내용**: 텍스트, 이미지, 코드 블록

**생성 방법**:
```bash
# pptxgenjs 라이브러리 사용 (Node.js)
npm install pptxgenjs
# 또는 수동으로 만들기
```

### 2️⃣ 워크북 (output/workbook/)
- **형식**: HTML, DOCX, PDF
- **구성**: 실습 문제 + 빈 칸 채우기 + 연습 공간
- **각 장**: 5-10개 연습 문제

**생성 방법**:
```bash
# Python으로 HTML에서 워크북 생성
python generate_workbook.py
```

### 3️⃣ Word 교재 (output/docx/)
- **형식**: .docx (Microsoft Word)
- **구성**: 전체 교재를 한 파일로
- **포함**: 목차, 페이지 번호, 스타일

**생성 방법**:
```bash
# python-docx 또는 pandoc 사용
python generate_docx.py
```

---

## 🛠️ 간단한 생성 방법

### 방법 1: 수동 변환 (추천)

1. **Google Slides에서 PPT 만들기**
   - index.html을 화면에 띄우기
   - 각 섹션을 슬라이드로 변환
   - .pptx로 다운로드

2. **Google Docs에서 워크북 만들기**
   - chapter1.html 내용 복사
   - 연습 문제 추가
   - 빈 칸 만들기
   - PDF 또는 DOCX로 다운로드

### 방법 2: 자동 스크립트 (고급)

**Python 스크립트 예시**:
```python
from docx import Document
from docx.shared import Pt, Inches
import re
from html.parser import HTMLParser

# 1. HTML에서 텍스트 추출
class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

# 2. Word 문서 생성
doc = Document()
doc.add_heading('Git 입문 교재', 0)

# 3. 각 장별로 추가
for chapter in range(1, 6):
    filename = f'chapter{chapter}.html'
    with open(filename, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # HTML에서 텍스트 추출
    parser = HTMLTextExtractor()
    parser.feed(html_content)

    # Word에 추가
    doc.add_heading(f'{chapter}장', level=1)
    for text in parser.text:
        if text.strip():
            doc.add_paragraph(text.strip())

# 4. 저장
doc.save('output/docx/Git_입문_교재.docx')
```

---

## 📋 산출물 생성 체크리스트

### PPT 생성
- [ ] 각 장별 슬라이드 20~30장
- [ ] 주요 개념 다이어그램 포함
- [ ] 명령어 예제 스크린샷
- [ ] 스피커 노트 포함
- [ ] 색상 일관성 유지

### 워크북 생성
- [ ] 각 장별 5~10개 문제
- [ ] 정답지 별도 작성
- [ ] 난이도 표시 (초급/중급/고급)
- [ ] 학생이 쓸 공간 충분
- [ ] 깔끔한 레이아웃

### Word 교재 생성
- [ ] 전체 목차
- [ ] 페이지 번호
- [ ] 각 장별 페이지 나누기
- [ ] 하이퍼링크 작동
- [ ] 출판 품질 스타일

---

## 📊 권장 일정

| 산출물 | 소요 시간 | 우선순위 |
|--------|---------|---------|
| PPT | 3시간 | 🔴 높음 |
| 워크북 | 2시간 | 🟡 중간 |
| Word | 1시간 | 🟢 낮음 |

---

## 🎯 다음 단계

1. ✅ **HTML 교재 완성** (완료)
2. ✅ **에이전트 팀 정의** (완료)
3. 🔄 **PPT 생성** (시작)
4. 🔄 **워크북 생성** (시작)
5. 🔄 **Word 교재 생성** (시작)

---

**최종 산출물 위치**:
- output/ppt/ - 강의 PPT
- output/workbook/ - 학생 워크북
- output/docx/ - 출판용 교재

**작성일**: 2026-03-14
**버전**: 1.0
