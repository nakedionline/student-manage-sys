#!/bin/sh

mongoimport --host Cluster0-shard-0/cluster0-shard-00-00-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-01-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-02-bxkea.gcp.mongodb.net:27017 --ssl --username stddbu --password stddbu --authenticationDatabase admin --db studentDB --collection schools --type=json --file='./output/data-higher-certificate.json'


mongoimport --host Cluster0-shard-0/cluster0-shard-00-00-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-01-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-02-bxkea.gcp.mongodb.net:27017 --ssl --username stddbu --password stddbu --authenticationDatabase admin --db studentDB --collection schools --type=json --file='./output/data-diploma.json'


mongoimport --host Cluster0-shard-0/cluster0-shard-00-00-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-01-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-02-bxkea.gcp.mongodb.net:27017 --ssl --username stddbu --password stddbu --authenticationDatabase admin --db studentDB --collection schools --type=json --file='./output/data-bachelor-degree.json'


mongoimport --host Cluster0-shard-0/cluster0-shard-00-00-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-01-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-02-bxkea.gcp.mongodb.net:27017 --ssl --username stddbu --password stddbu --authenticationDatabase admin --db studentDB --collection schools --type=json --file='./output/data-baccalaureus-technologiae.json'


mongoimport --host Cluster0-shard-0/cluster0-shard-00-00-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-01-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-02-bxkea.gcp.mongodb.net:27017 --ssl --username stddbu --password stddbu --authenticationDatabase admin --db studentDB --collection schools --type=json --file='./output/data-advanced-certificate.json'

mongoimport --host Cluster0-shard-0/cluster0-shard-00-00-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-01-bxkea.gcp.mongodb.net:27017,cluster0-shard-00-02-bxkea.gcp.mongodb.net:27017 --ssl --username stddbu --password stddbu --authenticationDatabase admin --db studentDB --collection schools --type=json --file='./output/data-advanced-diploma.json'