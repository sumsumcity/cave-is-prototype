# CAVE Tool
Collects, analyzes and visualizes metrics.

## Installation
Prerequisite: Python 3 must be installed.

Steps:

1. Clone the repository source-code
2. Create a .env file like below
3. Run the docker compose file
4. Make a virtual environment (venv)
5. Make sure all required packages are installed

Example .env file:
```shell
GRAFANA_PASSWORD=...
MYSQL_PASSWORD=...
```

Example on Linux:
```shell
git clone https://github.com/sumsumcity/cave.git
cd cave
docker-compose up -d
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Example on Windows:
```shell
git clone https://github.com/sumsumcity/cave.git
cd cave
docker-compose up -d
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

## Example
```shell
python src/metricvisualizer.py example/config.json
```

## Additions

To delete **all** docker volumes to reset everything (even the passwords):
```shell
docker volume rm $(docker volume ls -q)
``` 

Example for Grafana Dashboard:
```shell
SELECT im.*, i.appid, m.name, concat(status, ": ", description) AS detail
FROM items_metrics AS im
JOIN items AS i ON i.itemid = im.itemid
JOIN metrics AS m ON m.metricid = im.metricid
-- WHERE i.type = "app"
-- WHERE date = (SELECT MAX(date) FROM items_metrics)
``` 