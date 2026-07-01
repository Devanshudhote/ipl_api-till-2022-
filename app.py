from flask import Flask,jsonify,json,request
import ipl

app=Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/api/teams')
def teams():
    teams=ipl.teamAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = ipl.teamVteamAPI(team1,team2)
    print(response)
    return jsonify(response)

@app.route('/api/team-record')
def record():
    t=request.args.get("team")
    response=ipl.teamAPI(t)
    return (response)

@app.route('/api/team-and-city')
def team_city():
    team=request.args.get("team")
    city=request.args.get("city")
    response=ipl.city(team,city)
    return response

app.run()
