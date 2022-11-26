document.addEventListener("DOMContentLoaded", function () {
    
    /**
    * Check current value of quantity input
    * sets min and max values
    * disables buttons when exceeded
    * sets value to stock limit if keyboard used to enter value greater than stock limit
    */
    let qtyInputRangeHandler = productID => {
        
        const qtyInput = $(`.current-qty-pid-${productID}`);
        const qtyInputValue = parseInt(qtyInput.val());
        const qtyDisableMinus = qtyInputValue < 2;
        const qtyInputMax = parseInt(qtyInput.attr('max'));
        const qtyDisablePlus = qtyInputValue >= qtyInputMax;
        const qtyBtnMinus = $(`.decrease-qty-${productID}`);
        const qtyBtnPlus = $(`.increase-qty-${productID}`);
        qtyBtnMinus.prop('disabled', qtyDisableMinus);
        qtyBtnPlus.prop('disabled', qtyDisablePlus);
        if (qtyInputValue > qtyInputMax) {
            qtyInput.val(qtyInputMax);
        } else if (qtyInputValue < 1) {
            qtyInput.val(1);
        }
    };

    const allQtyInputs = $('.qty-input');
    allQtyInputs.each((index, input) => {
        const productID = $(input).data('product-id');
        qtyInputRangeHandler(productID);
    });


    /**
    * Gives functionality to the '-' button
    * on the qty selector forms and prevents its default action
    */
    $('.decrease-qty').click(function(e){
        
        e.preventDefault();
        let quantyInput = $(this).closest('.input-group').find('.qty-input')[0];
        let quantity = parseInt(quantyInput.value);
        let productId = $(this).data('product-id');
        let allQtyInputs = $(`.input-group-${productId} input[name='quantity']`);
        $(allQtyInputs).val(quantity - 1);
        qtyInputRangeHandler(productId);
    });

    /**
    /* Gives functionality to the '+' button
    /* on the qty selector forms and prevents its default action
    */
    $('.increase-qty').click(function(e){
        
        e.preventDefault();
        let quantyInput = $(this).closest('.input-group').find('.qty-input')[0];
        let quantity = parseInt(quantyInput.value);
        let productId = $(this).data('product-id');
        let allQtyInputs = $(`.input-group-${productId} input[name='quantity']`);
        $(allQtyInputs).val(quantity + 1);
        qtyInputRangeHandler(productId);
    });

});