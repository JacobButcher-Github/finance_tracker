#!/bin/bash
# NOTE: These are intentionally run as postgres
# to avoid ownership problems and intentionally fail if you are not postgres
echo "Creating database: finances"
psql -U postgres -c "CREATE DATABASE finances"
echo "Initializing database: finances"
psql -d finances -U postgres -f ./finances.sql
