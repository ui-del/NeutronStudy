#!/bin/bash
sed -i '/fun getAllSessions(): Flow/a \    @Query("SELECT * FROM sessions ORDER BY startTime DESC")\n    suspend fun getAllSessionsStatic(): List<SessionEntity>' app/src/main/java/com/example/data/local/dao/SessionDao.kt

sed -i '/fun getActiveSubjects(): Flow/a \    @Query("SELECT * FROM subjects")\n    suspend fun getAllSubjectsStatic(): List<SubjectEntity>' app/src/main/java/com/example/data/local/dao/SubjectDao.kt

sed -i '/fun getActiveSubjects(): Flow/a \    suspend fun getAllSubjectsStatic(): List<SubjectEntity> = subjectDao.getAllSubjectsStatic()' app/src/main/java/com/example/data/repository/StudyRepository.kt

sed -i '/fun getAllSessions(): Flow/a \    suspend fun getAllSessionsStatic(): List<SessionEntity> = sessionDao.getAllSessionsStatic()' app/src/main/java/com/example/data/repository/StudyRepository.kt
