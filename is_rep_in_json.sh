#!/bin/bash

ZIPCODE=$1
if [ -z "$ZIPCODE" ]
then
    echo "no input provided"
    exit 1
fi
if grep -q "$ZIPCODE" zips_to_reps.json
then
  echo "$ZIPCODE is in json"
else
  echo "$ZIPCODE is not in json"
fi
exit 0