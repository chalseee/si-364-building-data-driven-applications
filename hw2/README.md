# Homework 2 - SI 364 W18

### Deadline: January 28, 2018 at 11:59 PM

## To submit

Fork and clone this repository. Make edits, following the directions, commit them all, and then push your changes to your fork. Submit the link to your fork of the repository on GitHub to the Canvas assignment.

**Do not** change any file names. Make **sure** all your file names and label text are exactly as directed for grading. And **do not** make edits to this `README.md` file, even in your own fork (this is for a Git reason, which we will show you during a class session).

**If you have completed 100% of the homework,** your application should have the following routes, each of which should render the template listed here:

* `http://localhost:5000/artistform` -> `artistform.html`
* `http://localhost:5000/artistinfo` -> `artist_info.html`
* `http://localhost:5000/artistlinks` -> `artist_links.html`
* `http://localhost:5000/specific/song/<artist_name>` -> `specific_artist.html`
* `http://localhost:5000/album_entry` -> `album_entry.html`
* `http://localhost:5000/album_result` -> `album_data.html`

AND

* `http://localhost:5000/` -> should render **Hello world!** -- PROVIDED WITH ORIGINAL FILE
* `http://localhost:5000/user/<name>` -> should render **Hello {name}** -- PROVIDED WITH ORIGINAL FILE


## Instructions

This HW assignment comes in three parts, which build on one another.

They involve: using templates, writing templates with Jinja2 templating, debugging templates and view function decisions in a Flask application, and using WTForms.

### Part 1 (500 points)

Edit the `SI364_HW3.py` file inside the `HW3Part1` directory to add routes to the basic Flask application that will match the **provided** templates in the `templates` subdirectory inside the `HW3Part1` folder. (**Do not** change the name of this file.)

The templates that are provided for you are:

* `artist_info.html`
* `artist_links.html`
* `artistform.html`
* `specific_artist.html`

Check them out carefully (variables, actions, methods, etc) to determine how to write the view functions you need.

You will need to use the iTunes REST API for this again. Your parameters are laid out by the templates, and what you've already seen from this API. **Think:** What data do you know you need, based on each template? Given the context here, what does each view function need to *do*?

When you are done with this part of the HW, you should have the following four routes which render each of the corresponding templates with reasonable data:

* `http://localhost:5000/artistform` -> `artistform.html`
* `http://localhost:5000/artistinfo` -> `artist_info.html`
* `http://localhost:5000/artistlinks` -> `artist_links.html`
* `http://localhost:5000/specific/song/<artist_name>` -> `specific_artist.html`

Each of the templates should be rendered with actual data when those routes are reached when the Flask application runs.

Check out the action on forms, and the end-locations of links, in order to ensure that you send the correct data to templates and that the templates get the correct data!

You may edit the provided templates *only slightly*: **you may not edit their structure nor any variable names in them** to earn full credit. You should *not* need to do so in any significant way.

### Part 2 (300 points)

**Add a form to the application in `SI364W18_HW2.py`, using `WTForms` syntax. The class name should be `AlbumEntryForm`.**

The `AlbumEntryForm` should have the following fields:

* Text entry for an album name, whose label should be `Enter the name of an album:`, which should be **required**
* Radio buttons with options: 1,2,3 -- representing how much the user likes the album, whose label should be: `How much do you like this album? (1 low, 3 high)`, which should be **required**
* A submit button

**Then, add 2 more routes to the application:**

* `/album_entry`, which should render the WTForm you just created (note that there is a raw HTML form in one of the provided templates, but THIS should rely on your WTForms form). It should send data to a template called `album_entry.html` (see Part 3). The form should look pretty much [like this](https://www.dropbox.com/s/6mvt6d4b929vu0n/Screenshot%202018-01-15%2016.10.09.png?dl=0) **when you are done with Part 3.**

* `/album_result`, which should render the results of what was submitted to the `AlbumEntryForm`, [like this](https://www.dropbox.com/s/vqi7ybmkdh7ca1q/Screenshot%202018-01-15%2016.07.38.png?dl=0) **when you are done with Part 3.** It should send data to a template called `album_data.html` (see Part 3).

### Part 3 (200 points)

Add templates to the application, in the provided `templates/` directory, for those two routes.

You should be creating 2 template files:

* `album_entry.html`, which should use the data sent from the `/album_entry` route's view function
* `album_data.html`, which should use the data sent from the `/album_result` route's view function

## Finally

Check to make sure that each of the routes listed at the beginning of this README works correctly, and that each of the templates exist, all with the correct filenames.

If so, you're all set!

If you complete most but not all of this, that's OK, too. Commit and submit what you've got, and make sure that what you have got runs! We will not give partial credit for code that does not run.
