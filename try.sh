#!/bin/bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" \
-d '{"Price":1000 , "Rating":8.6 , "Spa":0 , "Wellness_Centre":0 , "Swimming_Pool":1 , "Fitness_Centre":1 ,"Room_Service":1 , "Facilities":0, "Airport_Shuttle":1 }'