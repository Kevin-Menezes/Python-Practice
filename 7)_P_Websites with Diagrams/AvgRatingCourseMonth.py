import justpy as jp

import pandas
from datetime import datetime
from pytz import utc


# Dataframe
df = pandas.read_csv("6)_EDA/reviews.csv",parse_dates=["Timestamp"])
df['Month'] = df['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = df.groupby(['Month','Course Name'])['Rating'].mean().unstack()
print(month_average_crs)

# Creating a string with the code from HighChart website -> Spline chart
chart_def = """ 

{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average Ratings of Course by Month'
    },
    subtitle: {
        align: 'center',
        text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {

        categories:['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'],

        plotBands: [{ // Highlight the two last years
            from: 2019,
            to: 2020,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Average Ratings'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Rating in month of {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0
        }
    },
    series: [{
        name: 'Moose',
        data:
            [
                38000,
                37300,
                37892,
                38564,
                36770,
                36026,
                34978,
                35657,
                35620,
                35971,
                36409,
                36435,
                34643,
                34956,
                33199,
                31136,
                30835,
                31611,
                30666,
                30319,
                31766
            ]
    }, {
        name: 'Deer',
        data:
            [
                22534,
                23599,
                24533,
                25195,
                25896,
                27635,
                29173,
                32646,
                35686,
                37709,
                39143,
                36829,
                35031,
                36202,
                35140,
                33718,
                37773,
                42556,
                43820,
                46445,
                50048
            ]
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
    
    hc.options.xAxis.categories = list(month_average_crs.index) # Creating a new key in the string
    
    hc_data = [{"name":v1,"data":[v2 for v2 in month_average_crs[v1]]}for v1 in month_average_crs.columns] # This is to dynamically create and insert list data
    
    hc.options.series = hc_data
    
    return wp

jp.justpy(app) # Calling the function
