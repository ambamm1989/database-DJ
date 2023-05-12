### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

  PostgreSQL is an open source object-relational database management system (ORDBMS) with an emphasis on extensibility and standards compliance. It can handle workloads ranging from small single-machine applications to large Internet-facing applications with many concurrent users. Recent versions also provide replication of the database itself for security and scalability. 

- What is the difference between SQL and PostgreSQL?
  
    SQL is a language for querying databases. PostgreSQL is a database management system that uses SQL as its language.

- In `psql`, how do you connect to a database?
  
    `\c <database_name>`

- What is the difference between `HAVING` and `WHERE`?

    `WHERE` is used to filter rows before grouping. `HAVING` is used to filter rows after grouping.

- What is the difference between an `INNER` and `OUTER` join?

    `INNER` join returns rows when there is at least one match in both tables. `OUTER` join returns rows when there is at least one match in one of the tables.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

    `LEFT OUTER` join returns all rows from the left table, even if there are no matches in the right table. `RIGHT OUTER` join returns all rows from the right table, even if there are no matches in the left table.

- What is an ORM? What do they do?

    ORM stands for Object-Relational Mapping. It is a technique for converting data between incompatible type systems using object-oriented programming languages.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

    AJAX is a technique for creating interactive web applications by using JavaScript to send and receive data from a web server asynchronously. `requests` is a Python library for making HTTP requests.

- What is CSRF? What is the purpose of the CSRF token?

    CSRF stands for Cross-Site Request Forgery. It is an attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated. The purpose of the CSRF token is to prevent CSRF attacks.

- What is the purpose of `form.hidden_tag()`?

    `form.hidden_tag()` is used to generate a hidden field that includes a token that Flask-WTF uses to protect against CSRF attacks.
