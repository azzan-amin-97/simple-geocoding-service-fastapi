# FastAPI Simple Geocoding Service
A simple API which will return the latitude and longitude for each request using FastAPI and <a href="https://github.com/symerio/pgeocode">Pgeocode</a> Library

## Introduction
This is a simple geocoding service API project using python. One of the library package used for this API is pgeocode. Pgeocode is a python package that provides postal geocoding service. The goal of this API is to mock the large geocoding microservice in order to understand how the API works.

## About the API
The architecture of the API can be explained by referring to the diagram below.

![](img/about_api.PNG)
Scenario:
A client wanted to have latitude and longitude of a certain address. The client will post a request to the api with the raw address. When the API received the address, it will check the geocoding database if the address is already exists. If it is exists, the API will fetch the existing geocoded address and send the response to the client. Otherwise, the API will call the geocoding function to geocode the address. The new geocoded data will save into the database.Then, the API will send it as response to the client. 

## Running the API 
Command:
`uvicorn main:app --reload`

## Run Test on the API
Command:
`pytest`

Goodluck!
