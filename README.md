# Single Domain Crawler

## Quickstart

### Quickstart: Virtual Environment

- Tested with Python3.10.
- Move into working directory `python-web-scraper`.
- Install `virtualenv` if not already installed: `python3.10 -m pip install virtualenv`
- Create a virtual environment: `python3.10 -m venv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install the requirements: `python3.10 -m pip install -r requirements.txt`
- Run unit tests: `python3.10 -m pytest -m "not integration"`
- Run the application: `python3.10 -m crawler.main --url http://monzo.com --limit 3 --log-level=INFO --workers 1`

### Quickstart: Docker

- Move into working directory `crawl_project`.
- Build the docker image: `docker build -t crawler-harry-turner-submission .`
- Run unit tests: `docker run crawler-harry-turner-submission python -m pytest -m "not integration"`
- Run the docker image: `docker run crawler-harry-turner-submission python -m crawler.main --url http://monzo.com --limit 3 --log-level=INFO --workers 1`

## Run Integration Test

- To run the integration test, you need to have a running instance of the application.
- In one terminal, move into `tests/fake_website` and run `python3.10 -m http.server 8000`.
- In another terminal, activate the virtual environment and run `python3.10 -m pytest -m "integration"`.
