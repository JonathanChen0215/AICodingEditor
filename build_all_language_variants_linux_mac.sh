#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
rm -rf build/classes dist/language-variants
mkdir -p build/classes dist/language-variants
javac -encoding UTF-8 -d build/classes AICodingEditor.java
build_variant() {
  local folder="$1"
  local suffix="$2"
  cp "Language_Defaults/${folder}/AICodingEditor_Default_Language.properties" AICodingEditor_Default_Language.properties
  jar cfm "dist/language-variants/AICodingEditor_V0.2.99-01a_${suffix}.jar" META-INF/MANIFEST.MF \
    -C build/classes . \
    AICodingEditor.java AICodingEditor_Default_Language.properties Manuals Examples
}
build_variant English English_Default
build_variant Traditional_Chinese Traditional_Chinese_Default
build_variant Simplified_Chinese Simplified_Chinese_Default
cp Language_Defaults/English/AICodingEditor_Default_Language.properties AICodingEditor_Default_Language.properties
printf 'Built all language variants in %s/dist/language-variants\n' "$(pwd)"
