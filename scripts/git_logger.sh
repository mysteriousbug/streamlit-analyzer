#!/bin/bash

cd $(git rev-parse --show-toplevel)

git add reports/*.txt
git commit -m "Auto: Added report at $(date '+%F %T')"
git push origin main