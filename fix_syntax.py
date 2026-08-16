import os

with open('app/src/main/java/com/example/feature/timer/TimerScreen.kt', 'r') as f:
    content = f.read()

content = content.replace("import androidx.compose.ui.graphics.Color\npackage com.example.feature.timer\n", "package com.example.feature.timer\nimport androidx.compose.ui.graphics.Color\n")

with open('app/src/main/java/com/example/feature/timer/TimerScreen.kt', 'w') as f:
    f.write(content)
