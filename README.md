# Greetings - Git Submodules

This is a playground for git submodules, which allows a git repository to include other repositories by referencing specific commits.

## Basic git commands

```bash
# add a new submodule to an existing git repository
git submodule add <url.git> dir
git submodule init
```

```bash
# clone a git repository inclusive its submodules
git clone --recursive <url.git>
```

```bash
# pull changes from parent and submodules
git pull --recurse-submodules
```

```bash
# push changes to parent and submodules
git push --recurse-submodules=on-demand
```


## Example workflow
This simple example illustrates the steps to make changes to a submodule and publish them. Note, a submodule behaves like a usual git repository when you switch into its directory. Whenever you make changes to a submodule, remember to also update the parent repository to reference the new submodule commit.
```bash
# pull all changes from parent and submodules
git pull --recurse-submodules

# got into submodule directory
cd plugins/greetings-de

# make some changes, e.g. add a comment
...

# stage and commit changes, as you would usually do
git add .
git commit -m"made some changes"

# go back to the main repository
cd ..

# let parent reference the new changes, by adding them in a new commit
git add .
git commit -m"updated submodule"

# publish all changes
git push --recurse-submodules=on-demand
```

## Helpful links
[Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
