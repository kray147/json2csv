import os
os.chdir(os.path.dirname(__file__))

print("Welcome to json2csv ! Here you can turn any json file into a csv, real quick, real simple, no problems !")
#insert funny smiley later
print("What file do you want to convert ?(submit the whole filename with extension): ")
ask=str(input())
file=open("Streaming_History_Audio_2023_4.json",mode="r",encoding="utf-8")
content=file.read()
lines=content.split("},{")

#To deal with the f*cking comas in artists names or album names F*CK YOU DONALD GLOVER:

def split_quoted_commas(text):
    result = []  # List to hold the final split segments
    current = []  # List to accumulate characters for the current segment
    in_quotes = False  # Flag to indicate whether we are inside quotes
    escaped = False  # Flag to indicate whether the previous character was an escape \

    i = 0
    while i < len(alpha):
        char = alpha[i]

        if char == '\\':  # Handle escaped characters
            if escaped:
                current.append(char)  # Keep escaped backslashes
            escaped = not escaped
        elif char == '"':
            if not escaped:
                in_quotes = not in_quotes
            else:
                current.append(char)  # Keep escaped quotes inside quotes
            escaped = False
        elif char == ',' and not in_quotes:
            result.append(''.join(current).strip())
            current = []
        else:
            current.append(char)

        i += 1

    result.append(''.join(current).strip())
    return result



#It's awful and doesn't serve any other purpose than causing suffering, I asked chatgpt for the real function used cuz i couldn't figure it out 
""" i=0
    while i<=len(alpha):
        bracks=False
        if alpha[i]=='"':
            bracks=not bracks
        if bracks==False and alpha[i]==",":
            alpha=alpha.split(",") 
        i=i+1 """


roses=[]
for line in lines:
    alpha=line
    #alpha=alpha.split(',')
    
    
    alpha=split_quoted_commas(alpha)


    roses.append(alpha)
    
    

file.close()




for i in range(len(roses)):
    for j in range(len(roses[i])):
        #print(f"i={i},j={j}")
        roses[i][j]=roses[i][j].split(":",1)
        for k in range(len(roses[i][j])):
             roses[i][j][k]=roses[i][j][k].strip("[").strip("{").strip("]").strip("}").strip('"')





bigrow=[[]for i in range(0,len(roses)+1)]

nbr_rows=len(roses[0])

for i in range(nbr_rows):
    bigrow[0].append(roses[0][i][0])




for n in range(0,len(roses)):
    for j in range(0,nbr_rows):

        bigrow[n+1].append(roses[n][j][1])

modded=ask.strip(".json")+".csv"

writer=open(modded,"w+",encoding="utf-8")
for i in range(len(bigrow)):
    for j in range(len(bigrow[i])):
        
        writer.write(bigrow[i][j]+",")
    writer.write("\n")
writer.close()

print(f"Your file is available, its name is '{modded}'")


