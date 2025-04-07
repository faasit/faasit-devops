#!/bin/bash

git checkout main

# modify code
FILE="./hello/code/index.py"
CURRENT_TIME=$(TZ=Asia/Shanghai date +"%Y-%m-%d %H:%M:%S UTC+8")
sed -i "s/\"deploy_time\": \".*\"/\"deploy_time\": \"${CURRENT_TIME}\"/" "$FILE"
echo "TIME: ${CURRENT_TIME}"

# commit code
git add "$FILE"
git commit -m "test on: ${CURRENT_TIME}"

# push branches to trigger CI/CD
# BRANCHES=("main" "aliyun" "knative" "k8s" "aliyun-canary" "knative-canary" "k8s-canary" "multi-env")
BRANCHES=("main" "aliyun" "aliyun-canary")

for branch in "${BRANCHES[@]}"; do
  git checkout -B "$branch"
  if [[ "$branch" == *"-canary" ]]; then
    sed -i 's/"isCanary": False/"isCanary": True/' "$FILE"
    git add "$FILE"
    git commit -m "Set isCanary to True for $branch on: ${CURRENT_TIME}"
  fi
  git push --force-with-lease origin "$branch"
  echo "Push branch [$branch] and trigger CI/CD."
done

git checkout main