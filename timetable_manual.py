import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
import matplotlib.colors as mcolors
import random

if plt.get_backend() == 'MacOSX':
    rc('font', family='Apple SD Gothic Neo')
else:
    rc('font', family='Malgun Gothic')

# Class schedule data
data = [
    {"Subject": "이산수학", "Days": "수", "Hours": "2,3"},
    {"Subject": "이산수학", "Days": "수", "Hours": "7,8,9"},
    {"Subject": "이산수학", "Days": "수", "Hours": "4,5"},
    {"Subject": "C언어프로그래밍", "Days": "수", "Hours": "1,2,3"},
    {"Subject": "C언어프로그래밍", "Days": "월", "Hours": "4,5,6"},
    {"Subject": "C언어프로그래밍", "Days": "목", "Hours": "4,5,6"},
    {"Subject": "C언어프로그래밍", "Days": "목", "Hours": "1,2,3"},
    {"Subject": "C언어프로그래밍", "Days": "목", "Hours": "1,2,3,4"},
    {"Subject": "C언어프로그래밍", "Days": "목", "Hours": "5,6,7"},
    {"Subject": "C언어프로그래밍", "Days": "금", "Hours": "1,2,3,4"},
    {"Subject": "파이썬 프로그래밍", "Days": "월", "Hours": "7,8,9"},
    {"Subject": "파이썬 프로그래밍", "Days": "월", "Hours": "7,8,9"},
    {"Subject": "파이썬 프로그래밍", "Days": "화", "Hours": "7,8,9"},
    {"Subject": "파이썬 프로그래밍", "Days": "목", "Hours": "7,8,9"},
    {"Subject": "파이썬 프로그래밍", "Days": "목", "Hours": "1,2,3"},
    {"Subject": "파이썬 프로그래밍", "Days": "목", "Hours": "7,8,9"},
    {"Subject": "논리회로 및 실습", "Days": "수", "Hours": "5,6,7,8"},
    {"Subject": "자료구조론", "Days": "화", "Hours": "2,3"},
    {"Subject": "자료구조론", "Days": "화", "Hours": "6,7"},
    {"Subject": "자료구조론", "Days": "월", "Hours": "5,6"},
    {"Subject": "자료구조론", "Days": "수", "Hours": "1,2"},
    {"Subject": "자료구조론", "Days": "수", "Hours": "6,7"},
    {"Subject": "유닉스시스템", "Days": "월", "Hours": "7,8,9"},
    {"Subject": "JAVA 프로그래밍", "Days": "월", "Hours": "4,5,6"},
    {"Subject": "JAVA 프로그래밍", "Days": "화", "Hours": "2,3,4"},
    {"Subject": "JAVA 프로그래밍", "Days": "월", "Hours": "7,8,9"},
    {"Subject": "C++프로그래밍", "Days": "월", "Hours": "1,2,3"},
    {"Subject": "C++프로그래밍", "Days": "화", "Hours": "4,5,6"},
    {"Subject": "C++프로그래밍", "Days": "목", "Hours": "1,2,3"},
    {"Subject": "선형대수학", "Days": "목", "Hours": "1,2"},
    {"Subject": "빅데이터", "Days": "목", "Hours": "1,2,3"},
    {"Subject": "센서공학", "Days": "수", "Hours": "1,2,3"},
    {"Subject": "웹프로그래밍", "Days": "목", "Hours": "7,8,9"},
    {"Subject": "파이썬응용", "Days": "화", "Hours": "2,3,4"},
    {"Subject": "파이썬응용", "Days": "목", "Hours": "4,5,6"},
    {"Subject": "파이썬응용", "Days": "수", "Hours": "1,2,3"},
    {"Subject": "파이썬응용", "Days": "금", "Hours": "4,5,6"},
    {"Subject": "데이터통신", "Days": "월", "Hours": "5,6,7"},
    {"Subject": "컴퓨터 구조론", "Days": "수", "Hours": "1,2,3"},
    {"Subject": "컴퓨터 구조론", "Days": "목", "Hours": "1,2,3"},
    {"Subject": "인공지능", "Days": "화", "Hours": "2,3"},
    {"Subject": "데이터베이스이론 및 실습", "Days": "월", "Hours": "5,6,7"},
    {"Subject": "데이터베이스이론 및 실습", "Days": "화", "Hours": "5,6,7,8"},
    {"Subject": "데이터베이스이론 및 실습", "Days": "수", "Hours": "5,6,7,8"},
    {"Subject": "IoT응용제어", "Days": "목", "Hours": "5,6,7,8"},
    {"Subject": "디지털영상처리", "Days": "수", "Hours": "1,2,3"},
    {"Subject": "알고리즘 및 실습", "Days": "수", "Hours": "1,2,3"},
    {"Subject": "알고리즘 및 실습", "Days": "수", "Hours": "7,8,9"},
    {"Subject": "알고리즘 및 실습", "Days": "월", "Hours": "5,6,7"},
    {"Subject": "캡스톤디자인", "Days": "금", "Hours": "1,2"},
    {"Subject": "캡스톤디자인", "Days": "수", "Hours": "1,2"},
    {"Subject": "캡스톤디자인", "Days": "목", "Hours": "5,6"},
    {"Subject": "딥러닝 프로그래밍", "Days": "수", "Hours": "7,8,9"},
    {"Subject": "딥러닝 프로그래밍", "Days": "화", "Hours": "2,3,4"},
    {"Subject": "파이썬응용", "Days": "수", "Hours": "1,2,3"},
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Create a mapping for days and hours
day_mapping = {"월": 0, "화": 1, "수": 2, "목": 3, "금": 4}
hour_labels = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"]
hour_mapping = {i: i-1 for i in range(1, 10)}

# Initialize the timetable grid
timetable = np.empty((9, 5), dtype=object)
timetable[:] = ""

# Function to check if the time slot is available
def is_time_slot_available(selected_days, selected_hours):
    for day in selected_days:
        for hour in selected_hours:
            if timetable[hour_mapping[hour], day_mapping[day]] != "":
                return False
    return True

# Function to select a time slot
def select_time_slot(row, selected_days, selected_hours):
    for day in selected_days:
        for hour in selected_hours:
            timetable[hour_mapping[hour], day_mapping[day]] = row['Subject']

# Allow user to input desired time slots
desired_time_slots = []
subjects = df['Subject'].unique()

for subject in subjects:
    print(f"Select a time slot for {subject}. Available options are:")
    subject_data = df[df['Subject'] == subject]
    options = list(subject_data.iterrows())
    for i, (index, row) in enumerate(options):
        print(f"Option {i + 1}: Days - {row['Days']}, Hours - {row['Hours']}")
    
    while True:
        user_input = input(f"Enter the option number for {subject}, 'skip' to skip this subject, or 'done' to finish: ")
        if user_input.lower() == 'skip':
            break
        if user_input.lower() == 'done':
            break
        try:
            option_index = int(user_input) - 1
            if option_index < 0 or option_index >= len(options):
                raise ValueError
            selected_row = options[option_index][1]
            days = selected_row['Days'].split(',')
            hours = list(map(int, selected_row['Hours'].split(',')))
            if is_time_slot_available(days, hours):
                select_time_slot(selected_row, days, hours)
                desired_time_slots.append({"Subject": subject, "Days": selected_row['Days'], "Hours": selected_row['Hours']})
                break
            else:
                print("The selected time slot is not available. Please choose another option.")
        except ValueError:
            print("Invalid input. Please enter a valid option number.")
    if user_input.lower() == 'done':
        break

# Generate a color map for subjects
unique_subjects = df['Subject'].unique()
colors = random.sample(list(mcolors.CSS4_COLORS.values()), len(unique_subjects))
color_map = dict(zip(unique_subjects, colors))

# Plot the timetable
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 5)
ax.set_ylim(0, 9)
ax.set_xticks(np.arange(5))
ax.set_xticklabels(["월", "화", "수", "목", "금"])
ax.set_yticks(np.arange(9))
ax.set_yticklabels(hour_labels)
ax.invert_yaxis()  # To match the usual top-down order of a timetable
ax.grid(True)

# Add rectangles and text annotations
for i in range(9):
    for j in range(5):
        subject = timetable[i, j]
        if subject != "":
            ax.add_patch(plt.Rectangle((j, i), 1, 1, color=color_map.get(subject, 'white'), ec='black'))
            text = ax.text(j + 0.5, i + 0.5, subject, ha="center", va="center", fontsize=8, clip_on=True)

ax.set_title("Class Timetable")
fig.tight_layout()

# Save the timetable as an image
image_filename = "timetable_colored_with_time.png"
plt.savefig(image_filename)

print(f"Timetable saved as {image_filename}")
