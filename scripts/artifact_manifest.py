#!/usr/bin/env python3
"""Inventory tracked Android artifacts without running, signing or publishing them."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--check', action='store_true')
args = parser.parse_args()
tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).decode().split('\0')
artifacts = []
for name in sorted(tracked):
    if Path(name).suffix.lower() not in {'.apk', '.aab'}:
        continue
    path = root / name
    with path.open('rb') as source:
        checksum = hashlib.file_digest(source, 'sha256').hexdigest()
    artifacts.append({'file': name, 'bytes': path.stat().st_size, 'sha256': checksum})
manifest = {'schemaVersion': 1, 'sourceRepository': 'nowis30/mobile-jeux-millionnaire',
            'sourceCommit': None, 'note': 'Source commit and Android signing identity are not established for these historical binaries.',
            'artifacts': artifacts}
expected = json.dumps(manifest, ensure_ascii=False, indent=2) + '\n'
target = root / 'artifact-manifest.json'
if args.check:
    if not target.exists() or target.read_text(encoding='utf-8') != expected:
        sys.exit('Artifact inventory differs. Review the binaries, then regenerate the manifest explicitly.')
    print(f'{len(artifacts)} tracked APK/AAB checksums verified.')
else:
    target.write_text(expected, encoding='utf-8')
    print(f'{len(artifacts)} tracked APK/AAB checksums written.')
