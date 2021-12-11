#!/usr/bin/env bash
# Wait for database to startup
sleep 20
./opt/mssql-tools/bin/sqlcmd -S localhost -U SA -d testDB -P Test123@ -i test.sql