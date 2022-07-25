#!/bin/bash

: '
Get directory that script is in
'
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

SCRIPT_DIR="${SCRIPT_DIR}/airnefpictures"

gphotofs $SCRIPT_DIR
