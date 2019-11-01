/* Selecting With Stock or Without Stock */
function navigateToWithStock(current_book_system_pk){
    window.location.assign(`/booksystem/${current_book_system_pk}/`);
}
function navigateToWithoutStock(current_book_system_pk){
    window.location.assign(`/booksystem/${current_book_system_pk}/withoutStock/`);
}


let localCart = [

]
function addAItem(){
    let [bookIdInputed, bookQtyInputed] = [document.getElementById('book-id-input').value, document.getElementById('book-qty-input').value];
    let aNewObj;
    for(let i = 0; i < bookLocalDatabase.length; i++){
        if(Number(bookLocalDatabase[i].bookId) == Number(bookIdInputed)){
            aNewObj = bookLocalDatabase[i];           // Creating a new obj with QTY property
            aNewObj['qty'] = Number(bookQtyInputed);
            localCart.push(aNewObj);                  // Pushing it to our local Cart
        }
    }
    calculateSubTotalNdTotal();
    updateTheCartView();
}

function calculateSubTotalNdTotal(){
    let subTotalInput = document.getElementById('subtotal-input');
    let totalInput = document.getElementById('total-input');
    let discountInput = document.getElementById('book-discount-input');
    let subTotal = 0;
    for(let i = 0; i < localCart.length; i++){
        subTotal += Number(localCart[i].qty) * Number(localCart[i].price);
    }
    /* Setting SubTotal */
    subTotalInput.value = subTotal;
    /* Setting Total */
    totalInput.value = subTotal * ((100 - discountInput.value) / 100);
}

function updateTheCartView(){
    let cartView = document.getElementById('cart');
    let htmlCode = '';
    for(let i = 0; i < localCart.length; i++){
        htmlCode += `
            <div class="cart-card">
                <h3>${localCart[i].name}</h3>
                <p>Rs.${localCart[i].price}.00 x ${localCart[i].qty}</p>
                <input type="hidden" name="book_pk_${localCart[i].bookPk}" value="${localCart[i].bookPk}">
                <input type="hidden" name="book_qty_${localCart[i].bookPk}" value="${localCart[i].qty}">
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
    let bookIdInput = document.getElementById('book-id-input');
    let bookQtyInput = document.getElementById('book-qty-input');
    let subtotalInput = document.getElementById('subtotal-input');
    let totalInput = document.getElementById('total-input');
    [bookIdInput.value, bookQtyInput.value, subtotalInput.value, totalInput.value] = ' ';
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
/* The Checkout Functionality */
function more_option_checkout(){
    console.log('Checkout pressed!');
    // Every inputs
    let inputList = document.getElementsByTagName('input');
    // Lists to hold book inputs
    let bookPkInputList = [];
    let bookQtyInputList = [];
    // Going through every input element on DOM and filtering RELATED INPUT
    for(let input in inputList){
        // If the input has a name then only check it
        if(inputList[input].name){
            if( inputList[input].name.slice(0, 4) == 'book' ){
                if( inputList[input].name.slice(0, 7) == 'book_pk' ){
                    bookPkInputList.push(inputList[input])
                }
                if( inputList[input].name.slice(0, 8) == 'book_qty' ){
                    bookQtyInputList.push(inputList[input])
                }
            }
        }
    }
    for(let pk in bookPkInputList){
        for(let book in bookLocalDatabase){
            if(bookPkInputList[pk].value == bookLocalDatabase[book].bookPk){
                bookLocalDatabase[book].stock = bookLocalDatabase[book].stock - Number(bookQtyInputList[pk].value);
            }
        }
    }
    console.log(bookPkInputList);
    console.log(bookQtyInputList);
    /* Setting the Local Book DB to a Input for Later Use */
    document.getElementById('input-local-book-db').value = bookLocalDatabase;
    /* Submitting */
    let inputForFormSubmission = document.getElementById('input-for-form-submission')
    inputForFormSubmission.click();
}

function more_option_receipts(){
    window.location.assign(`/booksystem/${current_book_system_pk}/receipts/`);
}

function more_option_dashboard(){
    window.location.assign(`/dashboard/`);
}

function more_option_endday(){
    $.ajax({
        type: 'POST',
        url: `/booksystem/${current_book_system_pk}/endDay/`,
        data: {
            'current_book_system_pk':current_book_system_pk,
            'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
        },
        success: function () {
            /* Success Message */
            n = new Notification( "Success!", {
                body: "End Day Success!!", 
                icon : "star.ico"
            });
        }
    });
}

/* Short keys */
// Click the Add btn when user hit shift
document.addEventListener("keyup", function(event) {
    console.log('keyup');
    event.preventDefault();
    //Check if modal is visible and key code

    /* For CTRL Key */
    if (event.keyCode === 17) {
        let book_id_input = document.getElementById('book-id-input');
        let book_qty_input = document.getElementById('book-qty-input');

        /* Focusing to what has not being inputed */
        if(book_id_input.value == ''){
            book_id_input.focus();
        }else if(book_qty_input.value == ''){
            book_qty_input.focus();
        }

        if(book_id_input.value && book_qty_input.value){
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