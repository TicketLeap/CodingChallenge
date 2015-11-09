#The Ticketleap Coding Challenge

**In the Philadelphia area,** many people commute to work using the SEPTA Regional Rail system.  You have been tasked with making a very simple application that allows riders to see what trains they can catch, and whether they’re on time.  To do this, you will take advantage of SEPTA’s train status API:

http://www3.septa.org/hackathon/NextToArrive/?req1=Swarthmore&req2=30th+Street+Station

(The URL structure for the request is pretty straightforward - the example here is for trains from Swarthmore to 30th Street Station)

You’ve been provided a simple one-page Django that renders the shell of the page.  Your job is to add a table to the page which displays the trains returned by the API call, their scheduled departure time, arrival time, and whether they’re running late or on time.   

This data should be current as of each page load, but unless you’ve got some time leftover don’t worry about trying to make the updates live.  There are many ways to accomplish this task on both the server and the client side, so go with what you’re familiar with.  

**The sample code we've given you is in Python/Django, but don't let that limit you!** If you can get a Node.js stack up and running in no time flat, feel free to chuck what we've given you.  Want to use the part of the app that renders the main page and do the rest in JavaScript?  That's fine too!  At the end of the day this is about seeing how you solve open-ended problems, so even if you can't get it 100% of the way there we still want to see what you've done. 

Feel free to pull in any libraries or extra resources you feel are necessary, but be ready to defend why.  Also, definitely go ahead and use built-in functionality like data structures and sorting algorithms rather than implementing your own, but be sure to have an idea of what’s going on under the hood.  Using StackOverflow/Googling around is fine, but give attribution in the form of a comment if a section of code is from or inspired by something you have not written. 

The easiest way to get the challenge is to clone the git repo (if you need help getting git up and running on your system, check out [this](http://rogerdudler.github.io/git-guide/) slightly profane tutorial):

```git clone https://github.com/TicketLeap/CodingChallenge.git```

Once you get the app unpacked and ready to go, start the server by running the setup script:

```./setup.sh ```

(It will prompt you for a password).  This installs the tools pip (python package installer) and a virtual environment tool on your system.  It runs a variety of commands to configure Django from scratch, but feel free to look at it before running to get a better sense of what it does. 

**If you do run into trouble during installation, let us know!**  The setup shouldn't be the part you're spending your time on.  If it takes more than a few minutes to get set up feel free to reach out to us and we'll see what we can do to get you un-stuck. 

Navigating a browser to localhost:8000 will show you how the site looks to get started, and has a helpful hint or two.  If you run into problems with the setup, let us know.  

Once you are done, please email us a screenshot of your solution and a link to a private repository (bitbucket is an option if you don't have a paid Github acct) or some other private code-sharing solution. 
