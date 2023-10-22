# What does database-connection.py do?
SpeedThis is a Python class called `DatabaseConnection` that represents a connection to a SQLite database. The class has several methods that allow it to save and read data from the database. The class uses the `sqlite3` library to connect to the database and execute SQL queries.

The `DatabaseConnection` class has three attributes: `connection`, `cursor`, and `database_name`. The `connection` attribute stores the connection to the database. The `cursor` attribute stores the cursor used to execute SQL queries. The `database_name` attribute stores the name of the database.

The `DatabaseConnection` class has a constructor that initializes a new instance of the class. The constructor takes a single argument, `database_name`, which is the name of the database to connect to. The constructor initializes the `database_name` attribute to the `database_name` argument.

The `DatabaseConnection` class has several methods for saving and reading data from the database. The `connect` method connects to the database using the `sqlite3.connect` method and initializes the `cursor` attribute. The `__exit__` method commits any changes made to the database and closes the connection. The `saveSensorDataA`, `saveSensorDataB`, and `saveFanData` methods save data to the `sensora`, `sensorb`, and `fan` tables, respectively. The `readSensorAData`, `readSensorBData`, and `readFanData` methods read data from the `sensora`, `sensorb`, and `fan` tables, respectively. The `getAllData` method fetches all the data from the `sensora`, `sensorb`, and `fan` tables and returns it as a list of tuples.

Overall, this code provides a simple class for connecting to a SQLite database and saving and reading data from the database. The code could be improved by adding more error handling and input validation to the methods, as well as improving the performance of the database queries. Additionally, the code could be modified to allow for more tables to be added to the database.

# What does fan.py do?
SpeedThis is a Python class called `Fan` that represents a fan that can be controlled using pulse-width modulation (PWM). The class uses the `pwmio` and `board` libraries to control the fan speed using a PWM signal. The class has several attributes and methods that allow it to start and stop the fan, increase and decrease the fan speed, and get the current fan speed.

The `Fan` class has two attributes: `currentSpeed` and `device`. The `currentSpeed` attribute stores the current speed of the fan. The `device` attribute stores the `pwmio.PWMOut` object used to control the fan.

The `Fan` class has a constructor that initializes a new instance of the class. The constructor initializes the `currentSpeed` attribute to 50, which represents 50% of the maximum fan speed. The constructor also initializes the `device` attribute to a `pwmio.PWMOut` object using the `board.D13` pin and a frequency of 25000 Hz.

The `Fan` class has four methods: `startSpinning`, `stopSpinning`, `increaseSpeed`, and `decreaseSpeed`, and `getCurrentSpeed`. The `startSpinning` method starts the fan spinning by printing a message to the console. The `stopSpinning` method stops the fan from spinning by printing a message to the console. The `increaseSpeed` method increases the speed of the fan by setting the duty cycle of the `device` attribute to a value between 0 and 65535 based on the percentage increase passed as an argument. The method also updates the `currentSpeed` attribute to reflect the new fan speed. The `decreaseSpeed` method decreases the speed of the fan by setting the duty cycle of the `device` attribute to a value between 0 and 65535 based on the percentage decrease passed as an argument. The method also updates the `currentSpeed` attribute to reflect the new fan speed. The `getCurrentSpeed` method returns the current speed of the fan by returning the `currentSpeed` attribute.

Overall, this code provides a simple class for controlling a fan using PWM signals. The code could be improved by adding more error handling and input validation to the methods, as well as improving the performance of the fan speed control. Additionally, the code could be modified to allow for more pins to be used for controlling multiple fans.

# What does sensor.py do?
SpeedThis is a Python class called `Sensor` that represents a sensor that reads temperature from a DHT22 sensor. The class uses the `adafruit_dht` library to read temperature values from the sensor and the `board` library to access the GPIO pins on the Raspberry Pi. The class has several attributes and methods that allow it to read temperature values from the sensor and stop reading from the sensor.

The `Sensor` class has four attributes: `startTime`, `gpio`, and `device`. The `startTime` attribute stores the time when the sensor was started. The `gpio` attribute stores the GPIO pin number used by the sensor. The `device` attribute stores the `adafruit_dht.DHT22` object used by the sensor.

The `Sensor` class has a constructor that initializes a new instance of the class. The constructor takes a single argument, `selectedGPIO`, which is the GPIO pin number to be used by the sensor. The constructor initializes the `currentValue` attribute to 0, the `startTime` attribute to the current time using the `time.time()` method, and the `gpio` attribute to the `selectedGPIO` argument. The constructor also initializes the `device` attribute to a `adafruit_dht.DHT22` object using the `board` library and the `selectedGPIO` argument.

The `Sensor` class has three methods: `getCurrentValue`, `readGPIO`, and `stopReading`. The `getCurrentValue` method returns the current temperature value read by the sensor by calling the `readGPIO` method. The `readGPIO` method reads the temperature value from the `device` attribute and returns it. If an error occurs while reading the temperature value, the method returns -1. The `stopReading` method stops reading from the `device` attribute by calling the `exit` method.

Overall, this code provides a simple class for reading temperature values from a DHT22 sensor using the `adafruit_dht` library. The code could be improved by adding more error handling and input validation to the methods, as well as improving the performance of the temperature readings.

# What does project.py do?
This is a Python class called Project that represents a project that collects data from sensors and saves it to a database. The class uses the Sensor, Fan, and DatabaseConnection classes to read data from sensors, control a fan, and save data to a database. The class has several attributes and methods that allow it to start and stop a sensor session, fetch data from the database, and control the fan based on the sensor readings.

The Project class has five attributes: startTime, sensors, fans, databaseConnection, and active. The startTime attribute stores the start time of the project. The sensors attribute stores a list of Sensor objects. The fans attribute stores a list of Fan objects. The databaseConnection attribute stores a DatabaseConnection object. The active attribute is a flag indicating whether the sensor session is active or not.

The Project class has a constructor that initializes a new instance of the class. The constructor initializes the startTime attribute to the current time using the time.time() method. The constructor also initializes two Sensor objects and one Fan object and adds them to the sensors and fans lists, respectively.

The Project class has three methods: startSensorSession, stopSensorSession, and fetchAllDBData. The startSensorSession method starts the sensor session and saves the data to the database. It creates a new DatabaseConnection object and connects to the database. It then enters a loop that reads data from the sensors and saves it to the database. The method also controls the fan based on the sensor readings. The stopSensorSession method stops the sensor session and stops the sensors from reading. The fetchAllDBData method fetches all the data from the database using the getAllData method of the DatabaseConnection object.

Overall, this code provides a simple class for collecting data from sensors and saving it to a database. The code could be improved by adding more error handling and input validation to the methods, as well as improving the performance of the database queries. Additionally, the code could be modified to allow for more sensors and fans to be added to the project.

# What does webserver.py do?
SpeedThis is a Python Flask web server that serves a web page with various routes. The web server is created using the Flask library and the routes are defined using the `@app.route` decorator. The web server has several routes that are used to start and stop a sensor session, view data from the sensor session, create a CSV file from the data, and download the CSV file.

The `index` route is the starting page of the web server. It renders an HTML template called `index.html` and passes in some data to be displayed on the page. The data includes the current time, the title of the web page, and whether or not a sensor session is currently running.

The `startsession` route is called when a user clicks a button to start a new sensor session. It starts a new thread that runs the `startSensorSession` method of the `currentProject` object. The `startSensorSession` method is defined in the `Project` class and starts a sensor session that reads data from sensors and stores it in a database. After starting the sensor session, the `startsession` route renders the `index.html` template with updated data that indicates a sensor session is running.

The `stopsession` route is called when a user clicks a button to stop the current sensor session. It stops the sensor session by calling the `stopSensorSession` method of the `currentProject` object and waits for the thread to finish. After stopping the sensor session, the `stopsession` route renders the `index.html` template with updated data that indicates no sensor session is running.

The `renderData` route is used to view the data that has been collected during the sensor session. It fetches all the data from the database using the `fetchAllDBData` method of the `currentProject` object and renders the `data.html` template with the data.

The `createcsv` route is used to create a CSV file from the data that has been collected during the sensor session. It fetches all the data from the database using the `fetchAllDBData` method of the `currentProject` object and writes it to a CSV file called `sensordata.csv`. After creating the CSV file, the `createcsv` route renders the `data.html` template with the data.

The `downloadcsv` route is used to download the CSV file that was created using the `createcsv` route. It sends the CSV file to the user's browser as an attachment with the filename `sensordata.csv`.

Overall, this code provides a simple web interface for starting and stopping a sensor session, viewing the data from the sensor session, and downloading the data as a CSV file. The code could be improved by adding more error handling and input validation to the routes, as well as improving the performance of the database queries.


# Python Version?
python 3.9.2