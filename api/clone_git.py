import os
from urlparse import urlparse, urlsplit

# def clone():
# try:
#     with open('settings.yml', 'r') as outfile:
#         oldset = yaml.load(outfile)
#         git_repo = oldset['GitRepo']
#         # path = os.path.join(os.environ['TEST_PATH'], os.path.splitext(os.path.basename(urlparse.urlsplit(git_repo).path))[0], "tests")
#         # test_folder = os.listdir(path)

# except:
#     print "No settings present!"

username = "webdelit-a0489-devel"
password = "J3YUh0.NrwDd"
path = os.environ['TEST_PATH']

clone = "git clone https://%s:%s@gitlab.forge.orange-labs.fr/lab-orange/robotests.git %s"%(username,password,path)


git_repo = urlparse("https://gitlab.forge.orange-labs.fr/lab-orange/robotests.git")

print git_repo.netloc+git_repo.path

# print urlsplit(git_repo)

# print clone
# clone = "git clone https://username:password@github.com/username/repository.git"