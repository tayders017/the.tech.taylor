<!--
Documentation for Project_Grafanista
-->
<div align="center">

  <img src="assets/logo.png" alt="logo" width="200" height="auto" />
  <h1>Project Grafanista Documentation
</h1>
  
  <p>
    Setting Up Grafana Cloud with Prometheus and OpenWeatherMap API for Weather Data Visualization
  </p>

  <p>
    This will be done 100% free by using free trial Grafana Cloud account, Prometheus (OS) running locally, and using the free OpenWeatherMap API.
  </p>
  
  
<!-- Badges -->
<p>
  <a href="">
    <img src="https://img.shields.io/badge/Grafana-F2F4F9?style=for-the-badge&logo=grafana&logoColor=orange&labelColor=F2F4F9" />
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/Prometheus-000000?style=for-the-badge&logo=prometheus&labelColor=000000" />
  </a>
</p>
   
<h4>
    <a href="https://github.com/tayders017/the.tech.taylor/tree/main/projects/Grafana/Project_Grafanista/dash_demo_img.jpg">View Dashboard Demo</a>
  <span> · </span>
    <a href="https://github.com/tayders017/the.tech.taylor/tree/main/projects/Grafana/Project_Grafanista/README.md">Documentation</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [Introduction](#star2-about-the-project)
  * [Screenshots](#camera-screenshots)
  * [Tech Stack](#space_invader-tech-stack)
  * [Environment Variables](#key-environment-variables)
- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Installation](#gear-installation)
  * [Run Script](#test_tube-run-script)
  * [Edit Prometheus Configuration](#running-edit-prometheus-configuration)
  * [Create Grafana Account](#triangular_flag_on_post-create-grafana-account)
  * [Integrate Prometheus](#triangular_flag_on_post-integrate-prometheus)
  * [Create Dashboard](#triangular_flag_on_post-create-dashboard)
- [Configuration](#eyes-configuration)
- [Challenges and Solutions](#wave-challenges-and-solutions)
- [Conclusion](#grey_question-conclusion)
- [Acknowledgements](#gem-acknowledgements)

  
<!-- Introduction -->
## :star2: Introduction


<!-- Screenshots -->
### :camera: Screenshots

<div align="center"> 
  <img src="https://placehold.co/600x400?text=Your+Screenshot+here" alt="screenshot" />
</div>


<!-- TechStack -->
### :space_invader: Tech Stack

<details>
  <summary>Host Client</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">VirtualBox</a></li>
    <li><a href="https://nextjs.org/">Ubuntu</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
    <li><a href="https://expressjs.com/">Express.js</a></li>
    <li><a href="https://go.dev/">Golang</a></li>
    <li><a href="https://nestjs.com/">Nest.js</a></li>
    <li><a href="https://socket.io/">SocketIO</a></li>
    <li><a href="https://www.prisma.io/">Prisma</a></li>    
    <li><a href="https://www.apollographql.com/">Apollo</a></li>
    <li><a href="https://graphql.org/">GraphQL</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mysql.com/">MySQL</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
  </ul>
</details>


<!-- Env Variables -->
### :key: Environment Variables

To run this project, you will need to generate an API key from OpenWeatherMap.

`API_KEY`

`ANOTHER_API_KEY`

<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

This project will be performed on a clean Ubuntu VM that was created in VirtualBox with Python and Pip installed.

Before starting, verified the following tools and services were installed or available:
* Prometheus installed and running.
* Grafana Cloud account.
* OpenWeatherMap API key.

This project uses prometheus_client Python library to expose weather data as Prometheus metrics.

```bash
 pip install prometheus_client
```

<!-- Installing prometheus_client Python library -->
### :gear: Installation

Before installing the prometheus_client Python library, verify everything is up-to-date with the latest updates.

Check for updates:

```bash
  sudo apt update
```

Run updates:

```bash
  sudo apt upgrade
```

Next, install the prometheus_client Python library.

Run the following to install the prometheus_client Python library:

```bash
  pip install requests prometheus_client
```

<!-- Create and run a python script to get weather data -->
### :test_tube: Run Script

Use a python script and the OpenWeatherMap API to periodically get weather data, expose the data as Prometheus metrics, and run a simple HTTP server to allow Prometheus to scrape the weather metrics.

Use script weather_exporter.py located in this GitHub project:
- <a href="https://github.com/tayders017/the.tech.taylor/tree/main/projects/Grafana/Project_Grafanista/weather_exporter.py">/weather_exporter.py</a>
- Update the script to reflect the correct API_KEY information and to ensure it has the desired 'cities' to pull data for listed.
  - To get an OpenWeatherMap API:
    - Sign up for a free account, link here: <a href="https://openweathermap.org/">OpenWeatherMap</a>
    - Once logged in, navigate to API keys and activate a new API key.
    - After the key is active it can now be copied and pasted into the script (or wherever else it is needed).

Run the script to start the server:

```python
  python3 weather_exporter.py
```

Check the server to verify the metrics.

Open your web browser and navigate to:

```
  http://<prometheus-ip>:8000/metrics
```

<!-- Edit configuration for Prometheus to Scrape Weather Data -->
### :running: Edit Prometheus Configuration

Update the prometheus.yml file to add the Python script as a target.

Locate the prometheus.yml file by running the following command and verifying the file location:

```bash
  sudo systemctl status prometheus
```
<a href="" /><img src="assets/chkcfgloc.png" alt="check_config" width="100" height="auto" />

Then update the prometheus.yml, this can be done via TextEdit or cli:

```bash
  sudo nano /etc/prometheus/prometheus.yml
```

Update the file and save when finished:

```bash
  scrape_configs: 
  - job_name: 'weather_exporter' 
    static_configs: 
      - targets: ['<VM_IP>:8000']
```
- If you need to check what the IP is for the VM, run the following command:
```bash
  ifconfig
```

Lastly, restart Prometheus anytime changes are made to the .yml for the configuration to take effect:

```bash
  sudo systemctl restart prometheus
```

Run the below command to check the status of Prometheus:

```bash
  sudo systemctl status prometheus
```

<!-- Set up Grafana Cloud Account (free version) -->
### :triangular_flag_on_post: Create Grafana Cloud Account

Sign up for a Grafana Cloud account through the Grafana site.

Visit Grafana Cloud and create a free account:

```
  https://grafana.com/auth/sign-up/create-user
```

After the account is active, access your Grafana Cloud portal home.

```
  https://<GRAFANA_ACCOUNT_NAME>.grafana.net/a/cloud-home-app
```

<!-- Integrate Prometheus with Grafana Cloud -->
### :triangular_flag_on_post: Integrate Prometheus

Configure local Prometheus instance to push metrics to Grafana Cloud using the provided remote_write URL and API Key by creating a Prometheus data source in Grafana Cloud so the weather data can be further visualized.

Follow the instructions to create a new Prometheus data source in Grafana Cloud.
- See documentation for refrence: <a href="https://grafana.com/docs/grafana/latest/datasources/prometheus/configure-prometheus-data-source/#configure-the-data-source">Configure the data source</a>

Find and gather the Remote Write Endpoint URL and API Key under the settings for Prometheus.
- The URL is where Prometheus will send the data.
- Example of URL:

```
https://prometheus-blocks-us-central1.grafana.net/api/prom/push
```

Use the Remote Write Endpoint URL and the API Key to update the Prometheus configuration file.

```bash
remote_write:
  - url:  'https://prometheus-us-example-URL.grafana.net/api/prom/push' 
    basic_auth: 
      username: <Grafana_Cloud_Username>
      password: <Grafana_Cloud_API_Key>
      #Provided in Grafana setup instructions
```

Lastly, restart Prometheus so the changes to the configuration are applied:

```bash
  sudo systemctl restart prometheus
```

<!-- Create dashboard(s) in Grafana Cloud to visualize the data -->
### :triangular_flag_on_post: Create Dashboard

Create a new dashboard in Grafana to view the weather metrics data.
- In the Grafana Cloud UI, go to Dashboards and select New Dashboard.
- Add panels and query your custom metrics (e.g., city_temperature_celsius{city="Stockholm"}) to visualize the weather data.
- Here is an example of the panel query: 
<a href="" /><img src="assets/dashqueryex.png" alt="dash_query" width="100" height="auto" />
- Update the “Legend” with 'Custom' so the label for the query is easier to read.
<a href="" /><img src="assets/dashqueryex.png" alt="dash_query" width="100" height="auto" />

<!-- Usage -->
## :eyes: Usage

Below are tips when referencing any steps in this project documentation.

Enable Prometheus to start on boot:

```bash
sudo systemctl enable prometheus
```

To keep the script running in the background, run:

```bash
python3 weather_exporter.py $
```


<!-- Contributing -->
## :wave: Challenges and Solutions


Challenges incurred throughout the project with solutions:
- API Limitations:
  - Using the free version of the OpenWeatherMap API has its limits, for instance, only the paid/pro version is able to gather historical data (ie. past/future data).
- Incountered error "Error: externally-managed-environment":
  - Resolve by running:
  ```bash
  python3 -m venv ~/py_envs
  source ~/py_envs/bin/activate
  python3 -m pip install xyz
  ```
  - Review the following article for more in depth details on the error:
  ```
  https://builtin.com/articles/error-externally-managed-environment
  ```
- To enhance the configuration and make it more robust, Prometheus could be ran from a Docker container, this would provide advanced scalability and would allow for further isolation from the host system.
  - The following documentation provides details on this: Install Docker Engine on Ubuntu - 
  ```
  https://docs.docker.com/engine/install/ubuntu/
  ```


<!-- Conclusion -->
## :grey_question: Conclusion

- Things learned throughout project:

  + By integrating Grafana Cloud with Prometheus and the OpenWeatherMap API, you can create powerful visual dashboards that monitor weather conditions in real-time. This setup can be further expanded to monitor other external data sources, making it versatile for different use cases.


<!-- References -->
## :gem: References

The below section provides useful resources and libraries used in the project and documentation.

 - [Shields.io](https://shields.io/)
 - [Awesome Readme Template](https://github.com/Louis3797/awesome-readme-template/blob/main/README.md)
 - [Configure Prometheus](https://grafana.com/docs/grafana/latest/datasources/prometheus/configure-prometheus-data-source/)
 - [OpenWeatherMap API Getting Started](https://openweathermap.org/appid)
 - [Grafana Visualizations](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/)
 - [Grafana Cloud](https://grafana.com/auth/sign-in)
 - [Prometheus Client Python Library](https://github.com/prometheus/client_python)
 - [Requests](https://pypi.org/project/requests/)
 - [Pip](https://pypi.org/project/pip/)
