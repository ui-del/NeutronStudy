#!/bin/bash
sed -i '/import com.example.data.repository.NeutronAiService/a \
import com.example.data.auth.AuthManager\nimport com.example.data.sync.FirestoreSyncManager\n' app/src/main/java/com/example/core/di/AppContainer.kt

sed -i '/val neutronAiService: NeutronAiService/a \
    val authManager: AuthManager\n    val firestoreSyncManager: FirestoreSyncManager' app/src/main/java/com/example/core/di/AppContainer.kt

sed -i '/override val neutronAiService: NeutronAiService by lazy {/i \
    override val authManager: AuthManager by lazy {\n        AuthManager(context)\n    }\n\n    override val firestoreSyncManager: FirestoreSyncManager by lazy {\n        FirestoreSyncManager(studyRepository)\n    }\n' app/src/main/java/com/example/core/di/AppContainer.kt
