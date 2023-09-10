json  = {"weather" : [{
    "id" : 804,
    "main" : "Cloud",
    "description" : "Overcasts Clouds",
    "icon" : "04d"
}]
}

#aim extract "description" value
print(json.get("weather")[0].get("description"))