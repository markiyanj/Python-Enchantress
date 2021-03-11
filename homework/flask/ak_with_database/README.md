README.md
setup.py
requirements.txt
requirements-to-freeze.txt
our_store
- models.py
- db.py
- __init__.py
- config.py
tests
- conftest.py
- unit
- integration
- end_to_end


# Run postgress from docker
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=pass -e POSTGRES_USER=illia -d postgres
