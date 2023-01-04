import datetime
import  pandas as pd
import calendar

def max_week_return():
    today = datetime.date.today()

    year = today.year
    month = today.month
    day = today.day
    weeks = []

    curr_week = str(today.isocalendar()[1])
    curr_week = "2023" + curr_week

    for i in range(1, calendar.monthrange(year, month)[1]):
        print(i)
        datem = datetime.date(year, month, i)
        weeks.append(int(datem.isocalendar()[1]))
    df = pd.DataFrame(weeks, columns=["weeks"])
    if month == 1:
        #delete row with max week index

        df.drop(df['weeks'].idxmax(), inplace=True)


    df = pd.DataFrame(df['weeks'].value_counts())
    df.reset_index(inplace=True)
    max_week = df['index'].max()
    max_week_prev = df['index'].max() - 1

    if df[df['index'] == max_week].iloc[0, 1] > df[df['index'] == max_week_prev].iloc[0, 1]:
        max_week_number = df[df['index'] == max_week].iloc[0, 0]
    else:
        max_week_number = df[df['index'] == max_week_prev].iloc[0, 0]

    max_week_number = str(year) + str(max_week_number)

    return year, month, max_week_number, curr_week
