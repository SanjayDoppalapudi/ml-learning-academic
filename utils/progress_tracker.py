"""
Progress Tracking System for ML Learning Platform
Tracks study sessions, exercise completion, and skill development.
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any
import time


class ProgressTracker:
    """
    Academic progress tracking system for machine learning curriculum.
    
    Tracks:
    - Study time and session logs
    - Exercise and project completion
    - Concept mastery ratings
    - Learning velocity and consistency
    """
    
    def __init__(self, base_path: str = "."):
        """
        Initialize progress tracker.
        
        Args:
            base_path: Base directory path for the learning platform
        """
        self.base_path = Path(base_path)
        self.progress_dir = self.base_path / "logs"
        self.progress_dir.mkdir(exist_ok=True)
        
        self.progress_file = self.progress_dir / "learning_progress.json"
        self.session_log_file = self.progress_dir / "session_logs.json"
        self.achievements_file = self.progress_dir / "achievements.json"
        
        self.progress = self._load_progress()
        self.session_log = self._load_session_log()
        self.achievements = self._load_achievements()
        
        self.current_session = None
        self.session_start_time = None
        
    def _load_progress(self) -> Dict[str, Any]:
        """Load progress from JSON file or create new."""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        
        return {
            "user_info": {
                "start_date": datetime.now().isoformat(),
                "current_level": 1,
                "total_xp": 0,
                "total_study_time_minutes": 0,
                "current_streak_days": 0,
                "longest_streak_days": 0,
                "last_study_date": None
            },
            "modules": {
                "module_0": {"completed": False, "progress_pct": 0.0, "lessons_completed": [], "exercises_completed": [], "time_spent_minutes": 0},
                "module_1": {"completed": False, "progress_pct": 0.0, "lessons_completed": [], "exercises_completed": [], "time_spent_minutes": 0},
                "module_2": {"completed": False, "progress_pct": 0.0, "lessons_completed": [], "exercises_completed": [], "time_spent_minutes": 0},
                "module_3": {"completed": False, "progress_pct": 0.0, "lessons_completed": [], "exercises_completed": [], "time_spent_minutes": 0},
                "module_4": {"completed": False, "progress_pct": 0.0, "lessons_completed": [], "exercises_completed": [], "time_spent_minutes": 0},
            },
            "capstones": {
                "project_1_regression": {"completed": False, "grade": None, "time_spent_minutes": 0},
                "project_2_classification": {"completed": False, "grade": None, "time_spent_minutes": 0},
                "project_3_neural_network": {"completed": False, "grade": None, "time_spent_minutes": 0},
            },
            "skills": {
                "python": {"level": 0, "confidence": 0, "exercises_completed": 0},
                "mathematics": {"level": 0, "confidence": 0, "exercises_completed": 0},
                "statistics": {"level": 0, "confidence": 0, "exercises_completed": 0},
                "machine_learning": {"level": 0, "confidence": 0, "exercises_completed": 0},
                "deep_learning": {"level": 0, "confidence": 0, "exercises_completed": 0},
            },
            "daily_activity": {}
        }
    
    def _load_session_log(self) -> List[Dict]:
        """Load session logs from JSON file or create new."""
        if self.session_log_file.exists():
            with open(self.session_log_file, 'r') as f:
                return json.load(f)
        return []
    
    def _load_achievements(self) -> Dict[str, Any]:
        """Load achievements from JSON file or create new."""
        if self.achievements_file.exists():
            with open(self.achievements_file, 'r') as f:
                return json.load(f)
        
        return {
            "scholar": {"unlocked": False, "date": None, "description": "Complete your first module"},
            "mathematician": {"unlocked": False, "date": None, "description": "Complete Module 1 with all exercises correct"},
            "statistician": {"unlocked": False, "date": None, "description": "Complete Module 2 with all exercises correct"},
            "ml_engineer": {"unlocked": False, "date": None, "description": "Build 5 algorithms from scratch"},
            "deep_learning_expert": {"unlocked": False, "date": None, "description": "Achieve 95%+ accuracy on capstone project"},
            "consistent_learner": {"unlocked": False, "date": None, "description": "Maintain a 30-day study streak"},
            "master": {"unlocked": False, "date": None, "description": "Complete the entire curriculum"},
            "speed_demon": {"unlocked": False, "date": None, "description": "Complete a module in under 3 days"},
            "perfectionist": {"unlocked": False, "date": None, "description": "Score 100% on all exercises in a module"},
        }
    
    def _save_progress(self):
        """Save current progress to JSON file."""
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def _save_session_log(self):
        """Save session logs to JSON file."""
        with open(self.session_log_file, 'w') as f:
            json.dump(self.session_log, f, indent=2)
    
    def _save_achievements(self):
        """Save achievements to JSON file."""
        with open(self.achievements_file, 'w') as f:
            json.dump(self.achievements, f, indent=2)
    
    def start_session(self, module: str, lesson: str, notes: str = "") -> Dict:
        """
        Start a new study session.
        
        Args:
            module: Module identifier (e.g., 'module_1')
            lesson: Lesson/project identifier
            notes: Optional notes about the session
            
        Returns:
            Session information dictionary
        """
        self.session_start_time = datetime.now()
        self.current_session = {
            "id": f"session_{len(self.session_log) + 1:04d}",
            "start_time": self.session_start_time.isoformat(),
            "module": module,
            "lesson": lesson,
            "notes": notes,
            "end_time": None,
            "duration_minutes": 0
        }
        
        return self.current_session
    
    def end_session(self, completed: bool = False) -> Dict:
        """
        End the current study session.
        
        Args:
            completed: Whether the lesson was completed in this session
            
        Returns:
            Updated session information
        """
        if not self.current_session or not self.session_start_time:
            raise ValueError("No active session to end")
        
        end_time = datetime.now()
        duration = (end_time - self.session_start_time).total_seconds() / 60
        
        self.current_session["end_time"] = end_time.isoformat()
        self.current_session["duration_minutes"] = round(duration, 2)
        self.current_session["completed"] = completed
        
        # Add to session log
        self.session_log.append(self.current_session)
        self._save_session_log()
        
        # Update user stats
        self.progress["user_info"]["total_study_time_minutes"] += duration
        self.progress["user_info"]["last_study_date"] = end_time.date().isoformat()
        
        # Update streak
        self._update_streak(end_time.date())
        
        # Update daily activity
        date_str = end_time.date().isoformat()
        if date_str not in self.progress["daily_activity"]:
            self.progress["daily_activity"][date_str] = {
                "total_time_minutes": 0,
                "sessions": 0,
                "modules_visited": []
            }
        
        self.progress["daily_activity"][date_str]["total_time_minutes"] += duration
        self.progress["daily_activity"][date_str]["sessions"] += 1
        
        if self.current_session["module"] not in self.progress["daily_activity"][date_str]["modules_visited"]:
            self.progress["daily_activity"][date_str]["modules_visited"].append(self.current_session["module"])
        
        # Update module time
        module = self.current_session["module"]
        if module in self.progress["modules"]:
            self.progress["modules"][module]["time_spent_minutes"] += duration
        
        self._save_progress()
        
        session_info = self.current_session.copy()
        self.current_session = None
        self.session_start_time = None
        
        return session_info
    
    def _update_streak(self, study_date):
        """Update study streak based on last study date."""
        last_date_str = self.progress["user_info"]["last_study_date"]
        
        if last_date_str:
            last_date = datetime.fromisoformat(last_date_str).date()
            
            if study_date == last_date:
                # Same day, no change to streak
                pass
            elif study_date == last_date + timedelta(days=1):
                # Consecutive day, increase streak
                self.progress["user_info"]["current_streak_days"] += 1
            else:
                # Streak broken, reset
                self.progress["user_info"]["current_streak_days"] = 1
        else:
            # First study session
            self.progress["user_info"]["current_streak_days"] = 1
        
        # Update longest streak
        current_streak = self.progress["user_info"]["current_streak_days"]
        longest_streak = self.progress["user_info"]["longest_streak_days"]
        
        if current_streak > longest_streak:
            self.progress["user_info"]["longest_streak_days"] = current_streak
        
        # Check for consistent learner achievement
        if current_streak >= 30 and not self.achievements["consistent_learner"]["unlocked"]:
            self.unlock_achievement("consistent_learner")
    
    def mark_lesson_complete(self, module: str, lesson: str, xp_earned: int = 0):
        """
        Mark a lesson or project as completed.
        
        Args:
            module: Module identifier
            lesson: Lesson/project identifier
            xp_earned: Experience points earned
        """
        if module not in self.progress["modules"]:
            raise ValueError(f"Unknown module: {module}")
        
        module_data = self.progress["modules"][module]
        
        if lesson not in module_data["lessons_completed"]:
            module_data["lessons_completed"].append(lesson)
            
            # Calculate progress percentage
            # This would need module-specific total lesson counts
            total_lessons = self._get_module_lesson_count(module)
            if total_lessons > 0:
                module_data["progress_pct"] = (len(module_data["lessons_completed"]) / total_lessons) * 100
            
            # Check if module is complete
            if module_data["progress_pct"] >= 100:
                module_data["completed"] = True
                self.unlock_achievement("scholar")
        
        # Add XP
        self.progress["user_info"]["total_xp"] += xp_earned
        self._update_level()
        
        self._save_progress()
    
    def _get_module_lesson_count(self, module: str) -> int:
        """Get total number of lessons in a module."""
        lesson_counts = {
            "module_0": 3,
            "module_1": 4,
            "module_2": 4,
            "module_3": 5,
            "module_4": 4,
        }
        return lesson_counts.get(module, 0)
    
    def _update_level(self):
        """Update user level based on XP."""
        xp = self.progress["user_info"]["total_xp"]
        # Simple leveling: level = 1 + floor(xp / 1000)
        new_level = 1 + xp // 1000
        self.progress["user_info"]["current_level"] = new_level
    
    def mark_exercise_complete(self, module: str, exercise_id: str, score: float = 1.0, skill: Optional[str] = None):
        """
        Mark an exercise as completed.
        
        Args:
            module: Module identifier
            exercise_id: Unique exercise identifier
            score: Score achieved (0.0 to 1.0)
            skill: Skill category (python, mathematics, statistics, etc.)
        """
        if module not in self.progress["modules"]:
            raise ValueError(f"Unknown module: {module}")
        
        exercise_data = {
            "id": exercise_id,
            "completed_at": datetime.now().isoformat(),
            "score": score,
            "module": module
        }
        
        module_data = self.progress["modules"][module]
        
        # Check if already completed
        existing = [e for e in module_data["exercises_completed"] if e["id"] == exercise_id]
        if not existing:
            module_data["exercises_completed"].append(exercise_data)
            
            # Update skill
            if skill and skill in self.progress["skills"]:
                self.progress["skills"][skill]["exercises_completed"] += 1
                
                # Update skill level based on exercises
                exercise_count = self.progress["skills"][skill]["exercises_completed"]
                self.progress["skills"][skill]["level"] = min(exercise_count // 10, 10)
        
        self._save_progress()
    
    def update_skill_confidence(self, skill: str, confidence: int):
        """
        Update confidence rating for a skill (1-5 scale).
        
        Args:
            skill: Skill category
            confidence: Confidence level (1-5)
        """
        if skill in self.progress["skills"]:
            self.progress["skills"][skill]["confidence"] = max(1, min(5, confidence))
            self._save_progress()
    
    def mark_capstone_complete(self, project: str, grade: float, time_spent_minutes: int = 0):
        """
        Mark a capstone project as complete.
        
        Args:
            project: Project identifier
            grade: Final grade/accuracy percentage
            time_spent_minutes: Time spent on project
        """
        if project in self.progress["capstones"]:
            self.progress["capstones"][project]["completed"] = True
            self.progress["capstones"][project]["grade"] = grade
            self.progress["capstones"][project]["time_spent_minutes"] = time_spent_minutes
            
            # Check for deep learning expert achievement
            if grade >= 95 and not self.achievements["deep_learning_expert"]["unlocked"]:
                self.unlock_achievement("deep_learning_expert")
            
            # Check for master achievement
            all_capstones_complete = all(
                c["completed"] for c in self.progress["capstones"].values()
            )
            all_modules_complete = all(
                m["completed"] for m in self.progress["modules"].values()
            )
            
            if all_capstones_complete and all_modules_complete:
                self.unlock_achievement("master")
            
            self._save_progress()
    
    def unlock_achievement(self, achievement: str):
        """
        Unlock an achievement.
        
        Args:
            achievement: Achievement identifier
        """
        if achievement in self.achievements and not self.achievements[achievement]["unlocked"]:
            self.achievements[achievement]["unlocked"] = True
            self.achievements[achievement]["date"] = datetime.now().isoformat()
            self._save_achievements()
            print(f"🏆 Achievement Unlocked: {achievement.replace('_', ' ').title()}")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get comprehensive learning statistics."""
        total_lessons = sum(len(m["lessons_completed"]) for m in self.progress["modules"].values())
        total_exercises = sum(len(m["exercises_completed"]) for m in self.progress["modules"].values())
        
        return {
            "user": self.progress["user_info"],
            "summary": {
                "modules_completed": sum(1 for m in self.progress["modules"].values() if m["completed"]),
                "total_modules": len(self.progress["modules"]),
                "lessons_completed": total_lessons,
                "exercises_completed": total_exercises,
                "capstones_completed": sum(1 for c in self.progress["capstones"].values() if c["completed"]),
            },
            "skills": self.progress["skills"],
            "achievements": self.achievements,
            "recent_sessions": self.session_log[-5:] if self.session_log else []
        }
    
    def generate_report(self, period: str = "weekly") -> str:
        """
        Generate a learning report.
        
        Args:
            period: 'daily', 'weekly', or 'monthly'
            
        Returns:
            Formatted report string
        """
        if period == "daily":
            days = 1
            title = "Daily Learning Report"
        elif period == "weekly":
            days = 7
            title = "Weekly Learning Report"
        else:
            days = 30
            title = "Monthly Learning Report"
        
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)
        
        # Filter sessions
        period_sessions = [
            s for s in self.session_log
            if datetime.fromisoformat(s["start_time"]).date() >= start_date
        ]
        
        total_time = sum(s["duration_minutes"] for s in period_sessions)
        lessons_completed = len(set(
            (s["module"], s["lesson"]) for s in period_sessions if s.get("completed")
        ))
        
        report = f"""
{'='*60}
{title}
Period: {start_date} to {end_date}
{'='*60}

Study Statistics:
  - Total Sessions: {len(period_sessions)}
  - Total Study Time: {total_time:.1f} minutes ({total_time/60:.1f} hours)
  - Average Session: {total_time/len(period_sessions) if period_sessions else 0:.1f} minutes
  - Lessons Completed: {lessons_completed}

Current Streak: {self.progress['user_info']['current_streak_days']} days
Longest Streak: {self.progress['user_info']['longest_streak_days']} days

Overall Progress:
  - Level: {self.progress['user_info']['current_level']}
  - Total XP: {self.progress['user_info']['total_xp']}
  - Total Study Time: {self.progress['user_info']['total_study_time_minutes']/60:.1f} hours

Module Progress:
"""
        
        for module, data in self.progress["modules"].items():
            status = "✓" if data["completed"] else f"{data['progress_pct']:.0f}%"
            report += f"  - {module}: {status} ({len(data['lessons_completed'])} lessons)\n"
        
        report += "\n" + "="*60
        return report


# Convenience function for quick access
def get_tracker(base_path: str = ".") -> ProgressTracker:
    """Get or create a progress tracker instance."""
    return ProgressTracker(base_path)