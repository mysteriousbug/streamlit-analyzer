#!/bin/bash
git log --pretty=format:"%h - %an, %ar : %s" > git_stats.txt