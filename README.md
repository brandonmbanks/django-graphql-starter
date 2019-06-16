# django-graphql-starter

## Getting Started

To get started contributing you need to have [Docker](https://docs.docker.com/install/) installed. From here, you should be able to complete most things with Docker and the provided [Makefile](https://github.com/brandonmbanks/django-graphql-starter/blob/master/Makefile).

Just run `make` to start the docker containers, install dependencies, copy the env file, and migrate the database.

If you prefer to start the project without using the `Makefile`, you will need to make sure that dependencies are installed, all of the containers are running, the `.env` file is present, and the database is migrated and seeded.

## Running Tests
Use the Makefile
```bash
make test
```
Or

1. Exec into the app container
```bash
docker-compose exec app bash
```

2. Run pytest
```bash
pytest
```

## Dependencies
I use [pip-tools](https://github.com/jazzband/pip-tools) to help manage dependencies.

`requirements.in` is the file which contains the project's base required dependencies and is the file to which you would add more dependencies.

`pip-compile` will produce your requirements.txt, with all the dependencies (and all underlying dependencies) pinned.

### Adding Dependencies
#### Steps

1. Add dependency to `requirements.in`

```bash
echo "pytest" >> requirements.in
```

2. Run `pip-compile`
```bash
make compile
```

3. Rebuild containers to install dependencies from the updated `requirements.txt`
```bash
make build
```
*By rebuilding, we don't have to install the new dependencies each time we start the containers and the image will be updated for the next time start the app.*

### Upgrading Dependencies
#### Steps

1. Upgrade using `pip-compile` through the `Makefile`
```bash
make upgrade dep=pytest
```

2. Rebuild containers to install dependencies from the updated `requirements.txt`
```bash
make build
```

*If you need more complex updating control, exec into app container*
```bash
docker-compose exec app bash
```

Follow `pip-tools` [documentation](https://github.com/jazzband/pip-tools#updating-requirements) for updating requirements
