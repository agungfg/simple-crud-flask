REQUIREMENTS :
1. PYTHON 3.6
2. FLASK LIBRARY
3. PYMYSQL LIBRARY
4. JSON LIBRARY
5. MYSQL DATABASE

HOW TO RUN:
1. CREATING DATABASE:

	INSTALL AND DOWNLOAD MYSQL DATABASE	
	
	SQL QUERY:

	CREATE TABLE `payment` (
	  `id` int(11) NOT NULL,
	  `create_date` datetime NOT NULL,
	  `modified_date` datetime NOT NULL,
	  `item` varchar(64) NOT NULL,
	  `count` int(11) NOT NULL,
	  `price` int(11) NOT NULL,
	  `paid` int(11) NOT NULL,
	  `deleted_at` datetime DEFAULT NULL
	) ENGINE=InnoDB DEFAULT CHARSET=latin1;

2. INSTALL PYTHON 3.6, FLASK, PYMYSQL, JSON
	
	DOWNLOAD AND INSTALL PYTHON 3.6
	
	INSTALLING FLASK, PYMYSQL, JSON ON WINDOWS CMD :
	
	pip install flask
	
	pip install pymysql
	
	pip install json

3. CONFIGURING DATABASE SETTING
	
	OPEN query.py
	
	Watch at function def __init__(self) (line 7)
	
	Set variable host, user, password, db depend on Your PC Setting

4. CONFIGURING AND RUN FLASK
	
	OPEN CMD AND CHANGE DIR TO MINI-PROJECT
	
	-- Configuring --
	
	set FLASK_RUN_PORT=80
	
	set FLASK_APP=routes.py
	
	-- Run --
	
	python -m flask run

	OPEN localhost or 127.0.0.1 on Your browser


FILE STRUCTURE

routes.py -> all of route settings

query.py -> all of query

templates folder -> html view

static folder -> css file
