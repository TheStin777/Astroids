from constants import *

def get_points_for_asteroid(radius):
    #Calculate the Medium Radius
    medium_radius = ASTEROID_MIN_RADIUS * 2
    
    #20 points for Large Asteroid
    if radius == ASTEROID_MAX_RADIUS:
        return 20
    
    #50 points for Medium Asteroid
    elif radius == medium_radius:
        return 50
    
    #100 points if Small Asteroid
    elif radius == ASTEROID_MIN_RADIUS:
        return 100
    
    #IF there is an error, fallback is 10 point
    else:
        return 10

def get_highscore():
    pass

def save_high_score(score):
    pass

def get_leaderboard():
    pass

def add_to_leaderboard():
    pass