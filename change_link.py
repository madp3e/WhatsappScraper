with open("convert_link.txt", "r") as file:
    links = file.readlines()

for link in links:
    print('"{}",'.format(link.strip()))