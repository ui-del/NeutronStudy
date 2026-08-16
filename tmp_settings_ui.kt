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
