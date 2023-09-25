import pandas as pd
from datetime import datetime as dt

names = ['Festival Name', 'Website', 'Start Date', 'End Date', 'City']
df = pd.read_csv("2020 Film Festival Database & Calendar - 2020 DATABASE.csv", usecols=names)
clean_df = df[df["Start Date"] != 'tbd']
pasts = []
after = []
for index, row in clean_df.iterrows():
    festival_name = row['Festival Name']
    site = row['Website']
    start_month, start_day = row['Start Date'].replace("`", "").split("/")[0:2]
    start_month = start_month.zfill(2)
    start_day = start_day.zfill(2)
    start_date = f"{str(dt.now().year)}-{start_month}-{start_day}"
    try:
        formatted_start = dt.strptime(start_date, "%Y-%m-%d").date()
        # print(formatted)
    except ValueError:
        continue

    end_month, end_day = row['End Date'].replace("`", "").split("/")[0:2]
    end_month = end_month.zfill(2)
    end_day = end_day.zfill(2)
    end_date = f"{str(dt.now().year)}-{end_month}-{end_day}"
    try:
        formatted_end = dt.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        continue

    if formatted_start <= dt.utcnow().date() < formatted_end:
        print(festival_name)
    elif formatted_end <= dt.utcnow().date():
        pasts.append(festival_name)
    elif formatted_start > dt.utcnow().date():
        after.append(festival_name)

print(after)
print(sorted(after))
print(pasts)
print(sorted(pasts))
