import pandas as pd
import plotly.graph_objs as go
import numpy as np
import requests
import plotly.colors
from collections import defaultdict
from datetime import datetime

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

runner_url = 'https://iupw2unr35.execute-api.ap-southeast-2.amazonaws.com/Prod/runner/'
race_url   = 'https://iupw2unr35.execute-api.ap-southeast-2.amazonaws.com/Prod/race/2020-05-30' 

def extract_runner(runner='AAGAS'):
    """Extract a Runner history run details via API call
    
    Args:
        None
        
    Return
        Runner's race Date List
        Runner's finishing Positions    
    """

    start_date = []
    finishing_position = []    
    odds = []
    margin = []
    runner_name = ''
    
    try:
        r = requests.get(runner_url + runner)
        
        for runner in r.json():            
            
            start_date.append(datetime.strptime(runner['startDate'], '%Y-%m-%d'))
            finishing_position.append(runner['finishingPosition'])
            odds.append(runner['odds'])
            margin.append(runner['margin'])
            runner_name = runner['runnerName']
            
    except Exception as e:
        print(e)       
    
    print(start_date)
    print(finishing_position)
        
    return runner_name, start_date, finishing_position, odds, margin
    

def active_jocky():
    """Test My API Call 
    
    Args:
        None
        
    Return:
        None
    """
    
    try:
        r = requests.get(race_url)
#         data = r.json()
#         print(data)
        
        data = defaultdict(list)
        
        for runner in r.json():
            if not data[runner['riderName']]:
                data[runner['riderName']] = [[],[],[], '', '']
                
            if int(runner['finishingPosition']) >= 0:
                if runner['riderName'] != 'Not declared':
                    data[runner['riderName']][0].append(runner['runnerName'])
                    data[runner['riderName']][1].append(runner['finishingPosition'])
                    data[runner['riderName']][2].append(runner['FixedWinClose'])
                    data[runner['riderName']][3] = runner['last12Months_rider_wins']
                    data[runner['riderName']][4] = runner['riderName']
        
        jocky = []
        last12Win = []
        
        for rider in data:
            if len(data[rider][0]) >= 6:
                jocky.append(data[rider][4])
                last12Win.append(data[rider][3])
#                 print(rider)
#                 print(data[rider][0])
#                 print(data[rider][1])
#                 print(data[rider][2])
#                 print(data[rider][3])
#                 print('\n')
        
    except Exception as e:
        print(e)       
    
    print(jocky)
    print(last12Win)
        
    return jocky, last12Win
    

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    
    runner_name, start_date, finishing_position, odds, margin = extract_runner()
    
    graph_one = []    
    
    graph_one.append(
      go.Scatter(
      x = start_date,
      y = finishing_position,
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'Runner ' + runner_name +  ' Historical Finishing Position',
                xaxis = dict(title = 'Race Date'),
                yaxis = dict(title = 'Finishing Position'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    jokcy, last12m = active_jocky()    

    graph_two = []

    graph_two.append(
      go.Bar(
      x = jokcy,
      y = last12m,
      )
    )

    layout_two = dict(title = 'Riders 12 Months Wins',
                xaxis = dict(title = 'Jocky',),
                yaxis = dict(title = 'Last 12 Months Rider Wins'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = start_date,
      y = odds,
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Runner ' + runner_name + ' Starting Odds ',
                xaxis = dict(title = 'Race Date'),
                yaxis = dict(title = 'Odds')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    
    graph_four.append(
      go.Scatter(
      x = start_date,
      y = margin,
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Runner ' + runner_name + ' Historical Margin',
                xaxis = dict(title = 'Race Date'),
                yaxis = dict(title = 'Margin'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures

if __name__ == "__main__":
    extract_runner()