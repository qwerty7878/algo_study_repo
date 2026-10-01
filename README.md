# SWEA 알고리즘 스터디

hyeonjune(Python) · wooseong(Java) — SWEA lv2부터, 하루 2문제씩

## 규칙
1. 각자 **자기 폴더**에만 올린다 (`hyeonjune/`, `wooseong/`)
2. 폴더 `이름/lv레벨/`, 파일명 `문제번호_제목.확장자`
3. 하루 2문제, 풀이 파일 상단에 **접근 / 시간복잡도 / 메모**를 간단히 적는다
4. 서로 풀이를 읽고 궁금한 점은 커밋/이슈 댓글로 남긴다

## 사용법
**처음 한 번**
```bash
git clone https://github.com/qwerty7878/algo_study_repo.git
cd algo_study_repo
```

**문제를 풀 때마다**
```bash
./new.sh 1204 최빈수구하기    # 풀이 파일 생성
# 파일을 열어 코드 붙여넣기 + 접근/시간복잡도/메모 작성
./push.sh                     # 내 폴더만 커밋 + push
```

`./new.sh`를 처음 실행하면 아래를 물어봅니다. (내 컴퓨터에만 저장되고 git에는 안 올라감)
```
내 폴더 이름 (예: hyeonjune): hyeonjune     # 우성: wooseong
사용 언어 확장자 (py / java / cpp): py       # 우성: java
```

**레벨**은 `./new.sh`를 실행할 때마다 물어봅니다. 기본값은 마지막에 쓴 레벨이라 같은 레벨이면 엔터만 치면 됩니다.
```
레벨 [2]: ↵      → hyeonjune/lv2/1204_최빈수구하기.py
레벨 [2]: 3      → hyeonjune/lv3/...   (이후 기본값은 3)
```
묻지 않고 바로 지정하려면 끝에 붙입니다: `./new.sh 1204 최빈수구하기 3`

**상대 풀이 보기**: `git pull`

push하면 아래 표는 GitHub Actions가 자동으로 갱신합니다.

## 진행 현황
<!-- STATUS:START -->
| 날짜 | hyeonjune | wooseong |
|---|---|---|
| 2026-10-01 | - | 1284 |
| 2026-09-29 | 1859 | - |
| **총합** | **1** | **1** |
<!-- STATUS:END -->
