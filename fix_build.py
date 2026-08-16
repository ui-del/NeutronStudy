import re
with open('app/build.gradle.kts', 'r') as f:
    content = f.read()

content = re.sub(r'buildConfigField\("String", "GOOGLE_WEB_CLIENT_ID", ""\$webClientId""\)', 'buildConfigField("String", "GOOGLE_WEB_CLIENT_ID", "\\\"$webClientId\\\"")', content)

with open('app/build.gradle.kts', 'w') as f:
    f.write(content)
