##Intro

* A huge part of any good search engine is not to simply return the pages that best match the input query.
* Instead, it tries to answer the underlying question.
* Many search engines use complex algorithms to determine what result they should return.
* Indexing is used to optimize speed and performance in finding relevant documents for a search query.
* Search engine indexing collects, parses, and stores data to facilitate fast and accurate information retrieval. 
* Indexing takes place within the search engine's database, after the crawler stores the data to the database.
* The search engine index provides the result for search queries, and pages that are stored within the search engine index that appear on the search engine results page.
* Index design incorporates interdisciplinary concepts from linguistics, cognitive psychology, mathematics, informatics, and computer science.



##Implementation

Crawlers gather information and pagers which is used to create an index, where things can be looked up easily. When you search, at the most basic level, our algorithms look up your search terms in the index to find the appropriate pages. 

* Indexing uses ranking algorithms to determine the best results. 
* When you search for “cats” you don’t want a page with the word “cats” on it hundreds of times. You probably want pictures, videos or a some hilarious GIFS. 
* Indexing systems note many different aspects of pages, such as when they were published, whether they contain pictures and videos, and much more. 
* It is more than just keyword matching, which would lead to much less desirable results.


##Components

There are many different parts to a search engine index. The design factors of a search engine index design or outline the architecture of the index and decide how the index actually works. Major factors include:

* Merge factors - how the information enters the index, deciding whether the data is new data or data that is being updated.
* Index size - the amount of computer space necessary to support the index.
* Storage techniques - how the information should be stored. Larger files are compressed while smaller files are simply filtered.
* Fault tolerance refers to the issue of how important it is for the search engine index to be reliable.
* Lookup speed - how quickly a word can be found when the data is searched in the inverted index.
* Index data structure - how a search engine performs indexing and stores indexes. We will cover more on this topic in the following sections.


##Index data structure
* When a search engine index is being built, there are also many different types of data structures to choose from. 
* Choosing a particular data structure for a search engine index is like deciding on a particular form for a web page, and depends on the factors that the search engine will serve. 

Examples:
* Suffix tree – Supports linear time lookup and is structured like a Tree.
* Tree – An ordered tree data structure that stores an associative array where the keys are strings.
* Inverted index – Stores a list of occurrences in the form of a hash table or a binary tree.
* Citation index – Stores citations or hyperlinks between certain documents to support citation analysis.
* Ngram index – Stores sequences of length of data, which supports other types of retrieval. Sometimes supports text mini too.


