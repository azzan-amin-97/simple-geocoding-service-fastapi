# Simple Geocoding Service FastAPI
A simple API which will returns the latitude and longitude for each requests using FastAPI

## Introduction
This is a simple geocoding service API project using python. The library package used for this API is pgeocode. Pgeocode is a python package that provides postal geocoding service. The goal of this API is to mock the large geocoding microservice in order to understand how to API works.

## About the API
The architecture of the API can be explained by referring to the diagram below.


Scenario:
A client wanted to have latitude and longitude of a certain address. The client will post a request to the api with the raw address. When the API received the address, it will check the geocoding database if the address is already exists. If it is exists, the API will fetch the existing geocoded address and send the response to the client. Otherwise, the API will call the geocoding function to geocode the address. The new geocoded data will save into the database.Then, the API will send it as response to the client. 

## Running the API
'uvicorn main:app --reload'

## Run Test on the API
'pytest'

Goodluck!
