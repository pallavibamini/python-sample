#automatic file backup script
# import os
# import shutil
# import datetime
# source="C:/Users/DELL/Desktop/python sample"
# backup=f"C:/Users/DELL/Desktop/project1/New folder/backup_{datetime.date.today()}"
# if not os.path.exists(backup):
#     os.makedirs(backup)
# for file in os.listdir(source):
#     if file.lower().endswith((".jpg",".jpeg",".png",".txt",".csv")):
#         sourcepath=os.path.join(source,file)
#         backuppath=os.path.join(backup,file)
#         shutil.copy(sourcepath,backuppath)
# print("Backup completed")

import os
import shutil
import datetime

source="C:/Users/DELL/Desktop/python sample"
backup=f"C:/Users/DELL/Desktop/project1/New folder/backup_{datetime.date.today()}"
if not os.path.exists(backup):
    os.makedirs(backup)
for file in os.listdir(source):
    if file.lower().endswith((".jpg",".jpeg",".png",".txt",".csv")):
        sp=os.path.join(source,file)
        bp=os.path.join(backup,file)        
        shutil.copy(sp,bp)
print("Backup completed")   

