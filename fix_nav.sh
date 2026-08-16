#!/bin/bash
sed -i 's/onNavigateToSettings: () -> Unit,/onNavigateToSettings: () -> Unit,\n    onNavigateToRevision: () -> Unit,\n    onNavigateToExam: () -> Unit,/g' app/src/main/java/com/example/feature/timer/TimerScreen.kt

sed -i '/IconButton(onClick = onNavigateToSettings)/i \
                        IconButton(onClick = onNavigateToRevision) {\n                            Icon(androidx.compose.material.icons.Icons.Default.Schedule, contentDescription = "Revision")\n                        }\n                        IconButton(onClick = onNavigateToExam) {\n                            Icon(androidx.compose.material.icons.Icons.Default.School, contentDescription = "Exam")\n                        }' app/src/main/java/com/example/feature/timer/TimerScreen.kt

cat << 'INNER_EOF' > app/src/main/java/com/example/core/navigation/NeutronNavHost.kt.fix
package com.example.core.navigation

import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.core.di.AppContainer
import com.example.feature.timer.TimerScreen
import com.example.feature.subjects.SubjectsScreen
import com.example.feature.analytics.AnalyticsScreen
import com.example.feature.settings.SettingsScreen
import com.example.feature.auth.AuthScreen
import com.example.feature.auth.OnboardingScreen
import com.example.feature.goals.GoalsScreen
import com.example.feature.revision.RevisionScreen
import com.example.feature.exam.ExamModeScreen

@Composable
fun NeutronNavHost(
    appContainer: AppContainer,
    modifier: Modifier = Modifier,
    navController: NavHostController = rememberNavController(),
    startDestination: String = "auth"
) {
    NavHost(
        navController = navController,
        startDestination = startDestination,
        modifier = modifier
    ) {
        composable("auth") {
            AuthScreen(
                onLoginSuccess = { 
                    navController.navigate("onboarding") {
                        popUpTo("auth") { inclusive = true }
                    }
                }
            )
        }
        composable("onboarding") {
            OnboardingScreen(
                onFinishOnboarding = {
                    navController.navigate("timer") {
                        popUpTo("onboarding") { inclusive = true }
                    }
                }
            )
        }
        composable("timer") {
            TimerScreen(
                appContainer = appContainer,
                onNavigateToSubjects = { navController.navigate("subjects") },
                onNavigateToAnalytics = { navController.navigate("analytics") },
                onNavigateToSettings = { navController.navigate("settings") },
                onNavigateToGoals = { navController.navigate("goals") },
                onNavigateToRevision = { navController.navigate("revision") },
                onNavigateToExam = { navController.navigate("exam") }
            )
        }
        composable("subjects") {
            SubjectsScreen(
                appContainer = appContainer,
                onNavigateBack = { navController.popBackStack() }
            )
        }
        composable("goals") {
            GoalsScreen(
                appContainer = appContainer,
                onNavigateBack = { navController.popBackStack() }
            )
        }
        composable("analytics") {
            AnalyticsScreen(
                appContainer = appContainer,
                onNavigateBack = { navController.popBackStack() }
            )
        }
        composable("settings") {
            SettingsScreen(
                appContainer = appContainer,
                onNavigateBack = { navController.popBackStack() }
            )
        }
        composable("revision") {
            RevisionScreen(
                appContainer = appContainer,
                onNavigateBack = { navController.popBackStack() }
            )
        }
        composable("exam") {
            ExamModeScreen(
                appContainer = appContainer,
                onNavigateBack = { navController.popBackStack() }
            )
        }
    }
}
INNER_EOF
mv app/src/main/java/com/example/core/navigation/NeutronNavHost.kt.fix app/src/main/java/com/example/core/navigation/NeutronNavHost.kt
