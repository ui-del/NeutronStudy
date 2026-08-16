import re

with open('app/build.gradle.kts', 'r') as f:
    content = f.read()

# Make sure we re-enable generativeai since we just disabled it in the previous script.
content = content.replace("// implementation(libs.generativeai)", "implementation(libs.generativeai)")

# Add resolution strategy
resolution_strategy = """
configurations.all {
    resolutionStrategy {
        eachDependency {
            if (requested.group == "io.ktor") {
                useVersion("2.3.11")
            }
        }
    }
}
"""

if "resolutionStrategy" not in content:
    content += resolution_strategy

with open('app/build.gradle.kts', 'w') as f:
    f.write(content)
