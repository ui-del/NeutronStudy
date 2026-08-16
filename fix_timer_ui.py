import re

with open('app/src/main/java/com/example/feature/timer/TimerScreen.kt', 'r') as f:
    content = f.read()

# Add animation imports
if "import androidx.compose.animation" not in content:
    content = content.replace(
        "import androidx.compose.foundation.layout.width",
        "import androidx.compose.foundation.layout.width\nimport androidx.compose.animation.*\nimport androidx.compose.animation.core.*\nimport androidx.compose.foundation.shape.CircleShape"
    )

# Fix ZenModeScreen
zen_mode_old = """@Composable
fun ZenModeScreen(
    appContainer: AppContainer,
    uiState: TimerUiState,
    onPause: () -> Unit,
    onResume: () -> Unit,
    onExitZenMode: () -> Unit,
    onStop: () -> Unit
) {
    ZenModeLockTaskEffect()
    val view = LocalView.current
    DisposableEffect(Unit) {
        view.keepScreenOn = true
        onDispose {
            view.keepScreenOn = false
        }
    }
    var showNeutronPanel by remember { mutableStateOf(false) }
    Box(modifier = Modifier.fillMaxSize()) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(24.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            Text(
                text = "━━━━━━━━━━━━━━━━",
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            Spacer(modifier = Modifier.height(16.dp))
            Text(
                text = uiState.selectedSubject?.name?.uppercase() ?: "FOCUS",
                fontSize = 24.sp,
                fontWeight = FontWeight.Bold,
                letterSpacing = 4.sp
            )
            Spacer(modifier = Modifier.height(16.dp))
            if (uiState.activeTimerInfo.mode == TimerMode.POMODORO) {
                val stateText = when (uiState.activeTimerInfo.pomodoroState) {
                    com.example.domain.models.PomodoroState.FOCUS -> "FOCUS TIME"
                    com.example.domain.models.PomodoroState.SHORT_BREAK -> "SHORT BREAK"
                    com.example.domain.models.PomodoroState.LONG_BREAK -> "LONG BREAK"
                    null -> ""
                }
                Text(
                    text = "$stateText • CYCLE ${uiState.activeTimerInfo.pomodoroCyclesCompleted + 1}",
                    fontSize = 14.sp,
                    color = MaterialTheme.colorScheme.secondary,
                    letterSpacing = 2.sp
                )
                Spacer(modifier = Modifier.height(16.dp))
            }
            Text(
                text = uiState.formattedTime,
                fontSize = 80.sp,
                fontWeight = FontWeight.Light,
                color = MaterialTheme.colorScheme.primary
            )
            Spacer(modifier = Modifier.height(16.dp))
            Text(
                text = "FOCUS MODE",
                fontSize = 18.sp,
                fontWeight = FontWeight.Medium,
                letterSpacing = 2.sp
            )
            Spacer(modifier = Modifier.height(16.dp))
            Text(
                text = "━━━━━━━━━━━━━━━━",
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            
            Spacer(modifier = Modifier.height(48.dp))
            
            if (uiState.activeTimerInfo.state == TimerState.RUNNING) {
                Button(onClick = onPause) {
                    Text("Pause")
                }
            } else {
                Button(onClick = onResume) {
                    Text("Resume")
                }
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            Button(onClick = { showNeutronPanel = true }) {
                Text("Neutron")
            }
            
            Spacer(modifier = Modifier.height(16.dp))
            
            Button(onClick = onExitZenMode) {
                Text("Exit Zen Mode")
            }
        }
        
        if (showNeutronPanel) {
            NeutronPanel(
                appContainer = appContainer,
                subjectContext = uiState.selectedSubject?.name,
                onClose = { showNeutronPanel = false },
                modifier = Modifier.align(Alignment.BottomCenter)
            )
        }
    }
}"""

zen_mode_new = """@Composable
fun ZenModeScreen(
    appContainer: AppContainer,
    uiState: TimerUiState,
    onPause: () -> Unit,
    onResume: () -> Unit,
    onExitZenMode: () -> Unit,
    onStop: () -> Unit
) {
    ZenModeLockTaskEffect()
    val view = LocalView.current
    DisposableEffect(Unit) {
        view.keepScreenOn = true
        onDispose {
            view.keepScreenOn = false
        }
    }
    var showNeutronPanel by remember { mutableStateOf(false) }

    // Pulse animation for the minimal ring
    val infiniteTransition = rememberInfiniteTransition(label = "pulse")
    val scale by infiniteTransition.animateFloat(
        initialValue = 0.95f,
        targetValue = 1.05f,
        animationSpec = infiniteRepeatable(
            animation = tween(2000, easing = EaseInOutSine),
            repeatMode = RepeatMode.Reverse
        ),
        label = "pulseScale"
    )

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background)
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(32.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            Text(
                text = uiState.selectedSubject?.name?.uppercase() ?: "PHYSICS",
                style = MaterialTheme.typography.titleMedium,
                letterSpacing = 4.sp,
                color = MaterialTheme.colorScheme.secondary
            )
            
            Spacer(modifier = Modifier.height(48.dp))
            
            AnimatedContent(
                targetState = uiState.formattedTime,
                transitionSpec = {
                    (slideInVertically { height -> height } + fadeIn()).togetherWith(slideOutVertically { height -> -height } + fadeOut())
                },
                label = "timeAnimation"
            ) { targetTime ->
                Text(
                    text = targetTime,
                    style = MaterialTheme.typography.displayLarge.copy(
                        fontSize = 72.sp,
                        fontWeight = FontWeight.Light,
                        letterSpacing = 2.sp
                    ),
                    color = MaterialTheme.colorScheme.primary
                )
            }
            
            Spacer(modifier = Modifier.height(24.dp))
            
            Text(
                text = "Focus Session",
                style = MaterialTheme.typography.bodyLarge,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
            
            Spacer(modifier = Modifier.height(48.dp))
            
            // Minimalist breathing circle indicator
            Box(
                modifier = Modifier
                    .size(12.dp)
                    .androidx.compose.ui.draw.scale(if (uiState.activeTimerInfo.state == TimerState.RUNNING) scale else 1f)
                    .background(
                        color = if (uiState.activeTimerInfo.state == TimerState.RUNNING) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.5f),
                        shape = CircleShape
                    )
            )
            
            Spacer(modifier = Modifier.height(64.dp))
            
            Row(
                horizontalArrangement = Arrangement.spacedBy(16.dp)
            ) {
                androidx.compose.material3.TextButton(onClick = { showNeutronPanel = true }) {
                    Text("Neutron", color = MaterialTheme.colorScheme.secondary)
                }
                
                androidx.compose.material3.TextButton(onClick = onExitZenMode) {
                    Text("Exit Zen Mode", color = MaterialTheme.colorScheme.secondary)
                }
            }
        }
        
        if (showNeutronPanel) {
            Box(modifier = Modifier.fillMaxSize().background(Color.Black.copy(alpha = 0.3f))) {
                com.example.feature.neutron.NeutronBottomSheet(
                    appContainer = appContainer,
                    subjectContext = uiState.selectedSubject?.name,
                    onDismiss = { showNeutronPanel = false }
                )
            }
        }
    }
}"""

content = content.replace(zen_mode_old, zen_mode_new)

with open('app/src/main/java/com/example/feature/timer/TimerScreen.kt', 'w') as f:
    f.write(content)

