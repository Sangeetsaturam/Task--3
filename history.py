# Access the value of key ‘history’ from the below
# sampleDict = {
# "class":{
# "student":{
# "name":"Mike",
# "marks":{
# "physics":70,
# "history":80
# }
# }
# }
# }
sampleDict = {
       "class":{
          "student":{
             "name":"Mike",
             "marks":{
                "physics":70,
                "history":80
             }
          }
       }
    }

print("output:",sampleDict['class']['student']['marks']['history'])

#output: 80