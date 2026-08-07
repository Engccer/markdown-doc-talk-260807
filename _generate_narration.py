"""
슬라이드 23장 내레이션 생성. ElevenLabs eleven_v3, Hyunsu 음성.

내레이션은 슬라이드 제목과 한 줄 키워드까지만 담는다. 본문은 스크린 리더가
읽으므로 같은 내용을 다시 읽으면 중복이 된다.

약어·영문 표기·숫자는 TTS가 철자를 그대로 읽어 버리므로 한글 발음으로 적는다
(txt는 "티엑스티", 제45차는 "제 사십오차").

    python _generate_narration.py            # 없는 것만 생성
    python _generate_narration.py --force    # 전부 다시 생성
"""
import os
import sys
from pathlib import Path

VOICE_ID = "cuXUjH0CSJkKipo0Hy9i"  # Hyunsu: 한국어 남성, 팟캐스트 진행 톤
MODEL_ID = "eleven_v3"
OUT_DIR = Path(__file__).parent / "narration"

NARRATIONS = {
    1: "에이아이와 마크다운을 활용한 구조화된 텍스트 문서 작성 사례. 제 사십오차 한국시각장애교육재활학회 학술대회",
    2: "시험 원안은 메모장에서 작성했습니다",
    3: "약점이 강점으로 바뀌다",
    4: "오늘 말씀드릴 것. 네 가지",
    5: "티엑스티가 담지 못하는 것",
    6: "스크린 리더 사용자에게 무엇이 달라지는가",
    7: "검색 엔진의 크롤러도 같은 방식으로 웹을 읽습니다",
    8: "스크린 리더가 읽기 좋은 형식은 에이아이 에이전트에게도 좋습니다",
    9: "권장하는 마크다운 중심 문서 작업 순서. 파싱, 확정, 변환",
    10: "한글 문서만 이 순서에 들어오지 못합니다",
    11: "스킬이란 무엇인가",
    12: "왜 한글 문서에 스킬이 필요한가",
    13: "스킬이 하는 세 가지 일. 읽기, 채우기, 만들기. 그리고 대조",
    14: "학교 업무에서의 활용 사례",
    15: "세 번째 대조에서 찾은 것",
    16: "관통하는 흐름과 검증의 층위",
    17: "기계가 채우지 못하는 것은 정확도가 아니라 책임 공백",
    18: "마지막 구간 처리까지 완주",
    19: "권리 옹호는 문서로 이루어집니다",
    20: "약점이 강점이 되는 조건",
    21: "남은 과제 셋",
    22: "나가며. 능력의 문제가 아니라 형식의 문제였습니다",
    23: "공개해 둔 도구",
}


def main():
    force = "--force" in sys.argv

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        sys.exit("ELEVENLABS_API_KEY env var not set")

    from elevenlabs import ElevenLabs, VoiceSettings

    client = ElevenLabs(api_key=api_key)
    OUT_DIR.mkdir(exist_ok=True)

    made = 0
    for num, text in sorted(NARRATIONS.items()):
        mp3_path = OUT_DIR / f"slide-{num:02d}.mp3"
        if mp3_path.exists() and not force:
            print(f"[{num:02d}] skip (exists)")
            continue

        print(f"[{num:02d}] {text}")
        audio = client.text_to_speech.convert(
            voice_id=VOICE_ID,
            model_id=MODEL_ID,
            text=text,
            voice_settings=VoiceSettings(
                stability=0.5,
                similarity_boost=0.75,
                style=0.0,
                use_speaker_boost=True,
                speed=1.0,
            ),
        )
        mp3_path.write_bytes(b"".join(audio))
        made += 1

    print(f"\nDone. {made} generated, {len(NARRATIONS) - made} skipped.")


if __name__ == "__main__":
    main()
