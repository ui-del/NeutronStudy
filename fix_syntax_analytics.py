import os

with open('app/src/main/java/com/example/feature/analytics/AnalyticsScreen.kt', 'r') as f:
    content = f.read()

content = content.replace("import androidx.compose.ui.unit.sp\npackage com.example.feature.analytics\n", "package com.example.feature.analytics\nimport androidx.compose.ui.unit.sp\n")

with open('app/src/main/java/com/example/feature/analytics/AnalyticsScreen.kt', 'w') as f:
    f.write(content)
