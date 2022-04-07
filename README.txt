https://github.com/clementgohchangming/hello_git/blob/master/readme.md

Installing Git
Source: https://www.atlassian.com/git/tutorials/install-git
git --version
This lets you know what is the current version of git you have.



Hello Git
// change directory to your desktop
cd ~/desktop

// make a directory
mkdir hello_git

// change directory to hello_git
cd hello_git
To start source controlling this repository with git, lets do
git init



Introducing Branches
Branches can be thought of as copies of the repository, each with their own source control history.
Typically in a production repository, we will have at least 1 master branch / clean copy of the repository that is clean.
That is usually called master / develop
When we wish to make changes to the repository, we will typically make a copy of that clean branch, called a feature branch.
alternatively, you can create and change our branch to that new branch in one step with
git checkout -b master



Introducing commits
Commits are checkpoints / versions which we create for changes to our branch or repositories.
For us to make a commit, we will need two things
A staged change to commit (e.g file changes, file creation, file deletion, moving a file from one place to another)
A commit message to let everyone know what this commit changes



Staging a change to commit
Git knows if a there is a change to be commited by checking its "staging area"
To check what files are staged, and what files are not staged, we can do
git status

this lists out all local changes we have made, and what are currently staged
to add a file to the staging area so that git knows that is ready for committing
we can do
git add path_to_file
# file has to be within hello_git directory/folder
# simply use git add two_sum.py

now that we have added that file, if we do git status again, we will now see that file in the staging area
if we wish to remove a file from staging, we can do
git restore --staged path_to_file
notice that git is nice to show us the command for unstaging a file when we do git status too!
if you wish to unstage all files in your staging area instead of unstaging each of them one by one, you can also do
git reset HEAD
this resets the repository to the current version of your repository



Making a commit
Once we have staged all the files we want to commit / version control, we can make a commit by doing
git commit -m "your message for the commit"
one example of a commit message can be
git commit -m "feat(add-file): add readme.md"
notice that we typically want commits to be descriptive of what the commit does :) we as engineers typically do our best to label and make our changes as readable as possible, so people dont talk shit about us on slack.



Checking our commit history
Congrats on making your first commit!
Now that we have made the commit, we might want to see what is the history of our repository now.
We can easily do that with
git log
this lets us know the history of the branch we are in.



Pushing changes to a remote repository
Now that you have made your first commit, you have successfully made a new version of your repository! locally though!
What if we want to share the repository with someone else?
We can do that by telling git that we want target our local repository to a remote repository, so that we can make copies of our changes there as well
To check which remote directory our current repository is targetting, we can do
-v is a verbose flag
git remote -v
We have nothing here :') lets make this repository target a remote repository!
We can do that by first creating a remote repository on github / gitlab, and copying the link to the remote repository
Then, we can do
git remote add <your_remote_name> link_to_your_remote_repository
Once done, we can push our changes to the remote repository with
git push <your_remote_name> <your_branch_name>
we typically call our remote repository origin
so if we wanted to push our local master branch to the remote's master branch, we would do
git push origin master
If you wish to remote a remote
git remote remove <name_of_remote>
Congratulations! You have pushed your first change to github!




***********
C:\Users\user\Desktop\hello_git>git push origin master
To https://github.com/zhengyanglim057/leetcode_solution.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/zhengyanglim057/leetcode_solution.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

solve it using 
C:\Users\user\Desktop\hello_git>git push origin master --force