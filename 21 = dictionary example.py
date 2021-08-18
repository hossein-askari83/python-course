# we whant create python cortse dictionary 

course = {
    "title" : "python",
    "teacher" : "mohmamad ordookhani",
    "time" :8.5 , 
    "videoCount" :30, 
    "tags" : ["python course" , "free python course" , "online course"],
    "parts" : [
    {
        "title" : "part1",
        "time" : 5
    },
    {
        "title" : "part2",
        "time" : 7
    },
    {
        "title" : "part3",
        "time" : 10
    }
    ],
    "realatedCourses" : [
    {
    "title" : "java",
    "teacher" : "mohammad ghari",
    "time" :20 , 
    "videoCount" :42, 
    "tags" : ["java course" , "free java course" , "online course"]
    },
    {
    "title" : "c#",
    "teacher" : "iman madaeny",
    "time" : 10 , 
    "videoCount" : 22, 
    "tags" : ["c# course" , "free c# course" , "online course"]
    }

    ]
}

print(course["realatedCourses"]) # ==>  this is crowded we use for : 

for item in course["realatedCourses"]  : 
    print(item)

# now we whant the total time of parts : 

print("----------------------")

total = 0 
for parts in course["parts"] : 
    total += parts["time"]


print(total)