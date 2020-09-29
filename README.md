# Home Automation System

## TL;DR 😅

1. Run `./runDemoApp.sh`
2. Visit `localhost:8000` on your internet browser
3. View logs at `app/home.log`
4. View live changes to home data in `app/data/data.json`
5. Run `ctrl-C` to exit script (cleans up processes started in background i.e. app/api.py)

## Dependencies
* Nodejs version `12` (but version 8+ will probably work too)
* Python version `3.7`

# Description
The core home automation application is in the `/app` directory with the main file being `app/home.py`. To keep things simple the webserver (`app/api.py`) for the demo project is also in this directory since it is written in Python using Flask and using the same virtual environment.

### A word on testing:
The focus of a production ready application is the contents of the `/app` folder minus `api.py`, therefore, the only tests (`app/tests`) focus specifically on the business logic of the core software as defined by the specification.

## Core Application

### Architecture

The application is relatively simple in that it is a set of endpoints/methods defined by the specifications which use a data access abstraction (Repository Pattern) to read and write Light and Thermostat values, and to add or remove Lights. The only domain objects are the Light and the Thermostat, but it would be relatively easy to add other components/devices so long as they have a "type" and "name" defined. The application relies on duck-typing.

The data repository `app/inMemoryRepository.py` itself depends on a FileService abstraction because it performs file writes on each write operation to the in-memory data and it also reads in the initial state of the system from  a JSON file `app/data/data.json`. This is due to the specification to read and write to file.

### Assumptions
* No home has more than 1 thermostat
* Thermostat component cannot be removed
* Components of type name "Light" and "Thermostat" exist

### System Constraints
* There is only 1 Thermostat component (see Assumtions section) and that object is already initialized in the system (via `app/data/data.json` file)
* All connected components/devices must have a unique name in the system
* JSON data file (`app/data/data.json`) needs tobe formatted with a "components" key whose value is a list of json objects (corresponding to unique components in the system such as lights and a thermostat)

## Demo Project
The demo project is a website and webserver that allows users to interact with the core home automation software. The webserver (`api.py`) remains in the `app/` folder, but the front-end code does live in its own top-level folder `web/`. The frontend is written in plain Javascript using the React based Gatsby framework for static websites. Gatsby was chosen because it is incredibly easy to setup and build websites with.

Following the instructions from the `web/README` file, you can get everything up and running for the front-end. You can run in both production and development environments. But the `web/public` folder contains all the static assets necessary to serve the front-end on any webserver such as nginx. I would have prefered to serve these files using the Flask api but due to being a new Python developer I refrained from making the project more complicated lest I get stuck figuring out configuration problems for hours.I chose Flask because it was recommended to me adn also because it is one of the more common frameworks besides Django.

Concurrency is not supported on the webserver because it is assumed that the users of a home automation system are very few therefore heavy traffic is unlikely. With more time, I would have added websockets to the webserver in order for all connected clients to be notified of write changes to the system (ex. light turns on) but since the focus of the project was to build the core home automation application I refrained from making websocket notifications a priority.

Gatsby documentation suggests that you need the Gatsby-CLI running globally to work effectively but I've changed the `package.json` scripts to utilize the gatsby "executable" from the gatsby npm package in `node_modules`. This removes the extra step of having to install Gatsby-CLI as a global NPM package for non-Nodejs users who want to get up and running fast.
