import re

file_path = 'app/src/main/java/com/example/feature/timer/TimerScreen.kt'
with open(file_path, 'r') as f:
    content = f.read()

replacement = """                StopwatchControls(
                    state = uiState.activeTimerInfo.state,
                    onStart = { viewModel.startTimer(mode = selectedMode, subjectId = selectedSubjectId) },
                    onPause = { viewModel.pauseTimer() },
                    onResume = { viewModel.resumeTimer() },
                    onReset = { viewModel.discardTimer() },
                    onStopAndSave = { viewModel.stopAndSaveTimer() }
                )"""

# The chunk we are replacing
target_chunk = """                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.SpaceEvenly
                ) {
                    if (uiState.activeTimerInfo.state == TimerState.IDLE) {
                        Button(onClick = { viewModel.startTimer(mode = selectedMode, subjectId = selectedSubjectId) }) {
                            Text("Start")
                        }
                    } else {
                        if (uiState.activeTimerInfo.state == TimerState.RUNNING) {
                            Button(onClick = { viewModel.pauseTimer() }) {
                                Text("Pause")
                            }
                        } else {
                            Button(onClick = { viewModel.resumeTimer() }) {
                                Text("Resume")
                            }
                        }
                        
                        Button(onClick = { viewModel.stopAndSaveTimer() }) {
                            Text("Stop & Save")
                        }
                        
                        Button(onClick = { viewModel.discardTimer() }) {
                            Text("Discard")
                        }
                    }
                }"""

content = content.replace(target_chunk, replacement)

# Add the Composable to the end of the file
composable_code = """

@Composable
fun StopwatchControls(
    state: TimerState,
    onStart: () -> Unit,
    onPause: () -> Unit,
    onResume: () -> Unit,
    onReset: () -> Unit,
    onStopAndSave: () -> Unit
) {
    Row(
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.Center,
        verticalAlignment = Alignment.CenterVertically
    ) {
        if (state == TimerState.IDLE) {
            Button(
                onClick = onStart,
                modifier = Modifier.height(56.dp).width(160.dp),
                shape = androidx.compose.foundation.shape.RoundedCornerShape(16.dp)
            ) {
                Icon(androidx.compose.material.icons.Icons.Filled.PlayArrow, contentDescription = "Start")
                Spacer(modifier = Modifier.width(8.dp))
                Text("Start", style = MaterialTheme.typography.titleMedium)
            }
        } else {
            androidx.compose.material3.OutlinedButton(
                onClick = onReset,
                modifier = Modifier.height(56.dp).padding(end = 8.dp),
                shape = androidx.compose.foundation.shape.RoundedCornerShape(16.dp)
            ) {
                Icon(androidx.compose.material.icons.Icons.Filled.Refresh, contentDescription = "Reset")
                Spacer(modifier = Modifier.width(4.dp))
                Text("Reset")
            }
            
            if (state == TimerState.RUNNING) {
                Button(
                    onClick = onPause,
                    modifier = Modifier.height(56.dp).padding(end = 8.dp),
                    shape = androidx.compose.foundation.shape.RoundedCornerShape(16.dp)
                ) {
                    Icon(androidx.compose.material.icons.Icons.Filled.Pause, contentDescription = "Pause")
                    Spacer(modifier = Modifier.width(4.dp))
                    Text("Pause")
                }
            } else {
                Button(
                    onClick = onResume,
                    modifier = Modifier.height(56.dp).padding(end = 8.dp),
                    shape = androidx.compose.foundation.shape.RoundedCornerShape(16.dp)
                ) {
                    Icon(androidx.compose.material.icons.Icons.Filled.PlayArrow, contentDescription = "Resume")
                    Spacer(modifier = Modifier.width(4.dp))
                    Text("Resume")
                }
            }

            androidx.compose.material3.FilledTonalButton(
                onClick = onStopAndSave,
                modifier = Modifier.height(56.dp),
                shape = androidx.compose.foundation.shape.RoundedCornerShape(16.dp)
            ) {
                Icon(androidx.compose.material.icons.Icons.Filled.Stop, contentDescription = "Save")
                Spacer(modifier = Modifier.width(4.dp))
                Text("Save")
            }
        }
    }
}
"""

if "fun StopwatchControls" not in content:
    content += composable_code

with open(file_path, 'w') as f:
    f.write(content)
