# ETL-PostgreSQL-Elasticsearch

This project is a simple example of ETL with PostgreSQL and Elasticsearch. It demonstrates the integration of Elasticsearch and PostgreSQL using Python. It establishes connections to both Elasticsearch and PostgreSQL databases, creates a table in PostgreSQL, inserts sample data, retrieves the data, transforms it, and then loads the transformed data into Elasticsearch.

## Getting Started

Run docker containers:
```bash
docker-compose up -d
```

Wait for the Docker containers to start.

Run the script: 
```bash
python etl.py
```

Expected output:

```
{'name': '2534948e13e1', 'cluster_name': 'docker-cluster', 'cluster_uuid': 'a37z0xf5RMmm6xEN13rd0A', 'version': {'number': '8.7.0', 'build_flavor': 'default', 'build_type': 'docker', 'build_hash': '09520b59b6bc1057340b55750186466ea715e30e', 'build_date': '2023-03-27T16:31:09.816451435Z', 'build_snapshot': False, 'lucene_version': '9.5.0', 'minimum_wire_compatibility_version': '7.17.0', 'minimum_index_compatibility_version': '7.0.0'}, 'tagline': 'You Know, for Search'}
PostgreSQL: Таблица создана и данные добавлены успешно.
Elasticsearch: Индекс создан и данные добавлены успешно.
По id=1 найдены данные:
{'_index': 'my_index', '_id': '1', '_version': 1, '_seq_no': 0, '_primary_term': 1, 'found': True, '_source': {'id': 1, 'name': 'Alice', 'age': 30}}
```