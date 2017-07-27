# import requests

# r = requests.get('http://chat.parachat.com/roam/login.html?room=MasalaChat&width=450&height=400')
# print r.content

def median(data):
    frequency_distribution = {i:0 for i in data}
    print frequency_distribution
    for x in data:
        frequency_distribution[x] =+ 1
    cumulative_sum = 0
    for i in data:
        cumulative_sum += frequency_distribution[i]
        if (cumulative_sum > int(len(data)*0.5)):
            return i

data = [5,3,9,1,4,6]
print sorted(data)
print median(sorted(data))