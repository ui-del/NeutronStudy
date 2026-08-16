#!/bin/bash
cat << 'INNER_EOF' > app/src/main/java/com/example/feature/timer/ZenModeEffect.kt
package com.example.feature.timer

import android.app.Activity
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.ui.platform.LocalContext

@Composable
fun ZenModeLockTaskEffect() {
    val context = LocalContext.current
    DisposableEffect(Unit) {
        val activity = context as? Activity
        try {
            activity?.startLockTask()
        } catch (e: Exception) {
            // Ignore if lock task is not available or fails
        }
        
        onDispose {
            try {
                activity?.stopLockTask()
            } catch (e: Exception) {
                // Ignore
            }
        }
    }
}
INNER_EOF

# Inject this into ZenModeScreen
sed -i '/val view = LocalView.current/i \    ZenModeLockTaskEffect()' app/src/main/java/com/example/feature/timer/TimerScreen.kt
