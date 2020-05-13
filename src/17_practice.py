waypoints = [
    {
        "lat": 43,
        "lon": 121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": 123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": 122,
        "name": "a third place"
    }
]
#FOR DICTS IN WAYPOINTS, PRINT THE NAME OF THE DICT(S) WITH
#"LON" VALUE > 121

# for i in range(0, len(waypoints)):
   
    # print(waypoint.name) for waypoint in waypoints if waypoint.lon > 121
print([waypoint['name'] for waypoint in waypoints if waypoint['lon'] > 121])