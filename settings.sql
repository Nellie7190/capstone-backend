-- settings.sql
CREATE DATABASE capbackend;
CREATE USER capbackenduser WITH PASSWORD 'capBackend';
GRANT ALL PRIVILEGES ON DATABASE capbackend TO capbackenduser;