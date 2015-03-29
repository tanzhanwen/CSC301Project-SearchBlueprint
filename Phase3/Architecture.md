## Architecture 
    
As with any project, ours has the two main components, the front end and the back end. The following describe what they are created using, and how they interact with each other.

#### Front End

The front end is responsible for the visuals of the whole system, which is a major part of our project and something we focused on. Right from the beginning we want to make sure the website is visually engaging and interactive, to involve the user in the learning process and –to give the users a greater experience.

The front end was developed using the usual languages: HTML5, CSS3 and JavaScript. For the design we used ‘FLAT UI’, a free bootstrap framework and theme.

The interactive portion was done using JavaScript/JQuery and HTML5. Ajax calls are made to the backend to get data for certain portions of the tutorial. One example would be the where the sample crawler results show in one of the tutorials.


#### Back End 

For back end, we used Python and the Django framework. The reason why we chose Django was because it was very easy to integrate other frameworks such as haystack for search and our own python based web crawler.

 Some of the major components created for this web application are:
 
*	Our Own Web Crawler - our own basic web crawler that is able to crawl through databases and collect data. The simple web crawler is utilized in the "Crawler" section of our tutorial so users can examine the code and learn its parts and their functionality. One of the controllers runs the script and returns the data in an Ajax call.
*	Haystack -  a framework that provides a modular searching feature for Django. It allows for multiple search engines to be integrated (in our web app, we used the Whoosh search engine and Elastic search engine) without changing anything in the code. This is what we use in the compare web page.
*	Whoosh search engine - a simple python based search engine
*	Elasticsearch - a java based search engine.

#### Important architectural design decisions:

There were a couple of major changes to the architectural design of the project.

Initially we had plans of adding registration that allowed users to save the progress of the tutorial and look at their scores in the quizzes, which we decided not to implement as a part of our final product even though it could be easily made by storing cookies. This also changed the way our front end tutorial app connected to the back end. Since we aren’t storing the results of the mini quizzes, the structure of the tutorial changed from what we had initially envisioned. We like the new way better and think it was a good decision to go in this direction.

Another major decision was to create our own crawler to use with Django as python scripts can be easily run in Django.
