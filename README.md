
# Oowlish Customer

A simple Django REST API that provides information about clients.


## Authors

- [@johannalbino](https://www.github.com/johannalbino)



## Tech Stack

**Server:** Django, Django Rest Framework, DRF_YASG, SQLite, pandas

  
## Run Locally

Clone the project

```bash
  git clone git@github.com:johannalbino/project_oowlish.git
```

Go to the project directory

```bash
  cd project_oowlish
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Start the server with script

```bash
  ./run.sh
  ./process-file.sh
```

  
## Installation

Install oowlist_customer with pip

```bash
  pip3 install -r requirements
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
```

Install oowlist_customer with script
```bash
  ./run.sh
  ./process-file.sh
```


    
## API Reference

#### Process File customers.csv

```http
  GET /process-file
```
Process file customers.csv

#### Get one customer

```http
  GET /customer/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of customer      |

#### Get all customer

```http
  GET /customer/
```

Get all customers

#### Get documentation of project

```http
  GET /api-docs/
```

Get documentation DRF-YASG

