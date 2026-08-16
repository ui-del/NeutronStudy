import re

# Fix SubjectsScreen missing Book Icon
with open('app/src/main/java/com/example/feature/subjects/SubjectsScreen.kt', 'r') as f:
    subjects = f.read()
if 'import androidx.compose.material.icons.filled.Book' not in subjects:
    subjects = subjects.replace('import androidx.compose.material.icons.filled.Add', 'import androidx.compose.material.icons.filled.Add\nimport androidx.compose.material.icons.filled.Book')
with open('app/src/main/java/com/example/feature/subjects/SubjectsScreen.kt', 'w') as f:
    f.write(subjects)

# Fix AnalyticsScreen extra NeutronPanel in StatCard
with open('app/src/main/java/com/example/feature/analytics/AnalyticsScreen.kt', 'r') as f:
    analytics = f.read()

# I will cleanly rewrite StatCard to remove the bug
good_stat_card = """@Composable
fun StatCard(title: String, value: String, modifier: Modifier = Modifier) {
    Card(modifier = modifier) {
        Column(
            modifier = Modifier.padding(16.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(title, style = MaterialTheme.typography.labelMedium)
            Spacer(modifier = Modifier.height(8.dp))
            Text(value, style = MaterialTheme.typography.titleMedium, fontWeight = androidx.compose.ui.text.font.FontWeight.Bold)
        }
    }
}"""
# Using regex to replace the messed up StatCard
analytics = re.sub(r'@Composable\nfun StatCard.*?\}\n\}', good_stat_card, analytics, flags=re.DOTALL)

with open('app/src/main/java/com/example/feature/analytics/AnalyticsScreen.kt', 'w') as f:
    f.write(analytics)

print("Errors fixed.")
