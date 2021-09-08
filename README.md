# python-flask-test
<p>This app will display the contents present in the requested file. By default, this will display File-1 contents as Homepage.</p>

LOCAL HOST URL : http://127.0.0.1:5000/

<hr>

<h2>Available File Requests</h2>

Below are the requests available from this App.

| S. No | Categories        | Endpoints     |
| ----- | -----------       | -----------   |
| 0     | Homepage          | /             |
| 1     | File 1 Contents   | /file1        |
| 2     | File 2 Contents   | /file2        |
| 3     | File 3 Contents   | /file3        |
| 4     | File 4 Contents   | /file4        |

<hr>

<h2>Query Names</h2>

These query names are optional and are used to filter the file contents based on our requirements.

| S. No | Query Name    | Description                |
| ----- | -----------   | ---------------------- |
| 1     | start-line    | Start of the line         |
| 2     | end-line      | End of the line        |


<hr>


<h2>Installation and Setup</h2>

All dependencies are listed in _requirements.txt_ file.

1. To install dependencies, run -

    ```bash
    $ pip install -r requirements.txt
    ```



2. Start the app server - 
    ```bash
    $ python app.py
    ```
<hr>