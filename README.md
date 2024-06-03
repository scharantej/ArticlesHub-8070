## Flask Application Design for Recent Newspaper Articles Website

### HTML Files

- **index.html**:
   - The main landing page of the website.
   - Displays a list of recent newspaper articles.
   - Provides a search bar to search for articles.

- **article.html**:
   - Displays the content of a specific newspaper article.
   - Includes the article's title, author, publication date, and text.

### Routes

**1. GET /**
- Purpose: Display the index page with a list of recent newspaper articles.
- Template: index.html

**2. POST /search**
- Purpose: Handle search functionality and display search results.
- Receives search query as a parameter.
- Filters articles based on the search query.
- Returns the index page with the filtered list of articles.

**3. GET /article/<int:id>**
- Purpose: Display the content of a specific newspaper article.
- Receives the article's ID as a parameter.
- Queries the database to fetch the article with the given ID.
- Returns the article.html template with the article's data.

**4. GET /add-article**
- Purpose: Display a form for adding a new newspaper article.
- Template: add-article.html

**5. POST /add-article**
- Purpose: Handle the submission of the new article form.
- Receives the article's title, author, publication date, and text as parameters.
- Validates the input data and inserts the new article into the database.
- Redirects to the index page.