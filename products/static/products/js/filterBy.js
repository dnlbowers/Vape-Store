document.addEventListener("DOMContentLoaded", function () {
    
    /**
     * Changes the method of sorting products on the products page
     */
    $('#sorting-menu').change(function() {
        // get the selected menu option value
        const menuChoiceValue = $(this).val();

        // Get the current URL
        const pageUrl = new URL(window.location);
        
        if(menuChoiceValue != 'default') {
                            
            // set the ordering parameters in the URL
            pageUrl.searchParams.set('ordering', menuChoiceValue);

            // redirect to the new URL which includes the above parameter
            window.location.replace(pageUrl);

        } else {

            // remove the ordering query parameters from the URL
            pageUrl.searchParams.delete('ordering');

            window.location.replace(pageUrl);
        }

    });
});
