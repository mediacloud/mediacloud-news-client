Mediacloud News Archive Client
===================================

🚧 _Archived_ 🚧

The functionality of this package has been folded entierly into mediacloud/mc-providers. As development here will stop, the package is archived

A simple client library to access the Wayback Machine news archive search.


Installation
------------

NB: TBD
`pip install mediacloud-news-client`


Basic Usage
-----------

Counting matching stories:

```python
from mcnews.searchapi import SearchApiClient
import datetime as dt

api = SearchApiClient("mediacloud_search_text_*")
api.count("coronavirus", dt.datetime(2023, 11, 1), dt.datetime(2023, 12, 1))
```

Paging over all matching results:

```python
from mcnews.searchapi import SearchApiClient
import datetime as dt

api = SearchApiClient("mediacloud_search_text_*")
for page in api.all_articles("coronavirus", dt.datetime(2023, 11, 1), dt.datetime(2023, 12, 1)):
    do_something(page)
```


Dev Installation
----------------

Install the dependencies for dev: `pip install -e .[dev]`



Distribution
------------

1. Run `pytest` to make sure all the test pass
2. Update the version number in `mcnews/__init__.py`
3. Make a brief note in the version history section below about the changes
4. Commit the changes
5. Tag the commit with a semantic version number - 'v*.*.*'
6. Push to repo to GitHub
7. Run `python setup.py sdist` to create an installation package
8. Run `twine upload --repository-url https://test.pypi.org/legacy/ dist/*` to upload it to PyPI's test platform
9. Run `twine upload dist/*` to upload it to PyPI


Version History
---------------

* __v2.0.0__ - Fresh start as mediacloud-news-client
* __v1.2.1__ - fix paging bug triggered by no results
* __v1.2.0__ - add support for new `expanded` results, and more integration testing
* __v1.1.0__ - add new `paged_articles` method to allow paging over all results
* __v1.0.3__ - add 30 sec timeout, remove extra params mcproviders library might be adding
* __v1.0.2__ - fix to article endpoint
* __v1.0.1__ - automatically escape '/' in query strings, test case for `url` field search
* __v1.0.0__ - update to public API endpoint
* __v0.1.5__ - simpler return for top terms
* __v0.1.4__ - better error handling
* __v0.1.3__ - allow overriding base api URL 
* __v0.1.2__ - fix `article` endpoint, test case for fetching content (`snippet`) via `article_url` property 
* __v0.1.1__ - more consistent method names
* __v0.1.0__ - initial test-only release
