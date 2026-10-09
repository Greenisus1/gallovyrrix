#!/bin/bash
# pi-app-store: 1
# pi-app-store-category: games
# pi-app-store-description: Offline fullscreen hangman with random words or hidden second-player word entry.
set -eu
cd -- "$(dirname -- "$0")"
case "${1:-}" in
 install) python3 -c 'import curses;from pathlib import Path;[compile(p.read_bytes(),str(p),"exec") for p in Path(".").glob("*.py")]' ;;
 run) exec python3 gallovyrrix.py ;;
 *) echo 'Use: bash app-store.sh install|run';exit 1 ;;
esac
