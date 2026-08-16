import re

file_path = 'app/src/main/java/com/example/feature/timer/TimerScreen.kt'
with open(file_path, 'r') as f:
    content = f.read()

# Add missing imports
imports_to_add = [
    "import androidx.compose.material.icons.filled.PlayArrow",
    "import androidx.compose.material.icons.filled.Pause",
    "import androidx.compose.material.icons.filled.Refresh",
    "import androidx.compose.material.icons.filled.Stop"
]

for imp in imports_to_add:
    if imp not in content:
        content = content.replace("import androidx.compose.material.icons.Icons", f"import androidx.compose.material.icons.Icons\n{imp}")

# Fix the icon usages
content = content.replace("androidx.compose.material.icons.Icons.Filled.PlayArrow", "Icons.Filled.PlayArrow")
content = content.replace("androidx.compose.material.icons.Icons.Filled.Pause", "Icons.Filled.Pause")
content = content.replace("androidx.compose.material.icons.Icons.Filled.Refresh", "Icons.Filled.Refresh")
content = content.replace("androidx.compose.material.icons.Icons.Filled.Stop", "Icons.Filled.Stop")

with open(file_path, 'w') as f:
    f.write(content)
