
## Virtual Environment

- Pycharm always create a new Virtual environment for each new project but you can choose to reuse old already created one.
- Customize after project creation, Settings... -> Project:[NAME] -> Python Interpreter -> Show All...

## Clone GitHub Project in Pycharm

- VCS -> Get from Version Control -> GitHub -> Select Repository -> Clone

> Before you do this you should add your GitHub Account in Pycharm from, Setting... -> Version Control -> GitHub -> Add -> Login via GitHub...
> Also after you clone repository, you will have to Add Interpretor (create Virtual Environment) and fix dependency by Install requirements (from requirement.txt) 

## Pull remore brnaches

- After cloning if you want to pull remote branch, Git -> Branches -> Remote Branches -> Select Branch -> Checkout

## Reseting to Older version

- Open Git Window, browse Commit history -> right click on desired commit -> Reset Current Branch Here... -> Hard

## Generate project dependency

- Tool -> Sync Project Requirements...

> This will create requirement.txt


## Generate project setup

- Tool -> Create setup.py

> Fill the form

