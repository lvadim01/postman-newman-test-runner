# postman-newman-test-runner

An application written in **Python** 

## Description

The application runs Postman test collections stored in the cloud
Using newman it generates a status report per endpoint
The generated report is sent by email with the test results

## Installation

* Clone the repo
* In the root folder avtivate virtual environment `source venv/bin/activate`
* Install required modules `pip install -r requirements.txt`
* Amend the parameters accordingly to your postman/gmail - acounts
* Amend the parameters accordingly to your collections and desired environments

## Software required

* *Node.js*
* *Newman Cli*
* *Python* > 2.7

## Running tests

* run `python main.py -e  -c -r`
* -e - any chosen env (test, production)
* -c - postman collection key  (can run multiple collections at once [coll1, coll2, coll3])
* -r - report, send or do not send an email report (true, false) 

## Notes
The generated file is stored locally also in the results directory

