#!/bin/bash

# Check if file path is provided
if [ -z "$1" ]
then
    echo "No arguments supplied, please provide a file path."
    exit 1
fi

filepath="$1"
directory=$(dirname "$filepath")

# Create parent directories if they don't exist
mkdir -p "$directory"

json_data=$(cat <<EOF
{
  "cells": [
   {
    "cell_type": "markdown",
    "metadata": {},
    "source": []
   }
  ],
  "metadata": {
   "language_info": {
    "name": "python"
   }
  },
  "nbformat": 4,
  "nbformat_minor": 2
}
EOF
)

# Write the json data to the file
echo "$json_data" > "$filepath"
