#!/bin/bash
cat app/src/main/java/com/example/feature/subjects/SubjectsViewModel.kt | sed '/fun deleteSubject/i \
    fun updateSubject(subject: SubjectEntity) {\
        viewModelScope.launch {\
            studyRepository.updateSubject(subject)\
        }\
    }\
' > tmp_vm.kt
mv tmp_vm.kt app/src/main/java/com/example/feature/subjects/SubjectsViewModel.kt
