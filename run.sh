#!/bin/bash
# Go through a full test suite.
echo "Generating a new set of words..."
./generate.py
echo "Brute-force method:"
./1-brute-force.py
echo "Serial reducer method:"
./2-map-reduce.py
echo "Distributed map-reduce method:"
./3-distributed-map-reduce.py
