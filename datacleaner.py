import pandas as pd
import numpy as np
import re
import os
import itertools

games = []
for filename in os.listdir('game_data/eng1819'):
    filename = filename.split('_')
    home_team = filename[1]
    away_team = filename[-1]
    away_team = away_team[:-4]
    if filename[0] == 'half':
        x = filename[1]+'_'+filename[2]
        half = open("game_data/eng1819/half"+"_"+x, "r")
        half = half.read()
        half = half.split('\n')
        end = open("game_data/eng1819/endd"+"_"+x, "r")
        end = end.read()
        end = end.split('\n')

        info = open("game_data/eng1819/info"+"_"+x, "r")
        info = info.read()
        info = info.split('\n')
        time = info[1].split(' ')
        date = time[0]

        pattern = '\s+\d\s[^A-Za-z0-9]\s\d'
        goal = open("game_data/eng1819/goal"+"_"+x, "r")
        goal = goal.read()
        goal = goal.split('\n')
        goals = []
        for i in goal:
            result = re.findall(r"\s?\s*\d\s[^A-Za-z0-9]\s\d\s*", i)
            if result:
                for i in result:
                    g = re.findall(r"\d", i)
                    if g:
                        goals.append((int(g[0]), int(g[1])))
        home_g_half = goals[0][0]
        away_g_half = goals[0][1]
        home_g_end = goals[1][0]+goals[1][0]
        away_g_end = goals[0][1]+goals[1][1]
#        print(date, "\n", home_team, "-", away_team, "\n", "half:", home_g_half,
#              "-", away_g_half, "\n", "result:", home_g_end, "-", away_g_end)


        triplets1 = []
        i = 0
        while i < len(half):
            triplets1.append(half[i:i+3])
            i += 3

        triplets2 = []
        i = 0
        while i < len(end):
            triplets2.append(end[i:i+3])
            i += 3

        half = pd.DataFrame(triplets1, columns=['Home1', 'label', 'Away1'])
        stacked = half.set_index('label').stack()
        labels1 = [f"{a} - {b}" for a,b in stacked.index]
        half = pd.DataFrame({'data': stacked.values, 'labels': labels1})
        half=half.set_index('labels').transpose()
        half['Ball Possession - Home1']=half['Ball Possession - Home1'][0][0:2]
        half['Ball Possession - Away1']=half['Ball Possession - Away1'][0][0:2]

        end = pd.DataFrame(triplets2, columns=['Home_end', 'label', 'Away_end'])
        stacked = end.set_index('label').stack()
        labels2 = [f"{a} - {b}" for a,b in stacked.index]
        end = pd.DataFrame({'data': stacked.values, 'labels': labels2})
        end=end.set_index('labels').transpose()
        end['Ball Possession - Home_end']=end['Ball Possession - Home_end'][0][0:2]
        end['Ball Possession - Away_end']=end['Ball Possession - Away_end'][0][0:2]
        end['Home']=home_team
        end['Away']=away_team
        end['Home_end_goal']=home_g_end
        end['Away_end_goal']=away_g_end
        end['Date']=date

        game=pd.concat([half, end], axis=1)
        game.reset_index(inplace = True)
        game=pd.DataFrame(game)
        game['col'] = pd.to_datetime(game['Date'])
        del game['col']
        del game['index']
        game.set_index(['Date'], inplace=True)
        game['home_goal1']=home_g_half
        game['away_goal1']=away_g_half
        cols = game.select_dtypes(exclude=['float']).columns
#        print(len(cols), home_team, away_team)
        game[cols] = game[cols].apply(pd.to_numeric, downcast='float', errors='coerce')
        game['Home']=home_team
        game['Away']=away_team
        games.append(game)
gameler = pd.concat(games, sort=False)

gameler=gameler[['Home','Away', 'Ball Possession - Home1', 'Ball Possession - Away1',
                 'Goal Attempts - Home1', 'Goal Attempts - Away1',
                 'Shots on Goal - Home1', 'Shots on Goal - Away1','Corner Kicks - Home1', 'Corner Kicks - Away1',
                 'Yellow Cards - Home1', 'Yellow Cards - Away1',
                 'Total Passes - Home1', 'Total Passes - Away1','Attacks - Home1', 'Attacks - Away1',
                 'Dangerous Attacks - Home1', 'Dangerous Attacks - Away1','home_goal1', 'away_goal1',
                 'Home_end_goal','Away_end_goal','Ball Possession - Home_end','Ball Possession - Away_end',
                 'Goal Attempts - Home_end','Goal Attempts - Away_end',
                 'Shots on Goal - Home_end', 'Shots on Goal - Away_end','Corner Kicks - Home_end', 'Corner Kicks - Away_end',
                 'Yellow Cards - Home_end','Yellow Cards - Away_end',
                 'Total Passes - Home_end','Total Passes - Away_end','Attacks - Home_end', 'Attacks - Away_end',
                 'Dangerous Attacks - Home_end', 'Dangerous Attacks - Away_end'
                ]]

gameler.to_csv('./eng1819.csv', sep='\t')
