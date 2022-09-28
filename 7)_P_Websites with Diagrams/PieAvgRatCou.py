import justpy as jp

import pandas
from datetime import datetime
from pytz import utc


# Dataframe
df = pandas.read_csv("6)_EDA/reviews.csv",parse_dates=["Timestamp"])
share = df.groupby(['Course Name'])['Rating'].count()

# Creating a string with the code from HighChart website -> Pie chart
chart_def = """ 

{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in May, 2020'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 70.67,
            sliced: true,
            selected: true
        }, {
            name: 'Edge',
            y: 14.77
        },  {
            name: 'Firefox',
            y: 4.86
        }, {
            name: 'Safari',
            y: 2.63
        }, {
            name: 'Internet Explorer',
            y: 1.53
        },  {
            name: 'Opera',
            y: 1.40
        }, {
            name: 'Sogou Explorer',
            y: 0.84
        }, {
            name: 'QQ',
            y: 0.51
        }, {
            name: 'Other',
            y: 2.6
        }]
    }]
}

"""

# Function that creates webpage
def app():
    wp = jp.QuasarPage() # Creating main page...Quasar is a framework from JS

    h1 = jp.QDiv(a=wp,text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp,text="These graphs represent course review analysis", classes="text-center q-mb-md")

    hc = jp.HighCharts(a=wp,options=chart_def) # Create object to access the dictionaries in the string

    hc_data = [{"name":v1,"y":v2} for v1,v2 in zip(share.index,share)]
    print(hc_data)

    hc.options.series[0].data = hc_data
    
    return wp

jp.justpy(app) # Calling the function
