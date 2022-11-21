import datetime
import  pandas as pd
import calendar

def max_week_return():
    today = datetime.date.today()

    year = today.year
    month = today.month
    day = today.day
    weeks = []

    for i in range(1, calendar.monthrange(year, month)[1]):
        datem = datetime.date(year, month, i)
        weeks.append(int(datem.isocalendar()[1]))

    df = pd.DataFrame(weeks, columns=["weeks"])
    df = pd.DataFrame(df['weeks'].value_counts())
    df.reset_index(inplace=True)
    max_week = df['index'].max()
    max_week_prev = df['index'].max() - 1
    if df[df['index'] == max_week].iloc[0, 1] > df[df['index'] == max_week_prev].iloc[0, 1]:
        max_week_number = df[df['index'] == max_week].iloc[0, 0]
    else:
        max_week_number = df[df['index'] == max_week_prev].iloc[0, 0]

    return max_week_number