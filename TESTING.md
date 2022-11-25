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

#### **EPIC 1 - Set up and Deployment:**

Most of this epic were tasks for the development phase and therefore the testing is the working of the overall site. The was the one story which tests all tasks as one.

|passed | **Access a live url** so that I can **use the site on any device**.
|:---:|:---|
|&check;| Can access the site via the deployed url on desktop.
|&check;| Can access the site via the deployed url on mobile.
|&check;| Can access the site via the deployed url on tablet.
|&check;| All images and styles are in tacked and as expected.

#### **EPIC 2 - Viewing and Navigation:**

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
|&check;| Over all rating is calculated and displayed on the product detail page/product card.
|&check;| Over all rating is adjusted when review is deleted or edited.
|&check;| Author of review can edit their review.
|&check;| Author of review can delete their review.
|&check;| Author of review can not edit or delete another users review.
|&check;| success message is displayed when a review is submitted.

|passed | **View reviews of a product** so that I can **see what other people think of a product.**
|:---:|:---|
|&check;| The site has a review section on the product detail page.
|&check;| The review section shows the review title.
|&check;| The review heading shows the review rating.
|&check;| The review heading shows a preview of the the review body.
|&check;| The review heading shows the review author.
|&check;| The review heading shows the review date.
|&check;| The review edit/delete buttons only show to the author and super users.
|&check;| Accordion opens and closes when clicked.
|&check;| Accordion only allows for one review to be expanded at a time to save display space.
|&check;| If no reviews then an inline form is shown in place of the accordion.
|&check;| If reviews then there is a button above for the user to be able to add a review.

|passed | **Identify any promotions that are available** so that I can **take advantage of them and obtain the best value for money possible.**
|:---:|:---|
|&check;| The site has a promotions page.
|&check;| The promotions page shows only items that have sale active.

|passed | **See clearly when something goes wrong on the site** so that I can **correct any errors and continue with my purchase.**
|:---:|:---|
|&check;| The site has a 404 page active when url unknown.
|&check;| The site has a 500 page active when server error.
|&check;| Relevant feedback is displayed as a toast message when the user cannot perform an action.

|passed | * ... **See a pleasantly styled and easy to navigate site** so that I can **enjoy the experience of using the site.**
|:---:|:---|
| | The site has a pleasant colour scheme.
| | The site has a pleasant font scheme.
| | The site has a pleasant layout.
| | The site has a pleasant navigation.
| | The site has a pleasant footer.
| | The site has a pleasant header.
| | The site has a pleasant product card.
| | The site has a pleasant product detail page.
| | The site has a pleasant cart page.
| | The site has a pleasant checkout page.
| | The site has a pleasant promotions page.
| | Everything is aligned and spaced correctly.

|passed | **Easily contact the store owner** so that I can **ask questions about the products or the site.**
|:---:|:---|
|&check;| The site has a contact page.
|&check;| Contact form cannot be submitted with required fields blank.
|&check;| Contact form cannot be submitted with invalid email address.
|&check;| Contact form submits a message to the database.
|&check;| Message can be read in the admin panel.
|&check;| Success message is shown to the user when message is submitted.
|&check;| Notes can be added to the message in the admin panel.
|&check;| Message can be updated as done.
|&check;| pending reply is automatically ticked and can be un-ticked to indicate the message is complete
|&check;| Message can be deleted.
|&check;| Messages can be filtered by "marked as done" and "pending reply".
|&check;| Messages can be filtered by "all", "today", "this week", "this month" and "this year".

|passed | **All site users are of legal age to purchase vape supplies** so that I can **comply with the law.**
|:---:|:---|
|&check;| On first visit to the site the user is asked to confirm they are over 18.
|&check;| If the user is under 18 they blocked from viewing the site until they confirm they are of legal age.
|&check;| Cookie is left upon the user confirming they are of legal age.
|&check;| Pop up appears on every page until the user confirms they are of legal age.
|&check;| Cookie has an expiry date of one day.

#### **EPIC 3 - Registration and User Accounts:**

|passed | **Register for an account** so that I can **save my personal details, view my order history online.**
|:---:|:---|
|&check;| The site has a registration page.
|&check;| Users can not register with an email address that is already in use.
|&check;| Users can successfully register for the site
|&check;| Users can not register with a username that is already in use.
|&check;| Users can not register with a password that is similar to their user name.
|&check;| Users can not register with a password that is similar to their email address.
|&check;| Users can not register with a password that is too short.
|&check;| Errors are displayed to the user if any of the above are attempted.
|&check;| Success message is displayed to the user if registration is successful.
|&check;| User sees message to verify their email.
|&check;| User can not login until they have verified their email.
|&check;| Verification email is sent to the user.
|&check;| Verification email contains a link to verify the users email.
|&check;| Once verified user can log in with their username or email.
|&check;| Users is redirected to the login in page once email is verified.

|passed | **Easily login or logout at any time** so that I can **access my personal account information and protect it from unauthorized viewing on shared devices.**
|:---:|:---|
|&check;| Log in/out options is visible on all pages under the my account dropdown.
|&check;| Once logged out personal information is no longer visible.
|&check;| Once logged In the my account options change to reveal a profile link.
|&check;| Once logged in/out the user is redirected to the home page.
|&check;| User receives a success message when they log in/out.

|passed | ...**Save my personal details to my profile from the checkout page** so that I **don’t have to enter them every time I make a purchase.**
|:---:|:---|
|&check;| The site has a profile page.
|&check;| The profile page has a form to update the users details.
|&check;| Checkout form takes the information available in the profile for the checkout process
|&check;| Details from checkout save if save info box checked
|&check;| Details from checkout do not save if save info box not checked
|&check;| Shipping address on previous order unaffected by updating details.

|passed | **Amend my personal details from my profile** so that I can **update information should there be any changes.**
|:---:|:---|
|&check;| User can update their details on the profile page.
|&check;| Appropriate error messages are shown if the user enters invalid details.
|&check;| Success message is shown if the user updates their details successfully.
|&check;| Shipping address on previous order unaffected by updating details.

|passed | **Recover my password in case I forget it** so that I can **regain access to my account in the event I lose my password.**
|:---:|:---|
|&check;| The site has a password reset page.
|&check;| The password reset page has a form to enter the users email address.
|&check;| Email is sent with password reset token.
|&check;| Link in email takes user to password reset page.
|&check;| Password reset page has a form to enter the new password.
|&check;| User get a success message once password has been reset
|&check;| User can now log in with their new password.

|passed | **Receive an email confirmation upon registration** so that I can **confirm the registration process worked correctly.**
|:---:|:---|
|&check;| Email sent upon registration asking for the user to verify there email address.

#### **EPIC 4 - Sorting and Searching:**

|passed | **Sort the list of available products** so that I can **view them in different orders. and find the highest/lowest rating/prices and sort alphabetically to aid in finding the most suitable products to suit my needs.**
|:---:|:---|
|&check;| Products can be sorted by name in ascending order.
|&check;| Products can be sorted by name in descending order.
|&check;| Products can be sorted by price in ascending order.
|&check;| Products can be sorted by price in descending order.
|&check;| Products can be sorted by rating in ascending order.
|&check;| Products can be sorted by rating in descending order.

|passed | **Search for a product by name or content in the product description** so that I can **find a specific product I am looking for.**
|:---:|:---|
|&check;| Search bar is visible on all pages.
|&check;| Search returns results based on the search term.
|&check;| Search query checks product name and description.
|&check;| search terms is displayed above the search results.
|&check;| Number of products returned is displayed above the search results.

|passed | **View a list of products in a specific category** so that I can **view all products in that category.**
|:---:|:---|
|&check;| Products can be filtered by category via the navbar links.
|&check;| Products can be filtered by sub-category via the navbar links.

#### **EPIC 5 - Purchasing and Checkout:**

|passed | **Select a quantity of a product** so that I can **buy the required amount of the product.**
|:---:|:---|
|&check;| Quantity can be selected on the product page.
|&check;| Quantity can be selected on the product detail page.
|&check;| User cannot set the quantity selector to more than the in stock level
|&check;| User cannot set the quantity selector to less than 1
|&check;| User can set the quantity selector to the in stock level
|&check;| User can set the quantity selector to 1
|&check;| User can use the plus and minus buttons to select the quantity.
|&check;| User cannot add a quantity of 0 to the cart.
|&check;| User cannot add more than the stock level to their cart.
|&check;| server side checks prevent the user from adding more than the stock level to their cart even if they change the input max value in the dev tools.
|&check;| User receives message if item added to cart.
|&check;| User receives message if if new quantity selected takes the cart total number of items over the stock level.
|&check;| Quantity selector is disabled if the product is out of stock.

|passed | **View items in my bag to be purchased** so that I can **identify the total cost of my purchases before checkout.**
|:---:|:---|
|&check;| The site has a shopping cart page.
|&check;| The shopping cart page has a list of all the items in the users cart.
|&check;| The shopping cart page has a total price for all the items in the users cart.
|&check;| The shopping cart page has a button to proceed to checkout.
|&check;| The shopping cart page has a button to remove items from the cart.

|passed | **Adjust the quantity of individual items in my bag** so that I can **easily make changes to my bag.**
|:---:|:---|
|&check;| The quantity of each item in the cart can be changed and updated from the cart page.
|&check;| Total recalculates each time the quantity is changed.
|&check;| User is shown success/error message when state changed in cart.
|&check;| User cannot set the quantity selector to more than the in stock level
|&check;| User cannot set the quantity selector to less than 1
|&check;| User can set the quantity selector to the in stock level.
|&check;| User can set the quantity selector to 1.
|&check;| User can use the plus and minus buttons to select the quantity.
|&check;| User cannot add a quantity of 0 to the cart.

|passed | **Easily enter my payment information** so that I can **checkout quickly with no hassles by using information previously stored in the system.**
|:---:|:---|
|&check;| The site has a checkout page.
|&check;| The checkout page has a form to enter the users payment details.
|&check;| The checkout page has a form to enter the users shipping details.
|&check;| Payments are handled by Stripe.
|&check;| The checkout page has a button to complete the order.
|&check;| The checkout page has a button to cancel the order and return to the shopping cart.
|&check;| The checkout page has a button to save the users details for future use.
|&check;| If checked the details from the checkout form are saved to the users profile.
|&check;| If exists the users saved details are pre-filled in the checkout form.
|&check;| If the user has saved details the checkbox is unchecked by default.

|passed | **View an order confirmation after checkout** so that I can **verify that I haven’t made any mistakes.**
|:---:|:---|
|&check;| The site has a checkout success page.
|&check;| The checkout success page has a message to confirm the order was successful.
|&check;| The checkout success page has a button to return to the home page.|
|&check;| The checkout success page has a button to take the user to the special offers page.
|&check;| Email is sent to the user confirming the order.
|&check;| order is available to the customer who made the order in their order history page.
|&check;| checkout success page for an order made by a registered user can only be seen by that user from the profile.
|&check;| once an order is confirmed on screen the order confirmation can only be revisited from a registered users profile/ non registered users cannot revisit the check out success page.

|passed | **Receive an email confirmation after checking out** so that I can **keep a record of my purchases.**
|:---:|:---|
|&check;| Email is sent to the user confirming the order.
|&check;| Email contains the order number.
|&check;| Email contains the order total.
|&check;| Email contains the order date.
|&check;| Email contains the delivery address.
|&check;| Email contains the delivery cost.
|&check;| Email has a contact email address for assistance.

|passed | **View my order history** so that I can **see the orders I have made previously.**
|:---:|:---|
|&check;| The site has an order history page for registered users.
|&check;| The order history page has a list of all the orders made by the user.
|&check;| The order history page has a link to view the order details.
|&check;| The order history page has a link to return to their profile page.
|&check;| The order history page can only be accessed by the user who made the order.
|&check;| Unregistered users cannot access their previous orders confirmation.
|&check;| Appropriate error message is shown if a user tries to access an order confirmation that is not theirs.
|&check;| Appropriate error message is shown if an unregistered user tries to get back to their order confirmation using a url.

|passed | **Access the checkout page** so that I can **review my order whilst entering my payment/shipping details**
|:---:|:---|
|&check;| The site has a checkout page.
|&check;| The checkout page has a form to enter the users payment details.
|&check;| The checkout page has a form to enter the users shipping details.
|&check;| The checkout page has a button to complete the order.
|&check;| The checkout page has a button to cancel the order and return to the shopping cart.
|&check;| The checkout page has a button to save the users details for future use.
|&check;| If checked the details from the checkout form are saved to the users profile.
|&check;| If exists the users saved details are pre-filled in the checkout form.
|&check;| Saved details the checkbox is unchecked by default.
|&check;| Guest users are invited to register/sign in and warned that they cannot view their order history online without registering.

|passed | **securely submit my payment details** so that I can **rest assured my financial information is safe**
|:---:|:---|
|&check;| Stripe payment system is used.
|&check;| Stripe payment system is PCI compliant.

#### **EPIC 6 - Admin and Store Management:**

|passed | **Add a product** so that I can **add new products to the store.**
|:---:|:---|
|&check;| Product can be added via the admin panel and is visible in the store front end.
|&check;| Newly added item had full functionality of pre existing items.

|passed | **Edit a product** so that I can **update the details of a product.**
|:---:|:---|
|&check;| Product can be edited via the admin panel and is visible in the store front end.
|&check;| Quick edited can be made from the front end only by super users.

|passed | **Delete a product** so that I can **remove products that are no longer for sale.**
|:---:|:---|
|&check;| Product can be deleted via the admin panel and is no longer visible in the store front end.
|&check;| Quick delete can be made from the front end only by super users.
|&check;| product cannot be deleted by non superuser using the url.

|passed | **Add a promotion** so that I can **add new promotions to the store.**
|:---:|:---|
|&check;| Promotion can be added via the admin panel and is visible in the store front end.
|&check;| Start sale function in the admin panel set has sale to true.
|&check;| Remove sale function in the admin panel set has sale to false.
|&check;| 10% discount function works to reduce the discounted price to 10% less.
|&check;| 20% discount function works to reduce the discounted price to 20% less.
|&check;| 30% discount function works to reduce the discounted price to 30% less.
|&check;| 40% discount function works to reduce the discounted price to 40% less.
|&check;| 50% discount function works to reduce the discounted price to 50% less.
|&check;| Price comes from discounted price when has sale is true.
|&check;| Price comes from RRP when has sale is false.
|&check;| Sale actions taken in the back end are visible on the front end via product cards and details pages.

|passed | **manually manage the stock levels** so that I can **input received purchase orders and ensure that the stock levels are accurate in case of discrepancies or damages.**
|:---:|:---|
|&check;| Stock levels can be manually adjusted via the admin panel.
|&check;| Stock levels can be manually adjusted via the front end.
|&check;| Stock levels are deducted upon a successful purchase.
|&check;| Item set to out of stock if stock level is 0.
|&check;| If order is deleted, stock is returned into the system.
|&check;| If order is amended from admin panel, stock is also adjusted accordingly.
|&check;| Order cannot be amended to have more products than are in stock..

#### **EPIC 7 - Product Reviews:**

|passed | **Add a review** so that I can **share my thoughts on a product.**
|:---:|:---|
|&check;| The site has a review form.
|&check;| When there are no reviews for a product, the review form is displayed on the product details page.
|&check;| When there are reviews they are displayed in an accordion with all relevant details visible.
|&check;| When there are reviews the is a button to add a review.
|&check;| The leave review takes the user to the review form page with the correct product name in the title and image displayed.
|&check;| The review form has a field to enter the review title, rating, and text.
|&check;| The review form has a button to submit the review.
|&check;| Rating cannot be above 5 or below 1.
|&check;| Rating is a number field.
|&check;| Once successfully submitted the review is visible on the product details page.
|&check;| All reviews can be edited by a superuser.
|&check;| All reviews can be deleted by a superuser.
|&check;| All reviews can be edited by the user who created the review.
|&check;| All reviews can be deleted by the user who created the review.
|&check;| Over all rating is re-calculated when a review is edited or deleted.
|&check;| Over all rating is re-calculated when a review is added.
|&check;| Review cannot be edited or deleted by a user who did not create the review.

|passed | **Edit a review** so that I can **update my thoughts on a product.**

