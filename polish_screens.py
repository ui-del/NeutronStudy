import re

# --- 1. AnalyticsScreen ---
with open('app/src/main/java/com/example/feature/analytics/AnalyticsScreen.kt', 'r') as f:
    analytics_code = f.read()

analytics_neutron = """        }

        if (showNeutronPanel) {
            com.example.feature.neutron.NeutronBottomSheet(
                appContainer = appContainer,
                subjectContext = "Analytics and Study Statistics",
                onDismiss = { showNeutronPanel = false }
            )
        }
    }
}"""
analytics_code = analytics_code.replace("        }\n    }\n}", analytics_neutron)

if "import com.example.feature.neutron.NeutronBottomSheet" not in analytics_code:
    analytics_code = analytics_code.replace("import com.example.core.di.AppContainer", "import com.example.core.di.AppContainer\nimport com.example.feature.neutron.NeutronBottomSheet")

with open('app/src/main/java/com/example/feature/analytics/AnalyticsScreen.kt', 'w') as f:
    f.write(analytics_code)


# --- 2. SubjectsScreen ---
with open('app/src/main/java/com/example/feature/subjects/SubjectsScreen.kt', 'r') as f:
    subjects_code = f.read()

empty_subject_state = """            if (subjects.isEmpty()) {
                item {
                    Column(
                        modifier = Modifier.fillMaxWidth().padding(vertical = 64.dp),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Icon(
                            Icons.Default.Book,
                            contentDescription = null,
                            modifier = Modifier.size(64.dp),
                            tint = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.5f)
                        )
                        Spacer(modifier = Modifier.height(16.dp))
                        Text(
                            text = "No subjects yet",
                            style = MaterialTheme.typography.titleMedium,
                            color = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                        Text(
                            text = "Tap + to start organizing your focus.",
                            style = MaterialTheme.typography.bodyMedium,
                            color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.8f)
                        )
                    }
                }
            }"""

# Using regex to replace the old empty state
subjects_code = re.sub(r'if \(subjects\.isEmpty\(\)\) \{.*?\n\s+\}\n\s+\}', empty_subject_state, subjects_code, flags=re.DOTALL)

# Add Keyboard Options
keyboard_opt = "import androidx.compose.foundation.text.KeyboardOptions\nimport androidx.compose.ui.text.input.KeyboardType\n"
if "KeyboardOptions" not in subjects_code:
    subjects_code = subjects_code.replace("import androidx.compose.ui.Alignment", keyboard_opt + "import androidx.compose.ui.Alignment")

subjects_code = subjects_code.replace('label = { Text("Target Hours") },\n                    singleLine = true', 'label = { Text("Target Hours") },\n                    singleLine = true,\n                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number)')

if "import androidx.compose.foundation.layout.size" not in subjects_code:
    subjects_code = subjects_code.replace("import androidx.compose.foundation.layout.padding", "import androidx.compose.foundation.layout.padding\nimport androidx.compose.foundation.layout.size\nimport androidx.compose.foundation.layout.height")

with open('app/src/main/java/com/example/feature/subjects/SubjectsScreen.kt', 'w') as f:
    f.write(subjects_code)


# --- 3. GoalsScreen ---
with open('app/src/main/java/com/example/feature/goals/GoalsScreen.kt', 'r') as f:
    goals_code = f.read()

empty_goals_state = """            if (goals.isEmpty()) {
                item {
                    Column(
                        modifier = Modifier.fillMaxWidth().padding(vertical = 64.dp),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Icon(
                            Icons.Default.Flag,
                            contentDescription = null,
                            modifier = Modifier.size(64.dp),
                            tint = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.5f)
                        )
                        Spacer(modifier = Modifier.height(16.dp))
                        Text(
                            text = "No goals set",
                            style = MaterialTheme.typography.titleMedium,
                            color = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                        Text(
                            text = "Tap + to define your milestones.",
                            style = MaterialTheme.typography.bodyMedium,
                            color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.8f)
                        )
                    }
                }
            }"""

goals_code = re.sub(r'if \(goals\.isEmpty\(\)\) \{.*?\n\s+\}\n\s+\}', empty_goals_state, goals_code, flags=re.DOTALL)

if "KeyboardOptions" not in goals_code:
    goals_code = goals_code.replace("import androidx.compose.ui.Alignment", "import androidx.compose.foundation.text.KeyboardOptions\nimport androidx.compose.ui.text.input.KeyboardType\nimport androidx.compose.ui.Alignment")

goals_code = goals_code.replace('label = { Text("Target Hours") },\n                    singleLine = true', 'label = { Text("Target Hours") },\n                    singleLine = true,\n                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number)')

if "import androidx.compose.foundation.layout.size" not in goals_code:
    goals_code = goals_code.replace("import androidx.compose.foundation.layout.padding", "import androidx.compose.foundation.layout.padding\nimport androidx.compose.foundation.layout.size")

with open('app/src/main/java/com/example/feature/goals/GoalsScreen.kt', 'w') as f:
    f.write(goals_code)

print("Polish script applied.")
