import os
import time
import shutil
 
def RemoveFiles():

    days = 30 
    DeletedFolders = 0
    seconds = time.time() - (days * 24 * 60 * 60)

    path = input("Enter Folder name : ")

    if os.path.exists(path) :

     for a, b, c in os.walk(path):

      if seconds >= FolderAge(a) :

          removeFolder(a)

          DeletedFolders +=1

          break
      else :
          for folder in b:
              folderPath = os.path.join(a,b)
              if seconds >= FolderAge(folderPath) :

                removeFolder(folderPath)

                DeletedFolders +=1

                break
        
          for file in c :
           filePath = os.path.join(a,c)
           if seconds >= FolderAge(filePath) :

                removeFolder(filePath)

                DeletedFolders +=1

                break
     else :
            if seconds >= FolderAge(path) :

                removeFolder(path)

                DeletedFolders +=1
    else :
             print(f'"{path}" is not found')

             DeletedFolders += 1 

             print(f"Total folders deleted: {DeletedFolders}")

             print(f"Total files deleted: {DeletedFolders}")
	
           

		
				



		
       


def FolderAge(path):

	ctime = os.stat(path).st_ctime

	return ctime

def removeFolder(path):

 if not shutil.rmtree(path):
      print(f"{path} is removed successfully")
 else: 
     print(f"Unable to delete the "+path)
 
RemoveFiles()
 
