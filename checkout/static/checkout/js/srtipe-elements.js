// Adapted from stripe card element docs https://stripe.com/docs/payments/card-element?client=html and
// https://stripe.com/docs/payments/accept-card-payments?platform=web&ui=elements using the boutique ado
// project as a guide to combine them

// Stripe related references
const stripePublicKeyRef = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecretRef = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripePublicKeyRef);
const elements = stripe.elements();

// Payment form references
const paymentFormRef = $("#payment-form");
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
    // card.on("change", function (event) {
        //       // Disable the Pay button if there are no card details in the Element
        //       document.querySelector("button").disabled = event.empty;
        //       document.querySelector("#card-error").textContent = event.error ? event.error.message : "";
        //     });
        
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


payNowBtnRef.click(function(event) {
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
    console.log("confirming card payment");   
    stripe.confirmCardPayment(clientSecret, {
        
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    state: $.trim(form.county.value),
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
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

                paymentFormRef.submit()

            }
        };
    })
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


// /* ------- UI helpers ------- */

// // Shows a success message when the payment is complete
// var orderComplete = function(paymentIntentId) {
//   loading(false);
//   document
//     .querySelector(".result-message a")
//     .setAttribute(
//       "href",
//       "https://dashboard.stripe.com/test/payments/" + paymentIntentId
//     );
//   document.querySelector(".result-message").classList.remove("hidden");
//   document.querySelector("button").disabled = true;
// };

// // Show the customer the error from Stripe if their card fails to charge
// var showError = function(errorMsgText) {
//   loading(false);
//   var errorMsg = document.querySelector("#card-error");
//   errorMsg.textContent = errorMsgText;
//   setTimeout(function() {
//     errorMsg.textContent = "";
//   }, 4000);
// };

// // Show a spinner on payment submission
// var loading = function(isLoading) {
//   if (isLoading) {
//     // Disable the button and show a spinner
//     document.querySelector("button").disabled = true;
//     document.querySelector("#spinner").classList.remove("hidden");
//     document.querySelector("#button-text").classList.add("hidden");
//   } else {
//     document.querySelector("button").disabled = false;
//     document.querySelector("#spinner").classList.add("hidden");
//     document.querySelector("#button-text").classList.remove("hidden");
//   }