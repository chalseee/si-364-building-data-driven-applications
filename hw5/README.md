# SI 364 - W18 - HW5

### DEADLINE: April 4, 2018 at 11:59 pm

**You should read all of the below before beginning to ensure you set yourself up well and submit the assignment correctly.** This assignment may only be submitted *2 days* late in order to ensure you get it back in a timely fashion.

## Overview

You've been provided a bunch of scaffolding code. On top of the provided code, you'll need to add a number of things to make this application work fully, each marked by `TODO 364` inside the `app.py` file.

The things to add in this file are many fewer than your previous assignment -- this assignment is practicing a skill you've already practiced in a class exercise or two, with a new base set of code.

Each `TODO` listed for you is intended to be a small-to-medium size task. In general, you can go through the file top to bottom to address each one, but we've included suggestions in the comments about any time it makes sense to work on a TODO that comes later in the file first.

Your overall objective is to complete building an application to build TODO lists, with individual items on them. You should be able to update individual list *items'* priority values, and you should be able to delete any TODO list that is saved in the app.

Examining the code and instructions will give you further specifics.

Finally, you have an additional TODO for this assignment: practicing the git branching skill we have practiced in class. There are directions below within the **Instructions** section of this README explaining specifically what to do.

Here is a series of screenshots displaying what you should be able to do in the completed application:

* [Home page](https://www.dropbox.com/s/dum22xa4qf3j2iy/Screenshot%202018-03-26%2001.23.46.png?dl=0)
* [An example of entering a new list](https://www.dropbox.com/s/84fqx5e2k455dj2/Screenshot%202018-03-26%2001.24.20.png?dl=0)
* [Viewing the All ToDo Lists page](https://www.dropbox.com/s/l9cmyg40gs5ltlv/Screenshot%202018-03-26%2001.24.27.png?dl=0)
* [View of one particular list](https://www.dropbox.com/s/72ea46h19fdh1xk/Screenshot%202018-03-26%2001.24.33.png?dl=0)
* [Example of the view while updating a ToDoList item's priority](https://www.dropbox.com/s/sjy4m3a96iuyxaf/Screenshot%202018-03-26%2001.24.38.png?dl=0)
* [Example of what you should see after successfully clicking Update on the above screen](https://www.dropbox.com/s/fzzxt8nhfexe3zs/Screenshot%202018-03-26%2001.24.45.png?dl=0)
* [Example of what you should see after successfully deleting a TODO list](https://www.dropbox.com/s/zjc0sn8bhfp85q6/Screenshot%202018-03-26%2001.26.34.png?dl=0)

Note also that the following is the format for entering multiple ToDoList items when creating a list, since it is harder to see in the screenshot:

        Description of item, priorityinteger
        Second item description, priorityinteger

e.g.

        Complete 364 HW5, 2
        Study for capstone exam, 3
        Go to soccer practice, 1

You'll notice that the way this app is built is not exactly an ideal "TODO list" application, of which you can find very many on the internet. There are a lot of unusual things about how the data is managed and how the views show up, in the way you are directed to do this.

That is because the goal of completing these tasks is to practice these important skills -- not to complete a thorough application, this time. If you want to do more work on this that is more advanced *on your separate branch*, that is completely fine. But the requirements of the app that you should turn in are as stated. They are relatively simple *compared to* a lot of the complex applications you probably engage with and use in real life.

(Considering the tradeoffs you're looking at if you wanted to build this out into something more complex may be a useful exercise, though! But that's not something you must do this week.)

You will be:

* Completing a CRUD (Create Read Update Delete) application, specifically focusing on the Update and Delete actions
* Continuing to plan around database relationships, forms, view functions, helper functions, and integrating back-end code with templates
* Practicing a skill with git, useful for collaborating and dealing with others' Flask and other types of web applications


## Specific Instructions

* First, check out the **to submit** instructions so you know how to begin work on this!
* Check out `app.py`, scan through it, read the comments, and complete the `TODO 364` todo items one by one.
* Try to understand all the code. What does this application do? What is missing from it? What is already there? What does this code do? Doing this will be enormously helpful to finishing this assignment more easily.
* Identify anything in the `TODO 364` comments you are confused about so you can ask questions ASAP.
* Consider what example(s) are similar to the tasks at hand -- if you look at the right examples and make analogies to them, this will be much easier to do!
* Make sure to debug along the way!
* Edit the files to ensure you have completed each `TODO 364` item. Each is worth points, and **the total of all `TODO 364` items completed are worth 850 points.**
* Ensure you have everything committed properly and pushed to your new GitHub repo to submit the link properly to Canvas.
* Make some additional change(s) to your application -- ANYTHING that is a change to at least one file.
* Create and check-out a new branch called `addl_feature` and commit the additional changes you have made to this `addl_feature` branch (these changes can be ANYTHING, working or not, but they must be changes to at least one file).
* Push the `addl_feature` branch to your GitHub repository, so at the end, your GitHub repository representing this project has two branches: `master` and `addl_feature` (**completing this branching and pushing step is worth 150 points from this HW**; the rest of the points come from the `TODO 364`s)

## To submit (read ALL the below before beginning)

**Don't fork this one.** Download the link as a .zip file. Unzip the file so you have all the provided, included files in a directory on your computer.

Just as you did for the midterm assignment, create a GitHub repository for HW5 on your account called `HW5_364`. (It must be called this to be graded.)

You may create a private repository if you want, and if you do that, you **must also add all three of us instructors as collaborators to your repository. Otherwise we will not be able to see and grade it**.

If you have not already, **[here](https://help.github.com/articles/applying-for-a-student-developer-pack/)** is how to get a GitHub student developer pack so you can have unlimited private repositories. *If you have already done this, you do not need to do it again.* (The student developer pack also includes access to a bunch of other useful/fun software tools! It is free for all students; follow the instructions at that link.)

Push *all* of the code files, including any additional files you add and all included files, to this GitHub repository.

Follow instructions above to ensure you have completed the branching requirement correctly.

[Check out the midterm instructions](https://github.com/SI364-Winter2018/Midterm-Instructions) for a reminder of how to add all 3 of us instructors (Jackie, Mauli, Sonakshi) as collaborators to the repository you submit.

Submit the link to your GitHub repository on the Canvas assignment for HW5. It should take the form of: `https://github.com/YOURGITHUBUSERNAME/HW5_364`
