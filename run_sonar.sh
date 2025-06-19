#!/bin/bash

echo "Running SonarQube Analysis..."

sonar-scanner \
  -Dsonar.projectKey=streamlit-analyzer \
  -Dsonar.sources=app \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=$SONAR_TOKEN