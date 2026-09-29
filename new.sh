#!/usr/bin/env bash
# 사용법: ./new.sh <문제번호> <제목> [레벨=2]
# 예시:   ./new.sh 1204 최빈수구하기
set -e
cd "$(dirname "$0")"

if [ $# -lt 2 ]; then
  echo "사용법: ./new.sh <문제번호> <제목> [레벨=2]"
  exit 1
fi

CONF=.study.conf
if [ ! -f "$CONF" ]; then
  read -rp "내 폴더 이름 (예: hyeonjune): " MY_DIR
  read -rp "사용 언어 확장자 (py / java / cpp): " EXT
  printf 'MY_DIR=%s\nEXT=%s\n' "$MY_DIR" "$EXT" > "$CONF"
fi
source "$CONF"

NUM=$1; TITLE=$2; LV=${3:-2}
DIR="$MY_DIR/lv$LV"
FILE="$DIR/${NUM}_${TITLE}.$EXT"

if [ -e "$FILE" ]; then
  echo "이미 있음: $FILE"
  exit 0
fi

mkdir -p "$DIR"
case "$EXT" in
  py)   C="#" ;;
  *)    C="//" ;;
esac
{
  echo "$C 문제: $NUM $TITLE"
  echo "$C 링크: https://swexpertacademy.com/main/code/problem/problemList.do (번호 $NUM 검색)"
  echo "$C 날짜: $(date +%Y-%m-%d)"
  echo "$C"
  echo "$C [접근] 어떻게 풀었는지 / 왜 이 방식인지"
  echo "$C [시간복잡도] O(?)"
  echo "$C [메모] 막혔던 점, 배운 점"
  echo
  if [ "$EXT" = "java" ]; then
    echo "import java.util.*;"
    echo "import java.io.*;"
    echo
    echo "class Solution {"
    echo "    public static void main(String[] args) throws Exception {"
    echo "        "
    echo "    }"
    echo "}"
  fi
} > "$FILE"
echo "생성됨: $FILE"
