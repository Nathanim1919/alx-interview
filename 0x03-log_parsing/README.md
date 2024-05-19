# 0x03. Log Parsing
`Algorithm`, `Python`

For the “0x03. Log Parsing” project, you will need to apply your knowledge of Python programming, focusing on parsing and processing data streams in real-time. This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. Here’s a list of concepts and resources that you might find useful:

## Concepts Needed:
### 1. file I/O:
File I/O (input/output) is the process of reading data from and writing data to files on a computer. In Python, you can use the built-in `open()` function to open a file and read or write data to it. File I/O is essential for reading log files, processing data streams, and storing output data.
[File I/O - Real Python](https://realpython.com/read-write-files-python/)

### 2. Signal handling in Python:
Signal handling in Python allows you to catch and handle signals sent to a process, such as SIGINT (interrupt signal) or SIGTERM (termination signal). You can use the `signal` module in Python to set up signal handlers and perform cleanup operations when a signal is received.
[Signal Handling in Python - Real Python](https://realpython.com/python-signals/)

### 3. Data processing:
Data processing is the process of transforming raw data into meaningful information by performing calculations, aggregations, and transformations on the data. In this project, you will need to process log data in real-time, extract relevant information, and calculate statistics based on the data.
[Data Processing - Wikipedia](https://en.wikipedia.org/wiki/Data_processing)

### 4. Regular expressions:
Regular expressions (regex) are sequences of characters that define a search pattern, used for pattern matching within strings. In this project, you may need to use regular expressions to extract specific fields or patterns from log data and perform data validation.
[Regular Expressions - Real Python](https://realpython.com/regex-python/)

### 5. Dictionaries in Python:
Dictionaries in Python are unordered collections of key-value pairs, used to store and retrieve data based on keys. In this project, you can use dictionaries to store and manipulate data efficiently, such as counting occurrences of log entries or aggregating statistics.
[Dictionaries in Python - Real Python](https://realpython.com/python-dicts/)

### 6. Exception handling:
Exception handling in Python allows you to catch and handle errors or exceptions that occur during program execution. You can use `try`, `except`, and `finally` blocks to handle exceptions gracefully and prevent the program from crashing.
[Exception Handling in Python - Real Python](https://realpython.com/python-exceptions/)


By studying these concepts and utilizing the resources provided, you will be well-prepared to tackle the log parsing project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.


## Additional Resources:
- [Python Documentation](https://docs.python.org/3/)
- [Mock Technical Interview](https://youtu.be/5dRTK-_Bzd0)


### Requirements:
#### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`


### Tasks:
#### 0. Log parsing
[0-stats.py](./0-stats.py)
- Write a script that reads `stdin` line by line and computes metrics:
    - Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
    - After every 10 lines and/or a keyboard interruption (`CTRL + C`), print these statistics from the beginning:
        - Total file size: `File size: <total size>`
        - where `<total size>` is the sum of all previous `<file size>` (see input format above)
        - Number of lines by status code:
            - possible status codes are `200`, `301`, `400`, `401`, `403`, `404`, `405`, and `500`
            - if a status code doesn’t appear, don’t print anything for this status code
            - format: `<status code>: <number>`
            - status codes should be printed in ascending order

**Warning:** In this sample, you will have random value - it’s normal to not have the same output as this one.

```
alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
alexa@ubuntu:~/0x03-log_parsing$ 
```

**Repo:**
- GitHub repository: `alx-interview`
- Directory: `0x03-log_parsing`
- File: `0-stats.py`

---
## Author
- [GitHub - Nathanim Tadele](https://github.com/Nathanim1919)