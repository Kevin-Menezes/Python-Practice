import justpy as jp

import pandas
from datetime import datetime
from pytz import utc


# Dataframe
df = pandas.read_csv("6)_EDA/reviews.csv",parse_dates=["Timestamp"])
df['Month'] = df['Timestamp'].dt.strftime('%Y-%m') # Extracting only months
month_average = df.groupby(['Month']).mean()
print(month_average)

# Creating a string with the code from HighChart website -> Spline chart
chart_def = """ 

{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Dates'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 2018-1-1 to 2021-3-19'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Ratings'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 3.5 to 5.5'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Ratings',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}

"""

# Function that creates webpage
def app():
    wp = jp.QuasarPage() # Creating main page...Quasar is a framework from JS

    h1 = jp.QDiv(a=wp,text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp,text="These graphs represent course review analysis", classes="text-center q-mb-md")

    hc = jp.HighCharts(a=wp,options=chart_def) # Create object to access the dictionaries in the string

    hc.options.title.text = "Average Rating by Month" # 'options' gives u to access the string on top and make changes
    
    hc.options.xAxis.categories = list(month_average.index) # Creating a new key in the string
    hc.options.series[0].data = list(month_average['Rating'])
    
    return wp

jp.justpy(app) # Calling the function
