#!/bin/bash
cat << 'INNER_EOF' > app/src/main/java/com/example/feature/timer/ZenModeEffect.kt
package com.example.feature.timer

import android.app.Activity
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.ui.platform.LocalContext
import androidx.core.view.WindowCompat
import androidx.core.view.WindowInsetsCompat
import androidx.core.view.WindowInsetsControllerCompat

@Composable
fun ZenModeLockTaskEffect() {
    val context = LocalContext.current
    DisposableEffect(Unit) {
        val activity = context as? Activity
        
        activity?.let {
            try {
                it.startLockTask()
            } catch (e: Exception) {
                // Ignore
            }
            
            val window = it.window
            val insetsController = WindowCompat.getInsetsController(window, window.decorView)
            
            insetsController.hide(WindowInsetsCompat.Type.systemBars())
            insetsController.systemBarsBehavior = WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE
        }
        
        onDispose {
            activity?.let {
                try {
                    it.stopLockTask()
                } catch (e: Exception) {
                    // Ignore
                }
                
                val window = it.window
                val insetsController = WindowCompat.getInsetsController(window, window.decorView)
                insetsController.show(WindowInsetsCompat.Type.systemBars())
            }
        }
    }
}
INNER_EOF
