####
# gitMirror.py
# Version: 0.1
# Python 3.7
#
# This script mirror git repositories from one server to a mirror server
# Requires a file "trackedRepositories.txt" with URL's to the git
# repositories that need to be mirrored
# The URL must be in the form https://provider/maintainer/repository
####import os
import datetimehomeDir = "/var/tmp/github/"def findBoundary(url, n):
    # split string at each '/' for max of n times
    splits = url.split('/', n)
    # confirm number of splits
    if len(splits) <= n:
        return -1
    # Substract the length of the substring after the nth '/' char
    # from the url to get the index
    return len(url) - len(splits[-1]) - 1def extractArgs(url):
        # Extract the repo maintainer's name
    maintainerStart = findBoundary(url, 3)+1
    if maintainerStart <= 0:
        raise ValueError('Invalid URL', url)
    maintainerEnd = findBoundary(url, 4)
    if maintainerEnd <= 0:
        raise ValueError('Invalid URL', url)
    maintainer = url[maintainerStart:maintainerEnd]
    repo = url[maintainerEnd+1:len(url)]  # repository name
    return [maintainer, repo]try:
    fin = open(homeDir + 'trackedRepositories.txt', 'r')
except:
    print("Could not open the tracked repositories file")
    exit()for line in fin:
    # Extract the maintainer and repo.
    nline = line.strip()
    # Get maintainer and repo names
    nArgs = extractArgs(nline)
    maintainer = nArgs[0]
    # Remove any trailing backslashes.
    repo = nArgs[1].strip('/')
    repoPath = (homeDir+repo+".git")
    # Check if the repository is already cloned locally
    if os.path.exists(repoPath):
        os.chdir(repoPath)
        cmd = "git pull"
        print(os.popen(cmd).read())
        cmd = "git push mirror"
        print(os.popen(cmd).read())
    else:
        os.chdir(homeDir)
        cmd = "git clone --mirror " + nline
        print(os.popen(cmd).read())
        mirrorRepoName = "git@mirror:mirror/" + maintainer +\
            "-" + repo + ".git"
        os.chdir(repoPath)
        cmd = "git remote add mirror " + \
            mirrorRepoName.lower()
        print(os.popen(cmd).read())
        cmd = "git push mirror --mirror"
        print(os.popen(cmd).read())
