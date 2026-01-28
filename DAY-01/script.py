# import sys
# var=sys.argv[1]
# print(f"Hello,{var}!")

# import sys
# print("prog name:",sys.argv[0])
# for i in range(1,len(sys.argv)):
#     print(f"arg{i}:", sys.argv[i])

# import shutil
# import datetime

# source="c:/Users/DELL/Pictures/Screenshots/Screenshot (2).png"
# backup=f"C:/Users/DELL/Desktop/project1/New folder/data_backup_{datetime.date.today()}.png"
# shutil.copy(source,backup)
# print(f"backup of {source} created at {backup}")


# import os
# import shutil
# import datetime
# source="C:/Users/DELL/Desktop/python sample"
# backup=f"C:/Users/DELL/Desktop/project1/New folder"
# for file in os.listdir(source):
#     if file.lower().endswith((".jpg",".jpeg")):
#         sourcepath=os.path.join(source,file)
#         backuppath=os.path.join(backup,file)
#         shutil.copy(sourcepath,backuppath)
# print("completed")
