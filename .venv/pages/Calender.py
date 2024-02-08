import streamlit as st
import calendar
from datetime import datetime

# Get the current date
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

# Create a calendar for the current month
cal = calendar.monthcalendar(current_year, current_month)

# Streamlit app
st.title("Calender")

# Display the current month and year
st.write(f"Current Month: {calendar.month_name[current_month]} {current_year}")

# Create a table to display the calendar
col_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Display each week in a separate row
for week in cal:
    week_str = []
    for day in week:
        if day == 0:
            week_str.append(" ")
        else:
            day_of_week = calendar.day_name[(calendar.weekday(current_year, current_month, day))]
            if day == current_day:
                week_str.append(f"<span style='color:red'><b>{day_of_week}, {day}</b></span>")
            else:
                week_str.append(f"<span style='color:orange'>{day_of_week}, {day}</span>")
    st.write("  ".join(week_str), unsafe_allow_html=True)

# Display the day of the week
day_of_week = now.strftime("%A")
day_of_month = now.strftime("%d")
st.write(f"\nToday is {day_of_week}, {calendar.month_name[current_month]} {day_of_month}th")
