# i-SAS_Subpackage-template_MIT
Implementation of the {package_type} subpackage {package_name} for i-SAS.

> [!IMPORTANT]
> This repository is not complete but development has been stopped.

## 1. Clone
```shell
$ git clone git@github.com:i-SAS/i-SAS_Subpackage-template_MIT.git
$ cd i-SAS_Subpackage-template_MIT
```

## 2. Docker build & run
Copy and modify `.env` according to your environment before building the docker image.
```shell
$ cp .env{.example,}
```

Now, you can build the image.
```shell
$ DOCKER_BUILDKIT=1 docker build --ssh default . -t isas_subpackage-template
$ docker compose run --rm package
```

## 3. Commands
### Download data
```shell
poetry run isas_download
```

### Add package
Modify `pyproject.toml` and execute
```shell
poetry lock
```
Note that you need to run ssh-agent in the container before the command, and rebuild the image after the command.

### Check coding conventions
```shell
flake8
```

### Run test
```shell
python -m unittest
```

---

## 4. Usage of the template

i-SAS_Subpackage-template contains the following templates of package type.

You can develop your subpackage by editing the template that matches the package type of your subpackage, and delete folders for the other templates.

| Package type | Discriptions |
| --- | --- |
| analysis | Analyze input data and compute data useful for monitoring and forecasting. |
| measurement | Measure or simulate values from measurement equipment. |
| visualization | Create widgets such as visualization or interaction for GUI. |
