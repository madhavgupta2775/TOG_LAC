import requests

# python script to like all chapters of tower of god

start_chapter = int(input("Start Chapter: ")) - 1
end_chapter = int(input("End Chapter: ")) - 1

sample_url = input("Sample URL: ")
#break sample url into parts after encountering 95_
for i in range(len(sample_url)):
    if sample_url[i:i+3] == "95_":
        url_prefix = sample_url[:i+3]
        break

# print(url_prefix)

for i in range(len(url_prefix), len(sample_url)):
    if(sample_url[i] == "&"): #break at the first & encountered after 95_
        url_suffix = sample_url[i:]
        break

# print(url_suffix)

for chapter in range(start_chapter, end_chapter + 1):
    url = url_prefix + str(chapter) + url_suffix
    response = requests.get(url)
    if response.status_code == 200:
        print("Liked Chapter " + str(chapter))
    else:
        print("Error in Chapter " + str(chapter))
        print("Status Code: " + str(response.status_code))
        break




