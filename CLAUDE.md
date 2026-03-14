# CLAUDE.md - Git 입문 교재 프로젝트

This file provides guidance to Claude Code when working with this Git textbook project.

## 프로젝트 정보

- **제목**: Git 입문 교재 - 완전 가이드
- **대상 독자**: Git을 처음 배우는 개발자 (모든 OS 환경, 비프로그래머 포함)
- **목표**: Git의 기초부터 협업, 심화 기술까지 단계별로 습득
- **톤**: 친근하고 따라하기 쉬운 실무 중심 설명

## 개발 환경

- **OS**: 플랫폼 독립적 (Windows, Mac, Linux 모두 대응)
- **프로젝트 루트**: d:/dev/AI/claude/08.Git-JustDoIt
- **기술 스택**: Git (모든 버전), GitHub (협업 부분)

---

## Claude Code Agent Teams 운영

이 프로젝트는 **Claude Code Agent Teams** 기능을 사용하여 7명의 전문가 팀을 운영합니다.

### 에이전트 팀 구성

| 역할 | 담당 | 정의 파일 |
|------|------|----------|
| 📋 Team Lead (총괄 편집장) | 프로젝트 관리, 최종 승인 | agents/editor_in_chief.md |
| ✍️ Teammate: 기술 저자 | 콘텐츠 집필, 코드·SVG 작성 | agents/technical_author.md |
| 🔍 Teammate: 기술 리뷰어 | Git 명령어 정확성 검증 | agents/technical_reviewer.md |
| 🎓 Teammate: 초보자 독자 | 이해도/난이도 평가 | agents/beginner_reader.md |
| 📐 Teammate: 교육 설계자 | 학습 흐름, 실습 설계 | agents/instructional_designer.md |
| 🧠 Teammate: 교육심리전문가 | 학습 동기, 불안 관리 | agents/educational_psychologist.md |
| 🎤 Teammate: 교육전문강사 | 설명 품질, 비유 검증 | agents/expert_instructor.md |

### 챕터 집필 실행 (workflows/agent_team_workflow.md 참조)

```
Phase 1: 기획 회의 (3 teammates 병렬)
         → 챕터 구조, 학습 목표, 실습 설계

Phase 2: 초안 작성 (기술 저자 단독)
         → HTML 원고, SVG 다이어그램, 코드 예제

Phase 3: 병렬 리뷰 (4 teammates 동시)
         → 기술 정확성, 이해도, 교육 설계, 심리적 안전성

Phase 4: 종합 회의 및 수정
         → 피드백 통합, 최종 승인
```

### Agent Team 운영 규칙

1. **Team Lead = 편집장**: 현재 세션의 사용자가 항상 편집장 역할
2. **Teammate 생성 시**: agents/*.md 파일을 spawn prompt에 명시
3. **병렬 리뷰 필수**: 독립적 리뷰 작업은 동시에 실행
4. **파일 충돌 방지**:
   - 기술 저자만 HTML 수정
   - 리뷰어들은 review_logs/ 디렉토리에만 작성
5. **작업 완료 후**: "팀 정리해줘" 요청으로 팀 종료

---

## 프로젝트 아키텍처

### 디렉터리 구조

```
d:/dev/AI/claude/08.Git-JustDoIt/
├── .claude/
│   └── settings.json              # Agent Teams 활성화 설정
├── README.md                       # 프로젝트 소개
├── CLAUDE.md                       # 이 파일
├── TABLE_OF_CONTENTS.md           # 최종 확정 목차
├── index.html                     # 메인 페이지 (목차)
├── chapter1.html ~ chapter5.html  # 원고
├── agents/                        # 에이전트 정의 (7개)
│   ├── editor_in_chief.md
│   ├── technical_author.md
│   ├── technical_reviewer.md
│   ├── beginner_reader.md
│   ├── instructional_designer.md
│   ├── educational_psychologist.md
│   └── expert_instructor.md
├── workflows/                     # 워크플로우 문서
│   ├── agent_team_workflow.md
│   ├── chapter_writing.md
│   ├── review_meeting.md
│   └── quality_checklist.md
├── templates/                     # HTML 템플릿
│   ├── chapter_template.html
│   └── book_style.css
├── manuscripts/                   # 원고 HTML (버전 관리용)
├── code_examples/                 # Git 명령어 예제
├── figures/                       # SVG 다이어그램
├── review_logs/                   # 리뷰 기록
│   ├── chapter1_tech_review.md
│   ├── chapter1_beginner_review.md
│   └── ...
├── skills/                        # textbook-authoring 스킬
└── output/                        # 최종 산출물
    ├── ppt/                       # 강의 PPT
    ├── workbook/                  # 워크북
    └── docx/                      # Word 문서
```

### 원고 파일 규칙

**현재 상태**: index.html, chapter1~5.html이 루트에 위치 (최종본)

- **위치**: d:/dev/AI/claude/08.Git-JustDoIt/chapterN.html
- **CSS**: 인라인 스타일 (각 파일이 독립적으로 동작)
- **SVG**: figures/ 에 저장 후 <img> 또는 <embed>로 참조
- **코드**: <div class="code-block"><code> 형식

### 콘텐츠 구조

각 chapter는 다음 섹션을 포함합니다:

```html
<header>              <!-- 장 제목 및 소개 -->
<nav>                 <!-- 이전/다음 장 네비게이션 -->
<section>             <!-- 각 주제별 섹션 -->
  <h2>제목</h2>
  <p>설명</p>
  <div class="code-block">  <!-- 명령어 예제 -->
  <div class="step">        <!-- 따라하기 -->
  <div class="tip">         <!-- 팁 -->
  <div class="highlight">   <!-- 중요 정보 -->
  <table>              <!-- 참조 테이블 -->
</section>
<footer>               <!-- 다음 학습 유도 -->
```

---

## HTML 원고 필수 구조

### Aside 박스 종류

- `<div class="tip">` — 💡 실무 팁 / 유용한 정보
- `<div class="highlight">` — 📌 중요 정보 / 핵심 개념
- `<div class="step">` — 단계별 따라하기
- `<div class="code-block">` — 터미널 명령어 / 코드

### 색상 코드

- 1장 (시작하기): #667eea - #764ba2 (보라)
- 2장 (기본 작업): #2196F3 - #1976D2 (파랑)
- 3장 (협업하기): #FF9800 - #F57C00 (주황)
- 4장 (문제 해결): #f44336 - #d32f2f (빨강)
- 5장 (실전 상황): #9C27B0 - #6A1B9A (자주)

---

## 콘텐츠 품질 기준

### 작성 원칙

1. **초보자 친화**: 전문 용어 첫 등장 시 한글 설명
2. **각 절 분량**: 2000~4000자 (현재 충족)
3. **새 개념 시**: 비유/실생활 예시 필수
4. **실습**: 항상 성공 경험으로 끝나기
5. **감정 곡선**: 호기심 → 불안 → 이해 → 성취감

### 금지 사항

- ❌ ASCII art (SVG 사용)
- ❌ 영어만 나열 (한글 설명 필수)
- ❌ 이론만 설명 (예제 필수)
- ❌ 너무 복잡한 초반 내용

### 검증 기준 (최종 승인)

- Critical 이슈: 0개
- Major 이슈: 0개
- 초보자 이해도: ⭐⭐⭐ 이상
- 교육 설계: ⭐⭐⭐ 이상
- 심리적 안전성: ⭐⭐⭐ 이상

---

## 피드백 충돌 해결 우선순위

기술 리뷰와 교육 목표가 충돌할 때:

```
정확성 > 심리적 안전 > 이해도 > 분량
```

예시:
- **기술 정확성 vs 이해도**: 정확성 유지 + 비유/다이어그램 추가
- **인지 부하 vs 내용 충실**: 절 분할, 단계적 빌드업
- **학습 불안 vs 난이도**: 안심 장치 삽입

---

## 현재 교재 상태

| 항목 | 상태 | 설명 |
|------|------|------|
| 1장 시작하기 | ✅ 완성 | Git 기초, 설치, 첫 저장소 |
| 2장 기본 작업 | ✅ 완성 | add, commit, push, pull |
| 3장 협업하기 | ✅ 완성 | branch, merge, conflict, PR |
| 4장 문제 해결 | ✅ 완성 | revert, reset, stash, rebase |
| 5장 실전 상황 | ✅ 완성 | 실제 문제 5가지 해결 |
| SVG 다이어그램 | 🔄 필요 | 주요 개념별 시각화 |
| 품질 검증 | 🔄 진행중 | 7명 팀 리뷰 예정 |
| 산출물 생성 | ✅ 완성 | PPT (24 슬라이드), 워크북 (46 문제), Word |

---

## 다음 진행 단계

1. **에이전트 팀 구성**: agents/ 디렉토리에 7개 정의 파일 생성
2. **워크플로우 문서화**: workflows/ 디렉토리 파일 작성
3. **품질 검증**: 각 챕터를 4명 리뷰어가 동시 검증
4. **산출물 생성**: PPT, 워크북, Word 자동 생성

---

## 체크리스트

- [x] HTML 교재 5장 작성
- [x] 프로젝트 구조 정비
- [x] .claude/settings.json 생성
- [x] CLAUDE.md 작성
- [ ] README.md 작성
- [ ] TABLE_OF_CONTENTS.md 작성
- [x] agents/ 7개 정의 파일 생성
- [x] workflows/ 문서 작성
- [ ] SVG 다이어그램 작성
- [ ] 품질 검증 실행
- [x] 산출물 생성
  - [x] PPT 생성 (generate_ppt.py) - 24개 슬라이드
  - [x] 워크북 생성 (generate_workbook.py) - 46개 문제 + 정답지
  - [x] Word 생성 (generate_docx.py) - 36개 섹션

---

**Updated**: 2026-03-14
**Version**: 1.1
**Status**: 산출물 생성 완료
