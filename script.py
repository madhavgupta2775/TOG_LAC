import requests

# python script to like all chapters of tower of god

start_chapter = int(input("Start Chapter: "))
end_chapter = int(input("End Chapter: "))
input_start = start_chapter

if(start_chapter > 220):
    start_chapter += 1
if(end_chapter > 220):
    end_chapter += 1

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

i = 0

for chapter in range(start_chapter, end_chapter + 1):
    if(chapter == 221): # url with 95_221 does not exist, ch 221 has 95_222
        continue

    url = url_prefix + str(chapter) + url_suffix
    response = requests.get(url)
    if response.status_code == 200:
        print("Liked Chapter " + str(input_start + i))
    else:
        print("Error in Chapter " + str(input_start + i))
        print("Status Code: " + str(response.status_code))
        break
    i += 1




