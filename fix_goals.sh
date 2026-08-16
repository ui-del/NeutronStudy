#!/bin/bash
sed -i '/import androidx.compose.material.icons.filled.Flag/d' app/src/main/java/com/example/feature/goals/GoalsScreen.kt
sed -i '5iimport androidx.compose.material.icons.filled.Flag' app/src/main/java/com/example/feature/goals/GoalsScreen.kt
