# TVDB

[![Requirements Status](https://requires.io/github/kvikshaug/tvdb/requirements.svg?branch=master)](https://requires.io/github/kvikshaug/tvdb/requirements/?branch=master)

A lightweight Django + Bootstrap app for keeping track of the TV series you're interested in.

## Development

### Start development server

```
docker-compose up
```

### Compile statics

```
docker-compose run --rm builder sass --scss --update scss:css
docker-compose run --rm app ./manage.py collectstatic --noinput
```

### QA

```
docker-compose run --rm app flake8 --config=flake8.cfg .
docker-compose run --rm app ./manage.py test
```

## Features

- Add your shows and categorize them by **active**, **default** and **archived**
- Keep track of which episode you last watched
- See which unseen episodes are available
- See when the next episode is coming out
- Data synchronized each night from [thetvdb.com](http://thetvdb.com/)

## How to play

- Get an API key from [TheTVDB](http://thetvdb.com/wiki/index.php?title=Programmers_API)
- Configure `crontab` to run `manage.py sync_all_shows` each night
- Set up your database, run all database migrations
- Set up a standard Django installation and webserver
- *(Optional)* set up Sentry for error logging
- [Should work now](https://www.google.com/search?tbm=isch&q=ponies)

## Screenshots

If the words above make no sense

### The dashboard shows you what's up

![No soup for eyehandicappeds](http://kvikshaug.github.io/tvdb/index.jpg "Index")

### Search for and add new shows

![No soup for eyehandicappeds](http://kvikshaug.github.io/tvdb/search.jpg "Search")

### Show details

![No soup for eyehandicappeds](http://kvikshaug.github.io/tvdb/show.jpg "Show")