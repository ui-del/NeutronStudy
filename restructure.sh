#!/bin/bash
cd app/src/main/java/com/example

# Create directories
mkdir -p feature
mkdir -p core

# Move directories
mv ui/timer feature/
mv ui/subjects feature/
mv ui/analytics feature/
mv ui/settings feature/
mv ui/ai feature/neutron

mv di core/

# Replace packages in files
find . -type f -name "*.kt" -exec sed -i 's/package com\.example\.ui\.timer/package com.example.feature.timer/g' {} +
find . -type f -name "*.kt" -exec sed -i 's/package com\.example\.ui\.subjects/package com.example.feature.subjects/g' {} +
find . -type f -name "*.kt" -exec sed -i 's/package com\.example\.ui\.analytics/package com.example.feature.analytics/g' {} +
find . -type f -name "*.kt" -exec sed -i 's/package com\.example\.ui\.settings/package com.example.feature.settings/g' {} +
find . -type f -name "*.kt" -exec sed -i 's/package com\.example\.ui\.ai/package com.example.feature.neutron/g' {} +

find . -type f -name "*.kt" -exec sed -i 's/package com\.example\.di/package com.example.core.di/g' {} +

# Replace imports in all files
find . -type f -name "*.kt" -exec sed -i 's/import com\.example\.ui\.timer/import com.example.feature.timer/g' {} +
find . -type f -name "*.kt" -exec sed -i 's/import com\.example\.ui\.subjects/import com.example.feature.subjects/g' {} +
find . -type f -name "*.kt" -exec sed -i 's/import com\.example\.ui\.analytics/import com.example.feature.analytics/g' {} +
find . -type f -name "*.kt" -exec sed -i 's/import com\.example\.ui\.settings/import com.example.feature.settings/g' {} +
find . -type f -name "*.kt" -exec sed -i 's/import com\.example\.ui\.ai/import com.example.feature.neutron/g' {} +

find . -type f -name "*.kt" -exec sed -i 's/import com\.example\.di/import com.example.core.di/g' {} +

