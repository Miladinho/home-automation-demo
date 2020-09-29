#!/bin/bash

# Install depndencies
npm install 

# Setup environment variables file
echo "GATSBY_API_URL=http://127.0.0.1:5000/api" > .env.development
# Add .env.production if planning to run in production
