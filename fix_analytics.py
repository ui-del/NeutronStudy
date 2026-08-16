import re

with open('app/src/main/java/com/example/feature/analytics/AnalyticsScreen.kt', 'r') as f:
    content = f.read()

new_ui = """                // Hero Metric
                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(bottom = 24.dp),
                    shape = MaterialTheme.shapes.large,
                    colors = androidx.compose.material3.CardDefaults.cardColors(
                        containerColor = MaterialTheme.colorScheme.primary
                    )
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(32.dp),
                        horizontalAlignment = Alignment.CenterHorizontally
                    ) {
                        Text(
                            text = "TOTAL FOCUS TIME",
                            style = MaterialTheme.typography.labelMedium,
                            color = MaterialTheme.colorScheme.onPrimary.copy(alpha = 0.8f),
                            letterSpacing = 2.sp
                        )
                        Spacer(modifier = Modifier.height(16.dp))
                        Text(
                            text = formatMs(uiState.totalStudyTimeMs),
                            style = MaterialTheme.typography.displayMedium,
                            color = MaterialTheme.colorScheme.onPrimary,
                            fontWeight = FontWeight.Light
                        )
                        Spacer(modifier = Modifier.height(24.dp))
                        Row(
                            modifier = Modifier.fillMaxWidth(),
                            horizontalArrangement = Arrangement.SpaceEvenly
                        ) {
                            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                                Text("Longest", style = MaterialTheme.typography.labelSmall, color = MaterialTheme.colorScheme.onPrimary.copy(alpha = 0.7f))
                                Text(formatMs(uiState.longestSessionMs), style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.onPrimary)
                            }
                            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                                Text("Avg/Session", style = MaterialTheme.typography.labelSmall, color = MaterialTheme.colorScheme.onPrimary.copy(alpha = 0.7f))
                                Text(formatMs(uiState.averageSessionTimeMs), style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.onPrimary)
                            }
                            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                                Text("Streak", style = MaterialTheme.typography.labelSmall, color = MaterialTheme.colorScheme.onPrimary.copy(alpha = 0.7f))
                                Text("${uiState.userProfile.currentStreak} Days", style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.onPrimary)
                            }
                        }
                    }
                }
                
                Text("Subjects", style = MaterialTheme.typography.titleLarge)
                Spacer(modifier = Modifier.height(16.dp))"""

# Replace the messy cards with the new hero card.
# We will use regex to find the bounds from `item {` up to the `items` block for distribution.
pattern = r"item\s*\{\s*Card\(\s*modifier = Modifier.*?(?=items\(uiState.subjectDistribution)"
content = re.sub(pattern, f"item {{\n{new_ui}\n            }}\n            \n            ", content, flags=re.DOTALL)

with open('app/src/main/java/com/example/feature/analytics/AnalyticsScreen.kt', 'w') as f:
    f.write(content)
