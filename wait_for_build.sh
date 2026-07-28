#!/bin/bash
while ! ls dist/assets/main-*.js >/dev/null 2>&1; do
  sleep 1
done
