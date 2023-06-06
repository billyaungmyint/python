#simple dictionary

capitals = { 
    "France" : "Paris",
    "Germany": "Berlin"
}

#list in a dictionary

travel_countries = {
    "France" : ["Paris", "Lillie" , "Montellier"],
    "Germany": ["Munich","Berlin","ABC"]
}


#dictionary in a dictionary

travel_dict = {
    "Countries" : travel_countries,
    "Capitals" : capitals
    
}

travel_log = {
    "France" :  {"cities_visited" : ["Paris" , "Lille" , "Dijon"] , "total_visits" : 12},
    "Germany": ["Berlin" , "Hamburg" , "Stuttggart"]
}

#list in a dictionary in a list

traven_log = [
    {
        "Country" : "France",
        "cities_visited" : ["Paris" , "Lille" , "Dijon"],
        "total_visit" : 12
    },
    {
        "Country" : "Germany",
        "cities_visited" : ["Berlin" , "Hamburg" , "Stuttggart"],
        "total_visit" : 5
    }
]