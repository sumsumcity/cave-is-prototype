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

## Collector Possibilities

### HTTP Collector (works also for Confluence)
GET Requests

### JIRA Collector
https://developer.atlassian.com/server/jira/platform/rest-apis/

### Contrast IAST Collector
https://github.com/Contrast-Security-OSS/contrast-teamserver-api-docs/tree/main/saas-restapi-v3

### Contrast SCA Collector
https://github.com/Contrast-Security-OSS/contrast-teamserver-api-docs/tree/main/saas-restapi-v3

### Dependabot Collector
https://docs.github.com/en/rest/dependabot/alerts?apiVersion=2022-11-28#about-dependabot-alerts

### CodeQL Collector
https://docs.github.com/en/rest/code-scanning/code-scanning?apiVersion=2022-11-28#about-code-scanning

It is not possible to obtain multiple severity levels in one request. The configuration of the severity levels in the validator is therefore very important.


## Example
```shell
python src/metricvisualizer.py example/config.json
```

## Example Metrics
The metrics are from the OWASP DSOVS Framework:
https://owasp.org/www-project-devsecops-verification-standard/

### sca
https://github.com/OWASP/www-project-devsecops-verification-standard/blob/main/document/CODE-005-Software-Composition-Analysis-SCA.md
Possible Collectors: contrast_sca-collector, dependabot_sca-collector

### iast
https://github.com/OWASP/www-project-devsecops-verification-standard/blob/main/document/TEST-003-Interactive-Application-Securit-Testing-IAST.md
Possible Collectors: contrast_iast-collector

### sast
https://github.com/OWASP/www-project-devsecops-verification-standard/blob/main/document/CODE-004-Static-Application-Security-Testing-SAST.md
Possible Collectors: codeql_sast-collector

### threatModel
https://github.com/OWASP/www-project-devsecops-verification-standard/blob/main/document/DES-002-Threat-Modelling.md
Possible Collectors: http-collector (e.g. confluence or other websites)

### securityIssueTrackingDesign
https://github.com/OWASP/www-project-devsecops-verification-standard/blob/main/document/REQ-004-Security-Issues-Tracking.md
Possible Collectors: (jira-collector)




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