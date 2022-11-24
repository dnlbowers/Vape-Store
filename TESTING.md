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
* Solution - Changing the query submit() to vanilla JS using "addEventListener" for "submit" resolved the issue. Although I later found this was causing further issues with the form submission when testing the loading indicator via a 3ds test payment. I then decide to use a click event and discovered that trying to combine JS and jquery in a single line was n't working as it should so I decided to write only Jquery with a reference to the button and the click() function.

Instead of documenting here from here out I decided it was better to solely raise a bug ticket in [JIRA](https://dnlbowers.atlassian.net/browse/PVS-47?filter=10005). I was finding myself getting fixated on bugs which were preventing my completing the over all purpose of the sprint in a timely manner. I decided to raise the bugs and move on to the next feature only to return in the same iteration later if there was excess time.

## Testing(post development phase)

I began the project writing automated tests for everything, however I soon realized this was slowing me down and I needed to focus on getting the project completed. You will find automated test files in the home and product apps. however the remaining apps do not have automated tests. I have decided to write manual tests for the remaining apps and features by testing each user story individually.

### Manual Testing of User Stories

For the following I will be skipping type of use i.e. "As a shopper I can" and list the latter part of the story as a heading.

#### Epic 1

Most of this epic were tasks for the development phase and therefore the testing is the working of the overall site. The was the one story which tests all tasks as one.

|passed | **Access a live url** so that I can **use the site on any device**.
|:---:|:---|
|&check;| Can access the site via the deployed url on desktop.
|&check;| Can access the site via the deployed url on mobile.
|&check;| Can access the site via the deployed url on tablet.
|&check;| All images and styles are in tacked and as expected.

#### Epic 2

|passed | .**Clearly identity the sites purpose upon visiting** so that I can **determine if the site is what I am looking for.**
|:---:|:---|
|&check;| The site has a clear purpose and is easy to navigate.

|passed | **View a list of products** so that I can **select some to purchase.**
|:---:|:---|
|&check;| The site has a list of products.
|&check;| The list of products is paginated.
|&check;| The list of products is ordered by ID by default.
|&check;| The list of products can be ordered by name ascending and descending.
|&check;| The list of products can be ordered by price ascending and descending.
|&check;| The list of products can be ordered by rating ascending and descending.
|&check;| The list of products can be filter to show only those that have an active sale.
|&check;| The list of products show stock status i.e. in stock/out of stock.
|&check;| Add to cart button works as expected on both the all products page and the product details page.
|&check;| User cannot add more items to their cart than are in stock.
|&check;| When and item is out of stock the add to cart button is disabled.

|passed | **View individual product details** so that I can **identify the price, description, detailed reviews, and product image enabling me to compare how the product differs from other items.**
|:---:|:---|
|&check;| The site has a product details page.
|&check;| The product details page shows the product image.
|&check;| The product details page shows the product name.
|&check;| The product details page shows the product price.
|&check;| The product details page shows the sale price if item has sale.
|&check;| The product details page shows the product description.
|&check;| The product details page shows the product rating.
|&check;| The product details page shows the product reviews.
|&check;| The product details page shows review form if no reviews already..
|&check;| The product details page shows the product stock status.
|&check;| The product details page shows the product quantity selector.
|&check;| The product details page shows the product add to cart button.
|&check;| User is unable to add more items to the cart than is currently in stock.

|passed | **View the total of my purchases at any time** so that I can **see and review how much I am spending at any time whilst building an order.**
|:---:|:---|
|&check;| The site has a cart page.
|&check;| The cart page/preview shows the product image.
|&check;| The cart page/preview shows the product name.
|&check;| The cart page/preview shows the product price.
|&check;| The cart page/preview shows current quantity in the cart.
|&check;| Cart preview shows from any page when item is added to it.
|&check;| The cart page shows the product quantity selector and the user can update their order quantity.
|&check;| The cart page/preview shows the cart total.
|&check;| The cart page/preview shows amount left to spend to get free delivery.
|&check;| The cart page shows the delivery cost and grand total.
|&check;| The cart page allows the user to completely remove and item from their cart and updates the cart total.
|&check;| When the quantity is updated in the users cart the cart total updates accurately.

|passed | **Leave a review** so that I can **share my opinion of a product and leave a star rating.**
|:---:|:---|
|&check;| The site has a review form.
|&check;| The review form has a title field.
|&check;| The review form has a rating field.
|&check;| The review form has a body field.
|&check;| When no reviews a review form is shown in place on the products detail page.
|&check;| When a review is submitted the review is added to the product detail page.
|&check;| User cannot enter a value greater than 5 for the rating field.
|&check;| User cannot enter a value less than 1 for the rating field.
|&check;| User cannot submit a review without a title.
|&check;| User cannot submit a review without a rating.
|&check;| Over all rating is calculated and displayed on the product detail page/product card .
