import os
os.chdir(os.path.dirname(__file__))

#This program is aimed to be used especially in spotify raw data modifications


print("""


   _                  _____                  ___                 _   _  __       
  (_)                / __  \                /   |               | | (_)/ _|      
   _ ___  ___  _ __  `' / /' ___ _____   __/ /| |___ _ __   ___ | |_ _| |_ _   _ 
  | / __|/ _ \| '_ \   / /  / __/ __\ \ / / /_| / __| '_ \ / _ \| __| |  _| | | |
  | \__ \ (_) | | | |./ /__| (__\__ \\ V /\___  \__ \ |_) | (_) | |_| | | | |_| |
  | |___/\___/|_| |_|\_____/\___|___/ \_/     |_/___/ .__/ \___/ \__|_|_|  \__, |
 _/ |                                               | |                     __/ |
|__/                                                |_|                    |___/ 



""")

print("Welcome to json2csv ! Here you can turn any json file into a csv, real quick, real simple, no problems !")
#insert funny smiley later
print("What file do you want to change ?(submit the whole filename with extension): ")
ask=str(input())
file=open(ask,mode="r",encoding="utf-8")
content=file.read()
lines=content.split("},{")

#To deal with the f*cking comas in artists names or album names F*CK YOU DONALD GLOVER:

#This function was written by chatgpt, i didn't understand it so i simply wrote a simpler and more understandable one right below
""" def split_quoted_commas(text):
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
    return result """



#It's awful and doesn't serve any other purpose than causing suffering, it was my first attemp at 4am, it didn't work
""" i=0
    while i<=len(alpha):
        bracks=False
        if alpha[i]=='"':
            bracks=not bracks
        if bracks==False and alpha[i]==",":
            alpha=alpha.split(",") 
        i=i+1 """

#Now this does the exact thing i wanted but way less complicated than what chatgpt did
def spliter(alpha):
    bracks=False
    kiss=[]
    temp=""
    for i in range(len(alpha)):
        if alpha[i]=='"' and(alpha[i-1] != '\\'):
            bracks=not bracks
            temp=temp+alpha[i]
        elif alpha[i]==',' and bracks==False:
            
            kiss.append(temp)
            temp=""
        else:
            temp=temp+alpha[i]
    return(kiss)

roses=[]
for line in lines:
    alpha=line

    #print(alpha)
    #print(type(alpha))
    
    
    alpha=spliter(alpha)



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

print(f"Your file is available, its name is: '{modded}'")


