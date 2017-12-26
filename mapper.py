import json

with open("City_State_US.json") as json_file:
    states_dict = json.load(json_file)

def get_USA_state(place):
    '''
    Search the state of a place, returns the place itself if it is a state yet
    :param city: must be an uppercase string
    :return state:
    '''

    if place in states_dict.keys():
        return place

    for state, cities in states_dict.items():
        if place in cities:
            return state

    return None


print(get_USA_state("BROOKHAVEN"))

ad= "Avon Park"
asd=ad.upper()
print(asd)



with open("twits.json") as f:
    lines = f.readlines()
i=0
for line in lines:
    twit=json.loads(line)
    try:
        if(twit["lang"]=="en"):
            raw_place=twit["place"]["name"]
            us_state = get_USA_state(raw_place.upper())
            if us_state is not None:
               # print("Place name====> " + raw_place+", "+us_state)
                i += 1
    except Exception as ex:
        pass
print(i)

