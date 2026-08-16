#!/bin/bash
cat << 'INNER_EOF' > app/src/main/java/com/example/feature/settings/SettingsViewModel.kt
package com.example.feature.settings

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.viewModelScope
import com.example.data.local.entities.AppSettingsEntity
import com.example.data.repository.StudyRepository
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch
import android.content.Context
import android.content.Intent
import androidx.core.content.FileProvider
import java.io.File
import java.io.FileWriter
import kotlinx.coroutines.flow.firstOrNull
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import com.example.data.auth.AuthManager
import com.example.data.sync.FirestoreSyncManager
import com.google.firebase.auth.FirebaseUser
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.combine

data class SettingsUiState(
    val settings: AppSettingsEntity = AppSettingsEntity(),
    val currentUser: FirebaseUser? = null,
    val isSyncing: Boolean = false
)

class SettingsViewModel(
    private val studyRepository: StudyRepository,
    private val authManager: AuthManager,
    private val firestoreSyncManager: FirestoreSyncManager
) : ViewModel() {

    private val _isSyncing = MutableStateFlow(false)

    val uiState: StateFlow<SettingsUiState> = combine(
        studyRepository.getSettings(),
        authManager.currentUser,
        _isSyncing
    ) { settings, user, isSyncing ->
        SettingsUiState(
            settings = settings ?: AppSettingsEntity(),
            currentUser = user,
            isSyncing = isSyncing
        )
    }.stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5000),
        initialValue = SettingsUiState()
    )

    fun signInWithGoogle() {
        viewModelScope.launch {
            authManager.signInWithGoogle()
        }
    }

    fun signOut() {
        authManager.signOut()
    }

    fun syncToCloud() {
        viewModelScope.launch {
            _isSyncing.value = true
            firestoreSyncManager.syncToCloud()
            _isSyncing.value = false
        }
    }

    fun syncFromCloud() {
        viewModelScope.launch {
            _isSyncing.value = true
            firestoreSyncManager.syncFromCloud()
            _isSyncing.value = false
        }
    }

    fun exportData(context: Context) {
        viewModelScope.launch {
            try {
                val sessions = studyRepository.getAllSessions().firstOrNull() ?: emptyList()
                val file = File(context.cacheDir, "study_sessions_export.csv")
                
                withContext(Dispatchers.IO) {
                    FileWriter(file).use { writer ->
                        writer.append("Session ID,Subject ID,Start Time,End Time,Duration Ms,Mode\n")
                        for (session in sessions) {
                            writer.append("${session.id},${session.subjectId},${session.startTime},${session.endTime},${session.duration},${session.mode}\n")
                        }
                    }
                }
                
                val uri = FileProvider.getUriForFile(context, "${context.packageName}.provider", file)
                val intent = Intent(Intent.ACTION_SEND).apply {
                    type = "text/csv"
                    putExtra(Intent.EXTRA_SUBJECT, "Study Sessions Export")
                    putExtra(Intent.EXTRA_STREAM, uri)
                    addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
                }
                
                val chooser = Intent.createChooser(intent, "Share Export")
                chooser.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                context.startActivity(chooser)
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    fun updatePomodoroFocus(minutes: Int) {
        viewModelScope.launch {
            val current = uiState.value.settings
            studyRepository.updateSettings(current.copy(pomodoroFocusDuration = minutes * 60 * 1000L))
        }
    }

    fun updatePomodoroShortBreak(minutes: Int) {
        viewModelScope.launch {
            val current = uiState.value.settings
            studyRepository.updateSettings(current.copy(pomodoroShortBreak = minutes * 60 * 1000L))
        }
    }

    fun updatePomodoroLongBreak(minutes: Int) {
        viewModelScope.launch {
            val current = uiState.value.settings
            studyRepository.updateSettings(current.copy(pomodoroLongBreak = minutes * 60 * 1000L))
        }
    }

    fun updatePomodoroCycles(cycles: Int) {
        viewModelScope.launch {
            val current = uiState.value.settings
            studyRepository.updateSettings(current.copy(pomodoroCycles = cycles))
        }
    }

    fun toggleAmoledDarkTheme(enabled: Boolean) {
        viewModelScope.launch {
            val current = uiState.value.settings
            studyRepository.updateSettings(current.copy(useAmoledDarkTheme = enabled))
        }
    }
    
    fun toggleBiometric(enabled: Boolean) {
        viewModelScope.launch {
            val current = uiState.value.settings
            studyRepository.updateSettings(current.copy(isBiometricEnabled = enabled))
        }
    }
}

class SettingsViewModelFactory(
    private val repository: StudyRepository,
    private val authManager: AuthManager,
    private val firestoreSyncManager: FirestoreSyncManager
) : ViewModelProvider.Factory {
    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        if (modelClass.isAssignableFrom(SettingsViewModel::class.java)) {
            @Suppress("UNCHECKED_CAST")
            return SettingsViewModel(repository, authManager, firestoreSyncManager) as T
        }
        throw IllegalArgumentException("Unknown ViewModel class")
    }
}
INNER_EOF

# Now update SettingsScreen.kt factory and UI
sed -i 's/factory = SettingsViewModelFactory(appContainer.studyRepository)/factory = SettingsViewModelFactory(appContainer.studyRepository, appContainer.authManager, appContainer.firestoreSyncManager)/g' app/src/main/java/com/example/feature/settings/SettingsScreen.kt

cat << 'INNER_EOF' > tmp_settings_ui.kt
            Divider(modifier = Modifier.padding(vertical = 16.dp))
            SettingSectionHeader("Cloud Sync & Account")
            
            if (uiState.currentUser == null) {
                Button(
                    onClick = { viewModel.signInWithGoogle() },
                    modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 8.dp)
                ) {
                    Text("Sign in with Google")
                }
            } else {
                Text(
                    text = "Signed in as: ${uiState.currentUser?.email}",
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp)
                )
                
                Row(modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp), horizontalArrangement = androidx.compose.foundation.layout.Arrangement.SpaceEvenly) {
                    Button(onClick = { viewModel.syncToCloud() }, enabled = !uiState.isSyncing) {
                        Text("Sync To Cloud")
                    }
                    Button(onClick = { viewModel.syncFromCloud() }, enabled = !uiState.isSyncing) {
                        Text("Sync From Cloud")
                    }
                }
                
                Button(
                    onClick = { viewModel.signOut() },
                    colors = androidx.compose.material3.ButtonDefaults.buttonColors(containerColor = MaterialTheme.colorScheme.error),
                    modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 8.dp)
                ) {
                    Text("Sign Out")
                }
            }
INNER_EOF

sed -i '/SettingSectionHeader("Data Management")/r tmp_settings_ui.kt' app/src/main/java/com/example/feature/settings/SettingsScreen.kt

