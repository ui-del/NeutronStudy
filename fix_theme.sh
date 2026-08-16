#!/bin/bash
cat << 'INNER_EOF' > app/src/main/java/com/example/ui/theme/Theme.kt
package com.example.ui.theme

import android.os.Build
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.dynamicDarkColorScheme
import androidx.compose.material3.dynamicLightColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.graphics.Color

private val DarkColorScheme =  darkColorScheme(primary = Purple80, secondary = PurpleGrey80, tertiary = Pink80)

private val AmoledColorScheme = darkColorScheme(
    primary = Purple80, 
    secondary = PurpleGrey80, 
    tertiary = Pink80,
    background = Color.Black,
    surface = Color.Black,
    surfaceVariant = Color(0xFF121212)
)

private val LightColorScheme =  lightColorScheme(
    primary = Purple40,
    secondary = PurpleGrey40,
    tertiary = Pink40,
)

@Composable
fun MyApplicationTheme(
  darkTheme: Boolean = isSystemInDarkTheme(),
  // Dynamic color is available on Android 12+
  dynamicColor: Boolean = true,
  isAmoled: Boolean = false,
  content: @Composable () -> Unit,
) {
  val colorScheme =
    when {
      isAmoled -> AmoledColorScheme
      dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
        val context = LocalContext.current
        if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
      }
      darkTheme -> DarkColorScheme
      else -> LightColorScheme
    }

  MaterialTheme(colorScheme = colorScheme, typography = Typography, content = content)
}
INNER_EOF
