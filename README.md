1. Install flask and requests

In terminal, run pip install flask-restx. After flasks finishes installing, run pip install requests. This will allow the user to run the microservice locally.

2. Requesting data

To request data, use requests.get() to connect to the localhost. After the '/' state the route to connect to based on the microservice program.

For eaxmple, to connect to the 'book' route. Run requests.get(https://localhost:5000/book) or requests.get(https://127.0.0.1:5000/book). Both connect to the local host and will requests data from the microservice.

3. Receiving data

To receive data, assign the requests.get() to a variable.

Following the previous example call, running response = requests.get(https://localhost:5000/book), will assign the JSON containing the book information to the 'response' variable.

An example of printing the JSON would be print(response.text).

4. UML Sequence Diagram

!["UML Diagram"] (./uml.jpg)
