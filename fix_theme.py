import os
import re

color_kt = """package com.example.ui.theme

import androidx.compose.ui.graphics.Color

val GreenBackgroundLight = Color(0xFFF5F7F2)
val GreenSurfaceLight = Color(0xFFFFFFFF)
val GreenPrimaryLight = Color(0xFF2C5535)
val GreenOnPrimaryLight = Color(0xFFFFFFFF)
val GreenPrimaryContainerLight = Color(0xFFC4E0C1)
val GreenOnPrimaryContainerLight = Color(0xFF0F2013)
val GreenSecondaryLight = Color(0xFF566956)
val GreenSurfaceVariantLight = Color(0xFFE8EBE3)
val GreenOnSurfaceVariantLight = Color(0xFF424941)

val GreenBackgroundDark = Color(0xFF0F1511)
val GreenSurfaceDark = Color(0xFF161F18)
val GreenPrimaryDark = Color(0xFFA8C4A5)
val GreenOnPrimaryDark = Color(0xFF102816)
val GreenPrimaryContainerDark = Color(0xFF2C5535)
val GreenOnPrimaryContainerDark = Color(0xFFC4E0C1)
val GreenSecondaryDark = Color(0xFF9CAEA0)
val GreenSurfaceVariantDark = Color(0xFF263328)
val GreenOnSurfaceVariantDark = Color(0xFFB0B9B0)
"""

theme_kt = """package com.example.ui.theme

import android.os.Build
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.dynamicDarkColorScheme
import androidx.compose.material3.dynamicLightColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.platform.LocalContext

private val DarkColorScheme = darkColorScheme(
    primary = GreenPrimaryDark,
    onPrimary = GreenOnPrimaryDark,
    primaryContainer = GreenPrimaryContainerDark,
    onPrimaryContainer = GreenOnPrimaryContainerDark,
    secondary = GreenSecondaryDark,
    background = GreenBackgroundDark,
    surface = GreenSurfaceDark,
    surfaceVariant = GreenSurfaceVariantDark,
    onSurfaceVariant = GreenOnSurfaceVariantDark
)

private val LightColorScheme = lightColorScheme(
    primary = GreenPrimaryLight,
    onPrimary = GreenOnPrimaryLight,
    primaryContainer = GreenPrimaryContainerLight,
    onPrimaryContainer = GreenOnPrimaryContainerLight,
    secondary = GreenSecondaryLight,
    background = GreenBackgroundLight,
    surface = GreenSurfaceLight,
    surfaceVariant = GreenSurfaceVariantLight,
    onSurfaceVariant = GreenOnSurfaceVariantLight
)

@Composable
fun MyApplicationTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = false, // Force custom theme for design consistency
    isAmoled: Boolean = false,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        isAmoled && darkTheme -> DarkColorScheme.copy(
            background = androidx.compose.ui.graphics.Color.Black,
            surface = androidx.compose.ui.graphics.Color.Black
        )
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        }
        darkTheme -> DarkColorScheme
        else -> LightColorScheme
    }

    MaterialTheme(
        colorScheme = colorScheme,
        typography = Typography,
        shapes = Shapes,
        content = content
    )
}
"""

type_kt = """package com.example.ui.theme

import androidx.compose.material3.Typography
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp

val Typography = Typography(
    displayLarge = TextStyle(
        fontFamily = FontFamily.SansSerif,
        fontWeight = FontWeight.Bold,
        fontSize = 57.sp,
        lineHeight = 64.sp,
        letterSpacing = (-0.25).sp
    ),
    displayMedium = TextStyle(
        fontFamily = FontFamily.SansSerif,
        fontWeight = FontWeight.Bold,
        fontSize = 45.sp,
        lineHeight = 52.sp,
        letterSpacing = 0.sp
    ),
    headlineLarge = TextStyle(
        fontFamily = FontFamily.SansSerif,
        fontWeight = FontWeight.SemiBold,
        fontSize = 32.sp,
        lineHeight = 40.sp,
        letterSpacing = 0.sp
    ),
    titleLarge = TextStyle(
        fontFamily = FontFamily.SansSerif,
        fontWeight = FontWeight.SemiBold,
        fontSize = 22.sp,
        lineHeight = 28.sp,
        letterSpacing = 0.sp
    ),
    titleMedium = TextStyle(
        fontFamily = FontFamily.SansSerif,
        fontWeight = FontWeight.Medium,
        fontSize = 16.sp,
        lineHeight = 24.sp,
        letterSpacing = 0.15.sp
    ),
    bodyLarge = TextStyle(
        fontFamily = FontFamily.SansSerif,
        fontWeight = FontWeight.Normal,
        fontSize = 16.sp,
        lineHeight = 24.sp,
        letterSpacing = 0.5.sp
    ),
    bodyMedium = TextStyle(
        fontFamily = FontFamily.SansSerif,
        fontWeight = FontWeight.Normal,
        fontSize = 14.sp,
        lineHeight = 20.sp,
        letterSpacing = 0.25.sp
    ),
    labelMedium = TextStyle(
        fontFamily = FontFamily.SansSerif,
        fontWeight = FontWeight.Medium,
        fontSize = 12.sp,
        lineHeight = 16.sp,
        letterSpacing = 0.5.sp
    )
)
"""

shape_kt = """package com.example.ui.theme

import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Shapes
import androidx.compose.ui.unit.dp

val Shapes = Shapes(
    small = RoundedCornerShape(12.dp),
    medium = RoundedCornerShape(24.dp),
    large = RoundedCornerShape(32.dp)
)
"""

with open('app/src/main/java/com/example/ui/theme/Color.kt', 'w') as f:
    f.write(color_kt)
with open('app/src/main/java/com/example/ui/theme/Theme.kt', 'w') as f:
    f.write(theme_kt)
with open('app/src/main/java/com/example/ui/theme/Type.kt', 'w') as f:
    f.write(type_kt)
with open('app/src/main/java/com/example/ui/theme/Shape.kt', 'w') as f:
    f.write(shape_kt)

