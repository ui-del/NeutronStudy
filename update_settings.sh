#!/bin/bash
cat app/src/main/java/com/example/feature/settings/SettingsScreen.kt | sed 's/SliderSettingItem(/NumberInputSettingItem(/g' > tmp_settings.kt
mv tmp_settings.kt app/src/main/java/com/example/feature/settings/SettingsScreen.kt
