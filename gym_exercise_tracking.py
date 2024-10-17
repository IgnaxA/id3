from attr_transform import AttrTransform
from typing import List, Mapping


class GymExerciseTracker:
    def __init__(self):
        pass

    @staticmethod
    def get_path_to_dataset() -> str:
        return "gym_members_exercise_tracking.csv"

    @staticmethod
    def get_age() -> str:
        return "age"

    @staticmethod
    def get_gender() -> str:
        return "gender"

    @staticmethod
    def get_weight() -> str:
        return "weight"

    @staticmethod
    def get_height() -> str:
        return "height"

    @staticmethod
    def get_session_duration() -> str:
        return "session_duration"

    @staticmethod
    def get_workout_type() -> str:
        return "workout_type"

    @staticmethod
    def get_experience_level():
        return "experience_level"

    @staticmethod
    def get_avg_bpm() -> str:
        return "avg_bpm"

    @staticmethod
    def get_attrs_transform() -> List[AttrTransform]:
        return [
            AttrTransform(GymExerciseTracker.get_age(), GymExerciseTracker.transform_age),
            AttrTransform(GymExerciseTracker.get_gender(), GymExerciseTracker.transform_gender),
            AttrTransform(GymExerciseTracker.get_weight(), GymExerciseTracker.transform_weight),
            AttrTransform(GymExerciseTracker.get_height(), GymExerciseTracker.transform_height),
            AttrTransform(GymExerciseTracker.get_session_duration(), GymExerciseTracker.transform_session_duration),
            AttrTransform(GymExerciseTracker.get_workout_type(), GymExerciseTracker.transform_workout_type),
            AttrTransform(GymExerciseTracker.get_avg_bpm(), GymExerciseTracker.transform_avg_bpm),
        ]

    @staticmethod
    def get_attrs_to_rename() -> Mapping[str, str]:
        return {
          "Age": GymExerciseTracker.get_age(),
          "Gender": GymExerciseTracker.get_gender(),
          "Weight (kg)": GymExerciseTracker.get_weight(),
          "Height (m)": GymExerciseTracker.get_height(),
          "Session_Duration (hours)": GymExerciseTracker.get_session_duration(),
          "Workout_Type": GymExerciseTracker.get_workout_type(),
          "Experience_Level": GymExerciseTracker.get_experience_level(),
          "Avg_BPM": GymExerciseTracker.get_avg_bpm(),
        }

    @staticmethod
    def get_attrs() -> List[str]:
        return [
            GymExerciseTracker.get_age(),
            GymExerciseTracker.get_gender(),
            GymExerciseTracker.get_weight(),
            GymExerciseTracker.get_height(),
            GymExerciseTracker.get_session_duration(),
            GymExerciseTracker.get_workout_type(),
            GymExerciseTracker.get_experience_level(),
        ]

    @staticmethod
    def get_target() -> str:
        return GymExerciseTracker.get_avg_bpm()

    @staticmethod
    def transform_age(value: int) -> int:
        if value <= 22:
            return 0
        if value <= 26:
            return 1
        if value <= 30:
            return 2
        if value <= 34:
            return 3
        if value <= 39:
            return 4
        if value <= 43:
            return 5
        if value <= 47:
            return 6
        if value <= 51:
            return 7
        if value <= 55:
            return 8
        if value > 55:
            return 9

    @staticmethod
    def transform_gender(gender: str) -> int:
        return 1 if gender == "Male" else 0

    @staticmethod
    def transform_weight(value: float) -> int:
        if value <= 49:
            return 0
        if value <= 58:
            return 1
        if value <= 67:
            return 2
        if value <= 76:
            return 3
        if value <= 85:
            return 4
        if value <= 94:
            return 5
        if value > 94:
            return 6

    @staticmethod
    def transform_height(value: float) -> int:
        if value <= 1.6:
            return 0
        if value <= 1.65:
            return 1
        if value <= 1.75:
            return 2
        if value <= 1.85:
            return 3
        if value > 1.85:
            return 4

    @staticmethod
    def transform_session_duration(value: float) -> int:
        if value <= 0.95:
            return 0
        if value <= 1.10:
            return 1
        if value <= 1.25:
            return 2
        if value <= 1.40:
            return 4
        if value > 1.40:
            return 5


    @staticmethod
    def transform_workout_type(workout_type: str) -> int:
        if workout_type == "Yoga":
            return 0
        if workout_type == "HIIT":
            return 1
        if workout_type == "Cardio":
            return 2
        if workout_type == "Strength":
            return 3
        return -1

    @staticmethod
    def transform_avg_bpm(value: float) -> int:
        if value <= 124.90:
            return 0
        if value <= 129.80:
            return 1
        if value <= 134.70:
            return 2
        if value <= 139.60:
            return 3
        if value <= 144.50:
            return 4
        if value <= 149.40:
            return 5
        if value <= 154.30:
            return 6
        if value <= 159.20:
            return 7
        if value <= 164.10:
            return 8
        if value > 164.10:
            return 9