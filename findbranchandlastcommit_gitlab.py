from git import Repo
import git
from time import strftime, localtime
import datetime
predefinedRepos=['https://git.example.com/repo1','https://git.example.com/repo2','https://git.example.com/repo3']
#create a file to write output
f = open("outputFile.txt", "w")
for repoName in predefinedRepos:
    print (repoName[repoName.rindex('/')+1:len(repoName)])
    folderNameLocal=repoName[repoName.rindex('/')+1:len(repoName)]
    try:
      #below command will refer the repo which is present local
        repo = git.Repo("C:\\"+folderNameLocal)
        #below command will all remote branches
        remote_refs = repo.remote().refs
    except:
      #below command will download the repo to local
        Repo.clone_from(repoName, "C:\\"+folderNameLocal,branch='master')
        repo = git.Repo(folderNameLocal)
        remote_refs = repo.remote().refs
    x,y=['','']
    for refs in remote_refs:
      #below if condition will check for given branch present in remote ref
        if (refs.name.lower()).startswith('origin/abc'):
                print(refs.name.lower())
            #datetime.datetime.fromtimestamp(refs.commit.committed_date) will get last commit date in remote branch
                x=x+"::"+refs.name;			y=y+"::"+str(datetime.datetime.fromtimestamp(refs.commit.committed_date))
    if x:
        f.write((repoName+"--"+x+"--"+y+"\n").replace("--::","--"))    
        
f.close()            
