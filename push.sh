#!/usr/bin/env bash
# 사용법: ./push.sh   (내 폴더의 변경사항만 커밋하고 push)
set -e
cd "$(dirname "$0")"
source .study.conf 2>/dev/null || { echo "먼저 ./new.sh 를 한 번 실행하세요."; exit 1; }

git add "$MY_DIR"
if git diff --cached --quiet; then
  echo "올릴 변경사항이 없습니다."
  exit 0
fi

COUNT=$(git diff --cached --name-only --diff-filter=AM | grep -v .gitkeep | wc -l | tr -d ' ')
git commit -m "[SWEA] $(date +%Y-%m-%d) ${COUNT}문제 - $MY_DIR"
git pull --rebase origin main 2>/dev/null || true
git push -u origin main
