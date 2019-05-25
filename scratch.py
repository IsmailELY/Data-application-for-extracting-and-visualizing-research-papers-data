import json
import urllib.request as urlr

def post_density():
    r = urlr.urlopen('https://api.osf.io/v2/providers/preprints/africarxiv/preprints/?format=json')
    dict = json.load(r)
    # store the Api in a dictionary

    d_list = list()
    d_list.insert(0, [dict["data"][0]["attributes"]["date_published"][:7], 1])
    # this list will contain a list of 2 elements (yyyy-mm,number_of_preprints)

    flag = 0

    while True:

        for j in range(1, len(dict["data"])):
            date = dict["data"][j]["attributes"]["date_published"][:7]

            if date == d_list[0][0]:
                d_list[0][1]+=1

            else:
                d_list.insert(0, [date, 1])

        if flag == 1:
            break
        else:
            r = urlr.urlopen(dict["links"]["next"])
            dict = json.load(r)
            if (dict["links"]["next"] == None):
                flag = 1

    return d_list


print(post_density())