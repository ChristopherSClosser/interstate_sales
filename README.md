# Interstate Sales
---
### Description
Version: *0.0.2b*

New Features
* Data Base
* REST API - Add, Update, Delete Items
* Search Feature

### Authors
---
* Jason Portlock
* [Chris Closser](https://github.com/ChristopherSClosser/interstate_sales)

### Getting Started
---
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository. To accomplish this, execute these commands:

`$ git clone https://github.com/ChristopherSClosser/interstate_sales.git`

`$ cd interstate_sales`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment named "ENV", and install the project requirements into your VE.

`$ python3 -m venv ENV`

`$ source ENV/bin/activate`

`$ pip install e .`
##### *Serving Locally*
Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command at the root level of your application, at the same level as `development.ini` and `production.ini`.
`$ pserve development.ini`
Once you have executed this command, open your browser, and go to `localhost:6543/`.
### Test Suite
---
##### *Running Tests*
This application uses [unittest](https://docs.python.org/3/library/unittest.html) as a testing suite. To run tests, run:

``$ python3 -m unittest``

To view test coverage, run:

``$ coverage report -m``
##### *Test Files*
The testing files for this project are:

| File Name | Description |
|:---:|:---:|
| `./interstate_sales/tests.py` | Backend I-S Tests. |

### URLs
---
The URLS for this project can be found in the following modules:

| URL module | Description |
|:---:|:---:|
| `./interstate_sales/routes.py` | I-S Defined Routes. |

### Pyramid Development Files
---
Development files specific to the Pyramid web framework can be found in the following files:
* ./development.ini

### Development Tools
---
* *python* - programming language
* *pyramid* - web framework
* *postgres* - database storage

### License
---
This project is licensed under Apache License - see the LICENSE.md file for details.
### Acknowledgements
---

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*
