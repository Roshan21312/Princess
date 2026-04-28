import streamlit as st
import pandas as pd
import datetime
import calendar
from supabase import create_client

# ------------------- CONFIG -------------------
st.set_page_config(page_title="Habit Tracker", layout="wide",initial_sidebar_state="collapsed")

st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
    }
    
</style>
""", unsafe_allow_html=True)


# ------------------- SUPABASE -------------------

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ------------------- DATE SETUP -------------------
today = datetime.date.today()
year = today.year
month = today.month
# month_key = today.strftime("%Y-%m")
# current_month_name = today.strftime("%B")
num_days = calendar.monthrange(year, month)[1]

date_columns = []
for day in range(1, num_days + 1):
    date_obj = datetime.date(year, month, day)
    day_str = date_obj.strftime("%a")[:3]
    date_columns.append(f"{day_str} {day}/{month}/{year}")


# ------------------- MONTH SELECTOR -------------------

# Fetch all months from DB
def get_all_months():
    response = supabase.table("habits_log").select("month").execute()
    months = list(set([r["month"] for r in response.data]))

    # Always include current month
    current = today.strftime("%Y-%m")
    if current not in months:
        months.append(current)

    return sorted(months, reverse=True)

available_months = get_all_months()

selected_month = st.sidebar.selectbox(
    "Select Month",
    available_months,
    index=0
)

# Override month_key based on selection
month_key = selected_month

# Update year/month accordingly
year = int(month_key.split("-")[0])
month = int(month_key.split("-")[1])

current_month_name = datetime.date(year, month, 1).strftime("%B")

st.title("Princess's Habit Tracker")
st.write(f"{current_month_name}")

# ------------------- DB FUNCTIONS -------------------

def get_active_habits(month_key):
    response = supabase.table("habits_master").select("*").execute()
    habits = []

    for r in response.data:
        if r["created_month"] <= month_key and (
            r["deleted_month"] is None or r["deleted_month"] > month_key
        ):
            habits.append(r["habit"])

    return habits


def add_habit(habit, month_key):
    supabase.table("habits_master").insert({
        "habit": habit,
        "created_month": month_key,
        "deleted_month": None
    }).execute()


def remove_habit(habit, month_key):
    supabase.table("habits_master")\
        .update({"deleted_month": month_key})\
        .eq("habit", habit)\
        .execute()


def load_data(habits, date_columns, month_key):
    response = supabase.table("habits_log")\
        .select("*")\
        .eq("month", month_key)\
        .execute()

    records = response.data

    data_map = {}
    for r in records:
        habit = r["habit"]
        date = r["date"]
        status = r["status"]

        if habit not in data_map:
            data_map[habit] = {}
        data_map[habit][date] = status

    data = []
    for habit in habits:
        row = {"Habit": habit}
        for col in date_columns:
            row[col] = data_map.get(habit, {}).get(col, False)
        data.append(row)

    return pd.DataFrame(data)


def save_data(df, month_key):
    records = []

    for _, row in df.iterrows():
        habit = row["Habit"]

        for col in df.columns[1:]:
            records.append({
                "habit": habit,
                "date": col,
                "month": month_key,
                "status": bool(row[col])
            })

    if records:  # important check
        supabase.table("habits_log")\
            .upsert(records, on_conflict="habit,date,month")\
            .execute()

# ------------------- HABITS -------------------

habits = get_active_habits(month_key)

with st.expander("Manage Habits (Max 10)", expanded=False):
    col1, col2 = st.columns([3, 1])

    with col1:
        new_habit = st.text_input(
            "Add a new habit",
            label_visibility="collapsed",
            placeholder="Enter habit name..."
        )

    with col2:
        if st.button("Add Habit", use_container_width=True):
            if len(habits) >= 10:
                st.error("Max 10 habits allowed")
            elif new_habit and new_habit not in habits:
                add_habit(new_habit, month_key)
                st.rerun()

    st.caption("Current Habits:")
    for i, habit in enumerate(habits):
        col_text, col_btn = st.columns([4, 1])
        col_text.write(habit)

        if col_btn.button("Remove", key=f"del_{i}"):
            remove_habit(habit, month_key)
            st.rerun()

# ------------------- DATAFRAME -------------------

df = load_data(habits, date_columns, month_key)

st.subheader("My Habits")

column_config = {
    "Habit": st.column_config.Column(width="medium")
}

for col in date_columns:
    column_config[col] = st.column_config.CheckboxColumn(width="small")

edited_df = st.data_editor(
    df,
    hide_index=True,
    use_container_width=True,
    disabled=["Habit"],
    column_config=column_config,
    key="habit_editor"
)

# ------------------- AUTO SAVE -------------------

if edited_df is not None:
    save_data(edited_df, month_key)


# ------------------- PROGRESS GRAPH -------------------

st.subheader("Daily Progress (%)")

if edited_df is not None and len(edited_df) > 0:
    total_habits = len(edited_df)

    progress_data = []

    for col in edited_df.columns[1:]:
        done = edited_df[col].sum()
        percent = (done / total_habits) * 100
        progress_data.append(percent)

    progress_df = pd.DataFrame({
        "Day": range(1, len(progress_data) + 1),
        "Completion %": progress_data
    })

    st.line_chart(progress_df.set_index("Day"))

st.markdown("""
<style>
.footer {
    position: fixed;
    bottom: 10px;
    width: 100%;
    text-align: center;
    font-size: 14px;
    color: grey;
}
.footer span {
    color: red;
    font-weight: bold;
}
</style>

<div class="footer">
    Made with love <span>❤️</span> by your's only Roshan Zambare
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.footer {
    position: fixed;
    bottom: 10px;
    width: 100%;
    text-align: center;
    font-size: 14px;
    color: grey;
}
.footer span {
    color: red;
    font-weight: bold;
}
</style>

<div class="footer">
    Made with love <span>❤️</span> by your's only Roshan Zambare
</div>
""", unsafe_allow_html=True)
