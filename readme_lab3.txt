##### Part 1: preparing the code
1.  goto your github account (if you dont have one; create one, it is free)
2.  click on ``repositories``
3.  click on ``New``
4.  give a name in repository name field (remember this as this is needed in part 2)
5.  make sure to make this repository as ``public``
6.  leave everything else as is and click on ``Create repository``
7.  on the next page (which just appeared) check for ``uploading an existing file`` and click on the same.
8.  this will give you a place to drag and drop your files.
9.  drag and drop all the files inside demo_slr (except envSLR, and __pycache__) folder here.
10. once the upload progress is complete, give a commit message and click on ``Commit changes`` button.
11. make sure all the selected files are available in the list.
12. if not click on ``Add file`` and upload the files that are missing.


##### Part 2: deploying the code
1. goto your heroku account page (if you dont have one; create one, it is free)
2. click on ``menu (3x3 matrix dots)`` and on ``dashboard``
3. click on ``New`` ->  ``create new app``
4. give a name and select your prefered country for deployment.
5. click on ``Create App``
6. under ``Deployment Method`` choose ``connect to GitHub``.
7. once you select ``connect to github`` there will be section ``connect to github`` appeared below.
8. follow steps to link your github if not already linked.
9. give the repository name (which you used while creating github repo) in repo-name column
    and click on ``Search``.
10. if the search was successfull, the repository should appear below and a ``connect`` button should
    appear to the right.
11. click on the ``connect`` button.
12. leave everything else as is and scroll all the way to the bottom.
13. click on the button ``Deploy Branch``.
14. on click the log should appear in the bottom and on success; a message stating the deployment status
    appears along with a ``View`` button.
15. click on the ``View`` button.
16. it may take upto 2 mins for the application to be deployed completely. but if you dont
    see ``{"message":"Hello World"}`` after 2 mins (after refreshing); there might be some error
    in your code; fix it and redeploy.
17. add ``/docs`` at the end of the url to access fast api.
18. now test you application here as you tested in lab2.
