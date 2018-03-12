# Midterm Assignment - SI 364 W18

### Deadline: March 11, 2018 11:59 PM
### Total: 2000 points

**This application allows users to enter in their favorite actors and TV shows, and then view detailed information about those interests on different pages.**

### Overview of Application.
**If you have completed 100% of the homework,** your application should have the following routes, each of which should render the template listed here:

* **http://localhost:5000/ -> base.html** -- This is the homepage of the application.
* **http://localhost:5000/movies -> movies.html** -- This page allows a user to enter their favorite actor, and if their most popular movie isn't a duplicate, information about it will appear.
* **http://localhost:5000/actors -> actors.html** -- This page shows information about every actor that was input on the movies.html page.
* **http://localhost:5000/names -> name_example.html** -- This page shows all information that was submitted to the form on the homepage.
* **http://localhost:5000/tv_shows -> tv_shows.html** -- This page shows all non-duplicate information about TV shows that was submitted to the homepage.
* **404.html**: 404 error page.

### Instructions

#### Documentation Requirements (so we can grade the assignments)

* **Note:** See **To Submit** for submission instructions.
* Create a `README.md` file for your app that includes the full list of requirements from this page. The ones you have completed should be bolded. (You bold things in Markdown by using two asterisks, like this: `**This text would be bold** and this text would not be`)
* The `README.md` file should include a list of all of the routes that exist in the app and the names of the templates each one should render (e.g. `/form` -> `form.html`, like [the list we provided in the instructions for HW2](https://www.dropbox.com/s/3a83ykoz79tqn8r/Screenshot%202018-02-15%2013.27.52.png?dl=0)).
* The `README.md` file should contain at least 1 line of description of what your app is about or should do.

#### Code Requirements

**Note that many of these requirements go together!**

- **[x] Ensure that the `SI364midterm.py` file has all the setup (`app.config` values, import statements, code to run the app if that file is run, etc) necessary to run the Flask application, and the application runs correctly on `http://localhost:5000` (and the other routes you set up)
- [x] Add navigation in `base.html` with links (using `a href` tags) that lead to every other viewable page in the application. (e.g. in the lecture examples from the Feb 9 lecture, [like this](https://www.dropbox.com/s/hjcls4cfdkqwy84/Screenshot%202018-02-15%2013.26.32.png?dl=0) )
- [x] Ensure that all templates in the application inherit (using template inheritance, with `extends`) from `base.html` and include at least one additional `block`.
- [x] Include at least 2 additional template `.html` files we did not provide.
- [x] At least one additional template with a Jinja template for loop and at least one additional template with a Jinja template conditional.
    - These could be in the same template, and could be 1 of the 2 additional template files.
- [x] At least one errorhandler for a 404 error and a corresponding template.
- [x] At least one request to a REST API that is based on data submitted in a WTForm.
- [x] At least one additional (not provided) WTForm that sends data with a `GET` request to a new page.
- [x] At least one additional (not provided) WTForm that sends data with a `POST` request to the *same* page.
- [x] At least one custom validator for a field in a WTForm.
- [x] At least 2 additional model classes.
- [x] Have a one:many relationship that works properly built between 2 of your models.
- [x] Successfully save data to each table.
- [x] Successfully query data from each of your models (so query at least one column, or all data, from every database table you have a model for).
- [x] Query data using an `.all()` method in at least one view function and send the results of that query to a template.
- [x] Include at least one use of `redirect`. (HINT: This should probably happen in the view function where data is posted...)
- [x] Include at least one use of `url_for`. (HINT: This could happen where you render a form...)
- [x] Have at least 3 view functions that are not included with the code we have provided. (But you may have more! *Make sure you include ALL view functions in the app in the documentation and ALL pages in the app in the navigation links of `base.html`.*)**

### Additional Requirements for an additional 200 points (to reach 100%) -- an app with extra functionality!

* **(100 points) Include an *additional* model class (to make at least 4 total in the application) with at least 3 columns. Save data to it AND query data from it; use the data you query in a view-function, and as a result of querying that data, something should show up in a view. (The data itself should show up, OR the result of a request made with the data should show up.)

* (100 points) Write code in your Python file that will allow a user to submit duplicate data to a form, but will *not* save duplicate data (like the same user should not be able to submit the exact same tweet text for HW3).**
