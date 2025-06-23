#!/bin/bash

cd $(git rev-parse --show-toplevel)

# Load environment variable from .env file
source .env

# Set identity (optional)
git config user.name >/dev/null 2>&1 || git config user.name "Ananya Aithal"
git config user.email >/dev/null 2>&1 || git config user.email "your@email.com"

# Temporarily change remote to use PAT
git remote set-url origin https://mysteriousbug:${GITHUB_PAT}@github.com/mysteriousbug/streamlit-analyzer.git

# Push the commit
git add reports/*.txt
git commit -m "Auto: Added report at $(date '+%F %T')"
git push origin main

# Reset the remote (optional cleanup)
git remote set-url origin https://github.com/mysteriousbug/streamlit-analyzer.git
