# Manuel Testing

## Bugs and Fixes During the Development Process

Below is a list of bugs and fixes found while creating a feature. You can find other bugs as bug tickets in [JIRA]()**Link to issues to be added**. The Jira tickets are bugs found after I concluded the sprint including this feature because during the feature creation I missed the bugs.

* Issue - When installing dj_database_url via pip install command django automatically upgraded to version 4.1.1
* Cause - Only had Django 3.2 installed. The latest version of this library requires Django a higher version of 3.2 to be installed.
* Solution - Installed the latest version of Django 3.2 with pip install django==3.2.14 to ensure I am developing with the LTS version of Django.

* Issue - When trying to paginate my products view all products were displayed on the same page instead of being paginated.
* Cause - The first issue here was the lack of ordering in the model. The second issue was using the wrong function in my class view to retrieve the context data.
* Solution - First I added ordering to the AllProducts model to order the record by ID. Second I replaced the get_context_data function with get_context_object_name, this function then took the model fed into the class view and and returned the context name as products.
* 