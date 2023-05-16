#!/bin/bash

for i in {1..5}
do
  kubectl  apply -f frontend.yaml -n frontend
  sleep 120
  kubectl  delete  -f frontend.yaml -n frontend
  sleep 120
done
