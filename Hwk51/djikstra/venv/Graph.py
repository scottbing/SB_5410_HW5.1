import collections, requests, math

# URL of service
URL_PATH = "https://nominatim.openstreetmap.org/search.php"

loc1 = []
loc2 = []

def nested_dict_iter(nested):
    for key, value in nested.items():
        if isinstance(value, nested.Mapping):
            yield from nested_dict_iter(value)
        else:
            yield key, value

def get_all_values(nested_dictionary):
    global loc1
    global loc2
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            origin = key
            #print("origin: ", origin)
            loc1 = get_lat_lon(key)
            #print("***loc1: ", loc1)
            get_all_values(value)
        else:
            dest = key
            #print("dest: ", key)
            #print(key, ":", value)
            loc2 = get_lat_lon(key)
            #print("loc1: ",loc1)
            #print("loc2: ",loc2)
            #print("distance:", calculate_distance(loc1, loc2))
            nested_dictionary[key] = round(calculate_distance(loc1, loc2))
            #thisdict["year"] = 2018

def get_lat_lon(location):
    PARAMS = {'q': location, 'format': 'jsonv2'}

    # send a GET request and save response object to variable
    r = requests.get(url=URL_PATH, params=PARAMS)

    # extract data from response object in and parse json data
    data = r.json()

    # print data for investigative purposes
    # print(data)

    latitude = float(data[0]['lat'])
    longitude = float(data[0]['lon'])
    return [latitude, longitude]

def calculate_distance(orig, dest):
    #print("orig: ", orig)
    #print("dest", dest)
    # dlon = lon2 -lon1
    dlon = dest[1] - orig[1]
    # dlat = lat2 - lat1
    dlat = dest[0] - orig[0]
    # a = (sin(dlat/2))^2 + cos(lat2) * cos(lat2) * (sin(dlon/2))^2
    a = (math.sin(math.radians(dlat / 2))) ** 2 + \
        math.cos(math.radians(orig[0])) * \
        math.cos(math.radians(dest[0])) * \
        (math.sin(math.radians(dlon / 2))) ** 2
    # c = 2 * atan( sqrt(a), sqrt(1-a) )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R = 3961
    d = R * c

    return d

def construct_graph():

    graph = {'Lubbock': {'Gilroy': 1133, 'Fargo': 957, 'Zanesville': 1181},
             'Gilroy': {'Cheyenne': 940},
             'Cheyenne': {'Fargo': 562, 'Lubbock': 547},
             'Fargo': {'Zanesville': 880},
             'Tupelo': {'Lubbock': 756, 'Zanesville': 538},
             'Zanesville': {'Worcester': 555},
             'Worcester': {'Tupelo': 1068}
             }

    #walk the graph updating the weights
    get_all_values(graph)

    #print("graph: ", graph)

    return graph