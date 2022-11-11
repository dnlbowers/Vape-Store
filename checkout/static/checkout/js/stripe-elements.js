/**Adapted from stripe card element docs https://stripe.com/docs/payments/card-element?client=html and
/ https://stripe.com/docs/payments/accept-card-payments?platform=web&ui=elements using the boutique ado
/ project as a guide to combine  and adapt them
*/

// Stripe related references
const stripePublicKeyRef = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecretRef = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripePublicKeyRef);
const elements = stripe.elements();

// Payment form references
const errorDivRef = $("#card-errors");
const payNowBtnRef = $("#pay-now-btn");

// Loading indicator references
const loadingSpinnerRef = $("#spinner");
const loadingOverlayRef = $("#loading-overlay");
const payNowBtnTxtRef = $("#pay-now-btn-txt");


const style = {
    base: {
    color: "#000",
    fontFamily: 'Arial, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
        color: "#aab7c4"
    }
    },
    invalid: {
    fontFamily: 'Arial, sans-serif',
    color: "#dc3545",
    iconColor: "#dc3545"
    }
};

const card = elements.create("card", { style: style });

// Stripe injects an iframe into the DOM
card.mount("#card-element");

// handle realtime validation errors on the card element
card.on('change', (event) => {
    
    if (event.error) {

        errorContent = getErrorMessageHtml(event)
        $(errorDivRef).html(errorContent);

    } else {

        errorDivRef.textContent = '';

    }
        
});


const getErrorMessageHtml = (event) => {
    /**
     * Returns the HTML for an error message
     * with error message text from event.error.message
     */
    return `
    <span role="alert">
    <i class="fa-solid fa-triangle-exclamation fa-sm"></i>
    </span>
    <span>${event.error.message}</span>
    `;
};

let paymentForm = document.getElementById('payment-form');

paymentForm.addEventListener('submit', (event) => {
    /**
    *Prevent default form submission, disables the pay now button
    * and calls payWithCard function to handle the payment request
    */
    event.preventDefault();
    
    payWithCard(stripe, card, clientSecretRef);
});


let payWithCard = (stripe, card, clientSecret) => {
    /**
     * Calls stripe.confirmCardPayment to complete the payment
     * If the card requires authentication Stripe shows a modal to
     * prompt the user to enter authentication details without leaving the page
     */
    
    loading(true); 
    
    let saveInfo = Boolean($('#id_save_info').attr('checked'));
    const crsfToken = $("input[name='csrfmiddlewaretoken']").val();

    const postCacheData = {
        "csrfmiddlewaretoken": crsfToken,
        "client_secret": clientSecret,
        "save_info": saveInfo,
    };

    const url = "/checkout/cache_checkout_data/";

    $.post(url, postCacheData).done( () => {
        
        stripe.confirmCardPayment(clientSecret, {
            
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(paymentForm.full_name.value),
                    phone: $.trim(paymentForm.phone_number.value),
                    email: $.trim(paymentForm.email.value),
                    address: {
                        line1: $.trim(paymentForm.street_address1.value),
                        line2: $.trim(paymentForm.street_address2.value),
                        city: $.trim(paymentForm.town_or_city.value),
                        country: $.trim(paymentForm.country.value),
                        state: $.trim(paymentForm.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(paymentForm.full_name.value),
                phone: $.trim(paymentForm.phone_number.value),
                address: {
                    line1: $.trim(paymentForm.street_address1.value),
                    line2: $.trim(paymentForm.street_address2.value),
                    city: $.trim(paymentForm.town_or_city.value),
                    country: $.trim(paymentForm.country.value),
                    postal_code: $.trim(paymentForm.postcode.value),
                    state: $.trim(paymentForm.county.value),
                }
            }                    
        })
        .then( result => {
            if (result.error) {
    
                loading(false)
                errorContent = getErrorMessageHtml(result)
                $(errorDivRef).html(errorContent);
    
            } else {
                
                if (result.paymentIntent.status === "succeeded") {
    
                    paymentForm.submit()
    
                }
            };
        })
    }).fail(() => {

        // just reload the page, the error will be in django messages
        location.reload();

    });
        
};


let loading = isLoading => {
    /**
     * Shows or hides the loading overlay with a loading spinner
    */
    if (isLoading) {
        
        payNowBtnRef.attr("disabled", true);
        loadingOverlayRef.removeClass("d-none");
        card.update({ "disabled": true });
        payNowBtnTxtRef.addClass("d-none");
        loadingSpinnerRef.removeClass("d-none");

    } else {

        loadingSpinnerRef.addClass("d-none");
        payNowBtnTxtRef.removeClass("d-none");
        card.update({ "disabled": false });
        payNowBtnRef.attr("disabled", false);
        loadingOverlayRef.addClass("d-none");
        
    }
};
