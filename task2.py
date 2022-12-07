a={
    "properties":{
        "profile":{
            "name": "ram",
            "education":[
                    {"college": "ABC", "year": 2018},
                    {"college": "XYZ", "year": 2020},
            ]
            
            
        },
        "followers": 10000,
        "following": 100,
    }
}

# name=a.get("properties").get("profile").get("name")
# followers = a.get("properties").get("followers")
# following = a.get("properties").get("following")
# print(f"Name: {name.capitalize()}")
# print(f"followers: {followers}")
# print(f"following: {following}")
# educations=a.get("properties").get("profile").get("education")
# for education in educations:
#     college=education.get("college")
#     year=education.get("year")
# print(f"Education({year}):{college.upper()}")

oil_prices=[
    {
        "oil_type": "petrol",
        "prices":[
            {"year":2018, "price":100},
            {"year":2019, "price":150},
            {"year":2020, "price":180},
        ]
    },
    {
        "oil_type": "diesel",
        "prices":[
            {"year":2018, "price":80},
            {"year":2019, "price":100},
            {"year":2020, "price":160},
        ]

    }
]

for item in oil_prices:
    print("Oil Type:", item.get('oil_type'))
    for year in item.get('prices'):
        print(f'Price({year.get("year")}):', year.get("price"))
    print("\n\n")
