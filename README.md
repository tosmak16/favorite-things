[![CircleCI](https://circleci.com/gh/tosmak16/favorite-things/tree/develop.svg?style=svg&circle-token=62365b061538ceb770aa8e1f063e86f6ac9ff00b)](https://circleci.com/gh/tosmak16/favorite-things/tree/develop)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
# favorite-things

This project is an application that allows users to track their favorite things.

## Table of Contents

- [Features](#features)
- [Api-docs](#Api-docs)
- [Technologies](#technology)
- [Architecture](#Architecture)
- [Installation](#installation)
- [Testing](#testing)
- [Contribution](#contribution)
- [Frequently Asked Questions](#faqs)
- [License](#license)

## Features

It consists of the following features:

- Users can and login register
- Users can create category
- Users can create favorites-things
- Users can edit favorites-things
- Users can delete favorites-things
- Users can filter favorites-things by category
- Users can sort favorites-things
- Users can view audit logs

## Api-docs
Check out the API docs at [Favorite-things-API-DOCS](https://favorite-things-api.tosmak.me/api/docs/)

## Technology
**Favorite-Things** makes use of a host of modern technologies. The core ones are:
- [JavaScript](https://www.javascript.com/)
- [Vue](https://vuejs.org/)
- [Vuex](https://vuex.vuejs.org/)
- [Django](https://www.djangoproject.com/)
- [Django rest framework](https://www.django-rest-framework.org/)
- [Postgres](https://www.postgresql.org/)
- [Zappa](https://www.zappa.io/)

## Architecture
It's a Monolith Architecture. Below is the application backend Database Design and Architecture

![](favERD.png)


## Server side setup

- Clone the repository
- Change into the directory `$ cd /favorite-things/server`
- Install all required dependencies with `$pipenv install`
- Create a `.env` file in your root directory as described in `.env.sample` file
- Start the app with `pipenv run server`

## Client side setup

- Change into the directory `$ cd /favorite-things/client`
- Install all required dependencies with `$npm install`
- Create a `.env` file in your root directory as described in `.env.production` file
- Start the app with `npm run serve`

## Testing

- `Run pipenv run tests`

## Contribution

- Fork this repository to your GitHub account
- Clone the forked repository
- Create your feature branch
- Commit your changes
- Push to the remote branch
- Open a Pull Request


## FAQs

Contact tosmak16@gmail.com

## LICENSE

#### [MIT](./LICENSE) © [Oluwatosin Akinola]

Copyright (c) 2019 Oluwatosin Akinola
