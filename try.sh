#!/bin/bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" \
-d '{"Swimming_Pool":1 , "Room_Service":1 , "Fitness_Centre":0 , "Airport_Shuttle":0 , "Highspeed_Internet":1 , "Airconditioning":1}'