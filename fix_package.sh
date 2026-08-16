#!/bin/bash
sed -i '1,2d' app/src/main/java/com/example/feature/settings/SettingsScreen.kt
sed -i '2iimport androidx.compose.runtime.collectAsState\nimport androidx.compose.runtime.getValue' app/src/main/java/com/example/feature/settings/SettingsScreen.kt
