file = open("map.txt")
events = open("events.txt", "w")
events.write("event \"all knowledge\"\n\tdate 17 11 3013\n")

text = ""

for line in file:

    if line.strip().split(" ")[0] == "pos":
        a = float(line.strip().split(" ")[1])
        b = float(line.strip().split(" ")[2])

        line = f"\tpos {-a} {-b}\n"

    if line.strip().split(" ")[0] == "system":
        a = line.strip()[7:]
        events.write(f"\tvisit {a}\n")

    if line.strip().split(" ")[0] == "planet":
        break

    if line.strip().split(" ")[0] == "government":
        a = line.strip()[11:]
        if a == "Republic":a = "Syndicate"
        elif a == "Syndicate":a = "Republic"

        line = f"\tgovernment {a}\n"
    
    text = text + line

out = open("newmap.txt", "w")
out.write(text)

out.close()
file.close()
events.close()
