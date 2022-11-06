# Manuel Testing

## Bugs and Fixes During the Development Process

Below is a list of bugs and fixes found while creating a feature. You can find other bugs as bug tickets in [JIRA](https://dnlbowers.atlassian.net/browse/PVS-47?filter=-2&jql=project%20%3D%20PVS%20AND%20issuetype%20%3D%20Bug%20AND%20reporter%20in%20(currentUser())%20order%20by%20created%20DESC). The Jira tickets are bugs found after I concluded the sprint including this feature because during the feature creation I missed the bugs.

* Issue - When installing dj_database_url via pip install command django automatically upgraded to version 4.1.1
* Cause - Only had Django 3.2 installed. The latest version of this library requires Django a higher version of 3.2 to be installed.
* Solution - Installed the latest version of Django 3.2 with pip install django==3.2.14 to ensure I am developing with the LTS version of Django.

* Issue - When trying to paginate my products view all products were displayed on the same page instead of being paginated.
* Cause - The first issue here was the lack of ordering in the model. The second issue was using the wrong function in my class view to retrieve the context data.
* Solution - First I added ordering to the AllProducts model to order the record by ID. Second I replaced the get_context_data function with get_context_object_name, this function then took the model fed into the class view and and returned the context name as products.

* Issue - When trying to use AllProducts in the ProductDetails view, I was getting an error saying that this model had not object attribute. The odd thing was that in shell I was able to use a for loop to iterate through the model and its child models.
* Cause - There seems to be a know issue where the base model doesn't work when iterating via the views when using the django-polymorphic library.
* Solution - The solution for this was a work around. I collected al the child models into and array and then iterated through the array in the view to find the correct ID passed in the URL. The down side of this is when scaling the site up later, it created a extra manual process to add the child models to the array if any new sub types of products are added.

* Issue - when one product is return from the search query, the product car is thinner than normal
* Cause - I am not sure why this is happening. I think it has something to do with the way the product card is being rendered using the bootstrap class.
* Solution - Adding a min-width to the card class resolved the issue.

* Issue - There are two qty selectors on the cart and they are not synced. this means if the screen changes size the second qty selector will not reflect the initial one
* Cause - There is no link between the two qty selectors on the cart page.
* Solution - Adding a variable to the increase/decrease click event to group all qty inputs for the same product together

* Issue - checkout form was not submitted (clearing to a new form), and a error was present saying the payment could not be processed even though stripe was registering the payment as successful
* Cause - I could see in the browser console that the payment intent was successful but there was a second request to the server that was failing. The stripe logs showed that the payment intend had already been processed and this second attempt was preventing the form submission from completing. From console logging the relevant part of the code I could see that using the query submit() was actually submitting the form despite having the preventDefault() function in place.
* Solution - Changing the query submit() to vanilla JS using "addEventListener" for "submit" resolved the issue.

## to fix later

* Issue - When deleting something from the cart, the first item in the list get deleted and not the item selected
* Cause - check the JS
* Solution -

* issue - Floating footer when content not enough to push it down

* issue - basket icon always blue(should only be blue when there is something in the basket) and also add the product count to tool tip
