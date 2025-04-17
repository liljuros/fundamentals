with open("ips.txt") as file:
    every = file.readlines()
    stripped_text = [ips.strip() for ips in every]
    joined_text = ",".join(ips for ips in stripped_text)

with open("output_v2.txt", 'w') as file2:
    file2.write(joined_text)





