document.addEventListener("DOMContentLoaded", function () {
    
    /**
    * Taken from boutique ado to handle a change 
    * of product image on the edit form page
    */
    $('#new-image').change(function () {
        var file = $('#new-image')[0].files[0];
        $('#filename').text(`Image will be set to: ${file.name}`);
    });     
});