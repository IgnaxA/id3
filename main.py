
from data_frame_parser import DataFrameParser
from gym_exercise_tracking import GymExerciseTracker
from id_tree import IdTree
from pandas import DataFrame

# Age: Age of the gym member.
# Gender: Gender of the gym member (Male or Female).
# Weight (kg): Member’s weight in kilograms.
# Height (m): Member’s height in meters.
# Session_Duration (hours): Duration of each workout session in hours.
# Workout_Type: Type of workout performed (e.g., Cardio, Strength, Yoga, HIIT).
# Experience_Level: Level of experience, from beginner (1) to expert (3).

# Avg_BPM: Average heart rate during workout sessions.

def main():
  df: DataFrameParser = (DataFrameParser(path_to_dataset = GymExerciseTracker.get_path_to_dataset(),
                                         attrs_to_rename = GymExerciseTracker.get_attrs_to_rename(),
                                         attrs_transform = GymExerciseTracker.get_attrs_transform(),
                                         attrs = GymExerciseTracker.get_attrs(),
                                         target = GymExerciseTracker.get_target())
                         .parse())

  data_frame: DataFrame = df.get_data_frame()
  print(data_frame.head(10)[['age', 'avg_bpm']])
  id_tree = IdTree(data_frame = data_frame.head(200), target = GymExerciseTracker.get_target())
  id_tree.build()
  print(id_tree)

if __name__ == "__main__":
  main()


