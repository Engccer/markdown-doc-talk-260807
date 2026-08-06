# AI와 마크다운을 활용한 HWP·DOCX 등 구조화된 텍스트 문서 작성 사례

**https://engccer.github.io/markdown-doc-talk-260807/**

제45차 한국시각장애교육재활학회 학술대회 (2026. 8. 7. 금요일, 여의도 이룸센터) 분과 발표 슬라이드덱. 발표자는 김헌용(신명중학교 영어 교사, 함께하는장애인교원노동조합 위원장).

## 발표 내용

시각장애인이 오래 써 온 텍스트 중심의 문서 작성 방식이 AI 에이전트 시대에 효율적인 작업 방식이 되었다는 이야기다. 마크다운이 스크린 리더 사용자와 AI 에이전트 양쪽에 같은 이유로 편한 형식인 까닭을 짚고, 한글 문서를 다루는 스킬을 만들어 학교 업무에 쓴 사례 넷을 소개한 뒤, 이 변화가 시각장애인의 문서 작성과 권리 옹호에 주는 함의를 논의한다.

23장, 발표 시간 20분.

## 조작

| 키 | 동작 |
|---|---|
| 오른쪽 화살표, PageDown | 다음 슬라이드 |
| 왼쪽 화살표, PageUp, Backspace | 이전 슬라이드 |
| Home / End | 처음 / 마지막 슬라이드 |

상단에 토글 셋이 있다.

- **문서 모드**: 23장 전체를 한 페이지로 펼친다. 발표자 진도와 무관하게 제목 이동으로 자기 속도로 읽을 때 쓴다.
- **내레이션**: 슬라이드를 넘길 때 제목과 한 줄 요약을 음성으로 재생한다. 자기 스크린 리더 낭독과 겹치면 끈다.
- **효과음**: 슬라이드 전환음.

선택은 브라우저에 기억된다.

## 구성

```
index.html                 슬라이드 23장 (바닐라 HTML/CSS/JS, 외부 의존 없음)
narration/                 슬라이드별 내레이션 MP3 23개 (ElevenLabs)
sfx/page-turn.mp3          전환 효과음
_generate_narration.py     내레이션 생성 스크립트
```

## 발표에서 소개한 도구

- [시각장애인을 위한 스킬 모음 (skills-for-the-blind)](https://github.com/Engccer/skills-for-the-blind)
- [한글 문서 자동화 스킬 (hwpx-automation)](https://github.com/Engccer/hwpx-automation)
- [HWPX를 마크다운으로 바꾸는 변환기 (hwpx-tomd)](https://github.com/Engccer/hwpx-tomd)
- [시각장애 교원 AI·에듀테크 접근성 매뉴얼](https://senedtecha11y.com)
