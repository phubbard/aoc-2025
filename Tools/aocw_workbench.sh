#!/bin/bash
#
# Copyright 2025 Scale Invariant, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Brad Hyslop <bhyslop@scaleinvariant.org>
#
# AOCW Workbench - AOC-2025 project workbench commands

set -euo pipefail

# Get script directory
AOCW_SCRIPT_DIR="${BASH_SOURCE[0]%/*}"

# Source dependencies
source "${AOCW_SCRIPT_DIR}/buk/buc_command.sh"

# Verbose output if BUD_VERBOSE is set
aocw_show() {
  test "${BUD_VERBOSE:-0}" != "1" || echo "AOCWSHOW: $*"
}

# Load BURC configuration
aocw_load_burc() {
  local z_burc_file="${PWD}/.buk/burc.env"

  test -f "${z_burc_file}" || buc_die "BURC file not found: ${z_burc_file}"

  aocw_show "Loading BURC from: ${z_burc_file}"
  # shellcheck disable=SC1090
  source "${z_burc_file}"
}

# SlickEdit project configuration
AOCW_VSEP_TEMPLATE_DIR="Tools/vsaoc"
AOCW_VSEP_DEST_DIR="../_vs/aoc-2025"

# Simple routing function
aocw_route() {
  local z_command="$1"
  shift
  local z_args="$*"

  aocw_show "Routing command: ${z_command} with args: ${z_args}"

  # Verify BUD environment variables are present
  test -n "${BUD_TEMP_DIR:-}" || buc_die "BUD_TEMP_DIR not set - must be called from BUD"
  test -n "${BUD_NOW_STAMP:-}" || buc_die "BUD_NOW_STAMP not set - must be called from BUD"

  aocw_show "BUD environment verified"

  # Load BURC configuration
  aocw_load_burc

  # Route based on command
  case "${z_command}" in

    # SlickEdit project builder
    aocw-vsb)
      buc_step "Visual SlickEdit Project Builder"

      local z_template_dir="${PWD}/${AOCW_VSEP_TEMPLATE_DIR}"
      local z_dest_dir="${PWD}/${AOCW_VSEP_DEST_DIR}"

      # Validate template directory exists
      test -d "${z_template_dir}" || buc_die "Template directory not found: ${z_template_dir}"

      # Step 1: Delete destination (fail if delete fails - catches held file handles)
      if [ -d "${z_dest_dir}" ]; then
        buc_step "Removing existing SlickEdit project directory"
        aocw_show "Deleting: ${z_dest_dir}"
        rm -rf "${z_dest_dir}" || buc_die "Failed to delete ${z_dest_dir} - is SlickEdit still open?"

        # Verify deletion succeeded
        test ! -d "${z_dest_dir}" || buc_die "Directory still exists after delete: ${z_dest_dir}"
      fi

      # Step 2: Create fresh destination directory
      buc_step "Creating fresh SlickEdit project directory"
      mkdir -p "${z_dest_dir}" || buc_die "Failed to create directory: ${z_dest_dir}"

      # Step 3: Copy template files
      buc_step "Copying SlickEdit project templates"
      cp "${z_template_dir}"/* "${z_dest_dir}/" || buc_die "Failed to copy templates"

      # Report success
      local z_file_count
      z_file_count=$(ls -1 "${z_dest_dir}" | wc -l | tr -d ' ')
      buc_success "SlickEdit project created: ${z_dest_dir} (${z_file_count} files)"
      ;;

    # Unknown command
    *)
      buc_die "Unknown command: ${z_command}\nAvailable commands:\n  aocw-vsb  Visual SlickEdit Project Builder"
      ;;
  esac
}

aocw_main() {
  local z_command="${1:-}"
  shift || true

  test -n "${z_command}" || buc_die "No command specified"

  aocw_route "${z_command}" "$@"
}

aocw_main "$@"

# eof
