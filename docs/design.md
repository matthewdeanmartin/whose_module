This library is a database library, in the sense thta the interesting bits
are the data and the data chanes over time.

Similar things:

Small
----
- country names and codes
- language names and codes

Small datasets can be put in a format, say json, sqlite, and a little bit of
python so the user doesn't have to use a json or sqlite api and thats it.

Another pattern is the "instant web API" that datasette does.

Also, the data doesn't change often, so publishing an update every few months or
years is okay. If data has to be updated hourly, that would be an abuse
of a public package repository.

Medium
------
- US zip code databases
- [Baby Names](https://github.com/mileswwatkins/ssa_baby_names/blob/master/ssa_baby_names.py)
- Names? https://pypi.org/project/names-dataset/
- Machine Learning datasets
    - ??? 

The datasize is a bit too large for a pip installable library, but small
enough that caching the whole thing might be a good idea. Or it changes
fast, like the top 100 popular books.

Large
-----
- Every US patent

The datasize is certainly too large for a library. This needs to be a remote
API and you'd want to use an API client that maybe caches just enough
