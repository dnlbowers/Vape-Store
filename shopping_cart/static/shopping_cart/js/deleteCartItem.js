document.addEventListener("DOMContentLoaded", () => {
    
    /**
     * Retrieves cookie and saves the contained csrf token to a variable for later use
     * Code Taken from Django docs https://docs.djangoproject.com/en/3.2/ref/csrf/
     */
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    const csrfToken = getCookie('csrftoken');


    /**
    * This function is used to delete a product from the cart.
    */
    $('.delete-btn').click(function(e) {

        e.preventDefault();
        let productId = $(this).data('remove-id');
        const url = `/shoppingcart/deleteitem/${productId}/`;
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': csrfToken,
                'product_id': productId,
            },
            success: function (data) {
                location.reload();
            },
            error: function (data) {
                console.log(data);
            }
        });
    });
});