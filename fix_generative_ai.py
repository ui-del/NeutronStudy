import re

with open('app/build.gradle.kts', 'r') as f:
    content = f.read()

# Make sure we use Firebase GenAI since it handles dependencies much better and doesn't conflict.
content = content.replace("implementation(libs.generativeai)", "// implementation(libs.generativeai)")

with open('app/build.gradle.kts', 'w') as f:
    f.write(content)
