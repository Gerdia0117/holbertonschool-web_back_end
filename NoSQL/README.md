# NoSQL - MongoDB

This project covers NoSQL databases, specifically MongoDB, including basic queries, Python integration with PyMongo, and data aggregation.

## Resources
- NoSQL Databases Explained
- What is NoSQL?
- MongoDB with Python Crash Course
- MongoDB Tutorial
- Aggregation Pipeline

## Learning Objectives
- What NoSQL means
- Difference between SQL and NoSQL
- What is ACID
- What is document storage
- NoSQL types
- Benefits of NoSQL databases
- How to query, insert, update and delete information from a NoSQL database
- How to use MongoDB

## Requirements
### MongoDB Command Files
- Files interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- Files should end with a new line
- First line of files should be a comment: `// my comment`
- A README.md file at the root of the project folder is mandatory

### Python Scripts
- Files interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- Files should end with a new line
- First line of files should be exactly `#!/usr/bin/env python3`
- Code should use pycodestyle style (version 2.5.*)
- All modules should have documentation
- All functions should have documentation
- Code should not execute when imported (use `if __name__ == "__main__":`)

## Tasks

### 0. List all databases
Write a script that lists all databases in MongoDB.
```bash
cat 0-list_databases | mongo
```

### 1. Create a database
Write a script that creates or uses the database `my_db`.
```bash
cat 1-use_or_create_database | mongo
```

### 2. Insert document
Write a script that inserts a document in the collection `school`:
- The document must have one attribute `name` with value "Holberton school"
```bash
cat 2-insert | mongo my_db
```

### 3. All documents
Write a script that lists all documents in the collection `school`.
```bash
cat 3-all | mongo my_db
```

### 4. All matches
Write a script that lists all documents with `name="Holberton school"` in the collection `school`.
```bash
cat 4-match | mongo my_db
```

### 5. Count
Write a script that displays the number of documents in the collection `school`.
```bash
cat 5-count | mongo my_db
```

### 6. Update
Write a script that adds a new attribute to documents with `name="Holberton school"`:
- The attribute is `address` with value "972 Mission street"
```bash
cat 6-update | mongo my_db
```

### 7. Delete by match
Write a script that deletes all documents with `name="Holberton school"` in the collection `school`.
```bash
cat 7-delete | mongo my_db
```

### 8. List all documents in Python
Write a Python function that lists all documents in a collection:
- Prototype: `def list_all(mongo_collection):`
- Return an empty list if no document in the collection

### 9. Insert a document in Python
Write a Python function that inserts a new document in a collection based on kwargs:
- Prototype: `def insert_school(mongo_collection, **kwargs):`
- Returns the new `_id`

### 10. Change school topics
Write a Python function that changes all topics of a school document based on the name:
- Prototype: `def update_topics(mongo_collection, name, topics):`
- `name` (string) will be the school name to update
- `topics` (list of strings) will be the list of topics approached in the school

### 11. Where can I learn Python?
Write a Python function that returns the list of schools having a specific topic:
- Prototype: `def schools_by_topic(mongo_collection, topic):`
- `topic` (string) will be topic searched

### 12. Log stats
Write a Python script that provides some stats about Nginx logs stored in MongoDB:
- Database: `logs`
- Collection: `nginx`
- Display:
  - First line: `x logs` where x is the number of documents
  - Second line: `Methods:`
  - 5 lines with method statistics (GET, POST, PUT, PATCH, DELETE)
  - One line with the number of documents with method=GET, path=/status

### 100. Regex filter
Write a script that lists all documents with name starting by "Holberton" in the collection `school`.
```bash
cat 100-find | mongo my_db
```

### 101. Top students
Write a Python function that returns all students sorted by average score:
- Prototype: `def top_students(mongo_collection):`
- Returns all students sorted by average score
- The average score must be part of each item returns with key = `averageScore`

### 102. Log stats - new version
Improve `12-log_stats.py` by adding the top 10 of the most present IPs in the collection `nginx` of the database `logs`:
- IPs top must be sorted

## Installation
```bash
# Install MongoDB 4.2
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org

# Install PyMongo
pip3 install pymongo
```
