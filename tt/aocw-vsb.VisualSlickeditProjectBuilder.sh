#!/bin/bash
# TabTarget - delegates to aocw workbench via launcher
exec "$(dirname "${BASH_SOURCE[0]}")/../.buk/launcher.aocw_workbench.sh" \
  "${0##*/}" "${@}"
