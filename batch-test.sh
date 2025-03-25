#!/bin/bash

# modify code
FILE="./hello/code/index.py"
CURRENT_TIME=$(TZ=Asia/Shanghai date +"%Y-%m-%d %H:%M:%S UTC+8")
sed -i "s/# Modified on .*/# Modified on ${CURRENT_TIME}/" "$FILE"
echo "TIME: ${CURRENT_TIME}"

# push branches to trigger CI/CD
BRANCHES=("master" "aliyun" "knative" "multi-env")

for branch in "${BRANCHES[@]}"; do
  git checkout -B "$branch"
  git push --force-with-lease origin "$branch"  # 推送分支
  echo "Push branch [$branch] and trigger CI/CD."
done