from typing import List, Mapping

from attr_transform import AttrTransform
from data_frame_parser import DataFrameParser
from id_tree import IdTree
from math import ceil
from pandas import DataFrame

# Age: Age of the gym member.
# Gender: Gender of the gym member (Male or Female).
# Weight (kg): Member’s weight in kilograms.
# Height (m): Member’s height in meters.
# Session_Duration (hours): Duration of each workout session in hours.
# Workout_Type: Type of workout performed (e.g., Cardio, Strength, Yoga, HIIT).
# Experience_Level: Level of experience, from beginner (1) to expert (3).

# Avg_BPM: Average heart rate during workout sessions.

def transform_numeric_value(value: float, step: float) -> int:
  return round(value / step)

def transform_age(value: int) -> int:
  return transform_numeric_value(value, 20)

def transform_gender(gender: str) -> int:
  return 1 if gender == "Male" else 0

def transform_weight(value: float) -> int:
  return transform_numeric_value(value - 39, 40)

def transform_height(value: float) -> int:
  return transform_numeric_value(value - 1.49, 0.1)

def transform_session_duration(value: float) -> int:
  return transform_numeric_value(value - 0.49, 0.5)

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

def transform_avg_bpm(value: float) -> int:
  return transform_numeric_value(value - 119, 10)

transform_attrs: List[AttrTransform] = [
  AttrTransform("age", transform_age),
  AttrTransform("gender", transform_gender),
  AttrTransform("weight", transform_weight),
  AttrTransform("height", transform_height),
  AttrTransform("session_duration", transform_session_duration),
  AttrTransform("workout_type", transform_workout_type),
  AttrTransform("avg_bpm", transform_avg_bpm),
]

path_to_dataset: str = "gym_members_exercise_tracking.csv"
attrs_to_rename: Mapping[str, str] = {
  "Age": "age",
  "Gender": "gender",
  "Weight (kg)": "weight",
  "Height (m)": "height",
  "Session_Duration (hours)": "session_duration",
  "Workout_Type": "workout_type",
  "Experience_Level": "experience_level",
  "Avg_BPM": "avg_bpm",
}

attrs: List[str] = [
  "age", "gender", "weight", "height", "session_duration", "workout_type", "experience_level"
]
target = "avg_bpm"


def main():
  df: DataFrameParser = DataFrameParser(path_to_dataset, attrs_to_rename, transform_attrs, attrs, target)
  df.parse()

  data_frame: DataFrame = df.get_data_frame()
  print("-----Height-----")
  print(data_frame["height"].min())
  print(data_frame["height"].max())
  print("-----Weight-----")
  print(data_frame["weight"].min())
  print(data_frame["weight"].max())
  print("-----Avg BPM-----")
  print(data_frame["avg_bpm"].min())
  print(data_frame["avg_bpm"].max())
  print("-----Session Duration-----")
  print(data_frame["session_duration"].min())
  print(data_frame["session_duration"].max())
  print("-----Workout Type-----")
  print(data_frame["workout_type"].unique())
  print("-----Experience Level-----")
  print(data_frame["experience_level"].unique())

  id_tree = IdTree(df)
  id_tree.build()

if __name__ == "__main__":
  main()


