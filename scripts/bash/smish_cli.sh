#!/bin/bash
if [ $# -eq 0 ]; then
  echo "Usage: smish_cli <message>"
  exit 1
fi

python -c "from smish_core.auto_router import AutoRouter; AutoRouter('cli').broadcast({'msg': '$1'})"
