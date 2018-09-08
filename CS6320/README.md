Jiadao's NLP project, spring 2018.
===========================================

Given a movie review, finds the sentence which best summmarizes the review. Based on research by Zhuang et al., available [here](http://research.microsoft.com/en-us/um/people/leizhang/Paper/cikm06_movie.pdf).



Examples
-------
The [NYTimes review for "Pain and Gain"](http://movies.nytimes.com/2013/04/26/movies/michael-bays-pain-gain-with-mark-wahlberg.html?_r=0) is summarized by the sentence:

> It all leaves you pondering whether you have just seen a monumentally stupid movie or a brilliant movie about the nature and consequences of stupidity

And, the [Roger Ebert's review of the estimable Mean Girls](http://www.rogerebert.com/reviews/mean-girls-2004) is summarized by
> Mean Girls dissects high school society with a lot of observant detail which seems surprisingly well-informed

To Use
------
After stting up your Stanford Parser, use followin commands to go:

To summarize reviews within NLTK movie_reviews corpus:

    $ python summarizer.py

To summarize movie review(s) not included in the NLTK:

    $ python summarizer.py filename1.txt filename2.txt ... etc.

