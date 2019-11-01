function navigateToWithStock(current_book_system_pk){
    window.location.assign(`/booksystem/${current_book_system_pk}`);
}
function navigateToWithoutStock(current_book_system_pk){
    window.location.assign(`/booksystem/${current_book_system_pk}/withoutStock/`)
}

/* Adding a item part */
let localCart = [];

function addAItem(){
    let [bookPriceInput, bookQtyInputed] = [document.getElementById('without-stock-book-price-input').value, document.getElementById('without-stock-book-qty-input').value];
    let discountInput = document.getElementById('without-stock-book-discount-input').value;
    let aNewObj = {};
    aNewObj['bookType'] = 'Other Sale';
    aNewObj['bookPrice'] = bookPriceInput;
    aNewObj['bookQty'] = bookQtyInputed;
    aNewObj['discount'] = discountInput;
    aNewObj['bookTotal'] = ((bookPriceInput * bookQtyInputed) * (100 - discountInput)) / 100; 
    localCart.push(aNewObj);
    calculateSubTotalNdTotal();
    updateTheCartView();
}

function calculateSubTotalNdTotal(){
    let subTotalInput = document.getElementById('without-stock-subtotal-input');
    let totalInput = document.getElementById('without-stock-total-input');
    let discountInput = document.getElementById('without-stock-book-discount-input');
    let subTotal = 0;
    let total = 0;
    for(let i = 0; i < localCart.length; i++){
        subTotal += Number(localCart[i].bookPrice) * Number(localCart[i].bookQty);
        total += localCart[i].bookTotal
    }
    /* Setting SubTotal */
    subTotalInput.value = subTotal;
    /* Setting Total */
    totalInput.value = total;
}

function updateTheCartView(){
    let cartView = document.getElementById('cart');
    let htmlCode = '';
    for(let i = 0; i < localCart.length; i++){
        htmlCode += `
            <div class="cart-card">
                <h3>${localCart[i].bookType}</h3>
                <p>Discount: ${localCart[i].discount}%</p>
                <p>Rs.${localCart[i].bookPrice}.00 x ${localCart[i].bookQty}</p>
                <p>= Rs.${localCart[i].bookTotal}</p>
                <input type="hidden" name="book_price_${i}" value="${localCart[i].bookPrice}">
                <input type="hidden" name="book_qty_${i}" value="${localCart[i].bookQty}">
            </div>
        `
    }
    cartView.innerHTML = htmlCode;
}

/* More Options */
/* The Drawer and Reports Functionality */
function more_option_drawer_and_reports(){
    window.location.assign(`/booksystem/${current_book_system_pk}/reports/`);
}

function more_option_clear(){
    /* Removing Values of some inputs */
    let bookPriceInput = document.getElementById('without-stock-book-price-input');
    let bookQtyInput = document.getElementById('without-stock-book-qty-input');
    let subtotalInput = document.getElementById('without-stock-subtotal-input');
    let totalInput = document.getElementById('without-stock-total-input');
    [bookPriceInput.value, bookQtyInput.value, subtotalInput.value, totalInput.value] = ' ';
    localCart = [];
    calculateSubTotalNdTotal();
    updateTheCartView();
}

function more_option_backend(){
    window.location.assign(`/booksystem/${current_book_system_pk}/backend/`);
}

function more_option_shortcuts(){
    let newWindow = window.open(
        `/booksystem/${current_book_system_pk}/shortcuts/`, 
        "_blank", 
        "width=600,height=600",
        "toolbar=0",
        "titlebar=0",
        "status=0",
        "scrollbars=0",
        "resizable=no",
        "menubar=0",
    );
}

function more_option_dashboard(){
    window.location.assign('/dashboard/');
}

/* The Checkout Functionality */

function more_option_checkout(){
    console.log('Checkout pressed!');
    /* Submitting */
    let inputForFormSubmission = document.getElementById('input-for-form-submission')
    inputForFormSubmission.click();
}

function more_option_receipts(){
    window.location.assign(`/booksystem/${current_book_system_pk}/receipts/`)
}

/* On load of Body Focus to Input:Book Price */
function focusToBookPriceField(){
    document.getElementById('without-stock-book-price-input').focus();
 }

/* Short keys */
// Click the Add btn when user hit shift
document.addEventListener("keyup", function(event) {
    console.log('keyup');
    event.preventDefault();
    //Check if modal is visible and key code

    /* For CTRL Key */
    if (event.keyCode === 17) {
        let book_price_input = document.getElementById('without-stock-book-price-input');
        let book_qty_input = document.getElementById('without-stock-book-qty-input');

        /* Focusing to what has not being inputed */
        if(book_price_input.value == ''){
            book_price_input.focus();
        }else if(book_qty_input.value == ''){
            book_qty_input.focus();
        }

        if(book_price_input.value && book_qty_input.value){
            //Programatically click the button
            document.getElementById("checkout-add-btn").click();
        }
    }

    /* For Delete Key for removing Elements */
    if (event.keyCode === 46){
        // Poping the last item of the cart
        localCart.pop();
        updateTheCartView();
    }

    /* For Home Key for Navigate to dashboard */
    if (event.keyCode === 36){
        // Navigating to dashboard
        window.location.assign('/dashboard/')
    }

    /* For End Key for getting receipts panel */
    if (event.keyCode === 35){
        // Navigating to dashboard
        window.location.assign(`/booksystem/${current_book_system_pk}/receipts/`)
    }

    /* Insertkey for Shortcut click */
    if(event.keyCode === 45){
        // Clicking the shortcut button
        document.getElementById('more-option-shortcut-btn').click();
    }
});