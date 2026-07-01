import pandas as pd
import numpy as np
import json

ipl_matches ="https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches=pd.read_csv(ipl_matches)
def teamAPI():
    teams = matches["Team1"].unique().tolist()

    team_dict={
        "teams":teams
    }
    return team_dict
def teamVteamAPI(team1,team2):
    try:

        valid_teams = matches["Team1"].unique().tolist()

        if team1 in valid_teams and team2 in valid_teams:

            temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (matches['Team2'] == team1)]
            total_matches = temp_df.shape[0]

            matches_won_team1 = temp_df['WinningTeam'].value_counts().get(team1,0)
            matches_won_team2 = temp_df['WinningTeam'].value_counts().get(team2,0)

            draws = total_matches - (matches_won_team1 + matches_won_team2)

            response = {
                'total_matches': str(total_matches),
                team1: str(matches_won_team1),
                team2: str(matches_won_team2),
                'draws': str(draws)
            }

            return response
        else:
            return {'message':'invalid team name'}
    except Exception as e:
        print("error is:",e)

def allrecord(team):
    try:
        df=matches[(matches["Team1"]==team) | (matches['Team2']==team)].copy()
        mp=df.shape[0]
        won = df[df.WinningTeam == team].shape[0]
        nr=df[df.WinningTeam.isnull()].shape[0]
        loss=mp-won-nr
        nt = df[(df.MatchNumber == 'Final') & (df.WinningTeam == team)].shape[0]
        return {
            "MatchesPlayed": mp,
            "MatchesWon": won,
            "MatchesLost": loss,
            "number_of_Title": nt
            }
    except:
        print("error:")

def teamAPI(team):
    df=[(matches["Team1"]==team) | (matches["Team2"]==team)]
    self_record=allrecord(team)
    Teams=matches.Team1.unique()
    against={team2 : teamVteamAPI(team,team2) for team2 in Teams }
    data = {
        team:{
            "overall":self_record,
            "against":against
        }
    }
    return json.dumps(data)

def city(te,c):
    a=matches[(matches["City"]==c) & ((matches["Team1"]==te)|(matches["Team2"]==te))].shape[0]
    b=matches[(matches["City"]==c) & (matches["WinningTeam"]==te)].shape[0]
    try:
        per=(b/a)*100
        result = f"{per:.2f}"
    except ZeroDivisionError as e:
        print(e)
    
    response={
        "city" : c,
        te:{
        "played" : str(a),
        "won" :str(b),
        "winning_percent":result
        }
    }
    return json.dumps(response)




