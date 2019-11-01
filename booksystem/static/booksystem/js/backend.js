let createItemSpawnSpace = document.getElementById('create-item-spawn-space');
function spawnAuthorCreateInput(){
    createItemSpawnSpace.innerHTML = `
        <input 
            id="item-spawn-space-author-input"
            type="text" 
            class="add-bottom-left-radius add-bottom-right-radius" 
            placeholder="Author Name"
        >
    `
}
function spawnPublisherCreateInput(){
    createItemSpawnSpace.innerHTML = `
        <input 
            id="item-spawn-space-publisher-input"
            type="text"
            class="add-bottom-left-radius add-bottom-right-radius" 
            placeholder="Publisher Name"
        >
    `
}
function spawnBookTypeCreateInput(){
    createItemSpawnSpace.innerHTML = `
        <input 
            id="item-spawn-space-book-type-input"
            type="text" 
            class="add-bottom-left-radius add-bottom-right-radius" 
            placeholder="Type Name"
        >
    `
}
function spawnUserCreateInput(){
    createItemSpawnSpace.innerHTML = `
        <input 
            id="item-spawn-space-cashier-username-input" 
            type="text" 
            placeholder="User Name"
        >
        <input 
            id="item-spawn-space-cashier-password-input" 
            type="password" 
            placeholder="Password"
        >
        <input 
            type="password" 
            class="add-bottom-left-radius add-bottom-right-radius" 
            placeholder="Confirm Password"
        >
    `
}

if(Notification.permission !== 'granted'){
    Notification.requestPermission();
}

function addAItemToDB(){
    console.log('Function Fired!');
    let author_input = document.getElementById('item-spawn-space-author-input');
    let publisher_input = document.getElementById('item-spawn-space-publisher-input');
    let book_type_input = document.getElementById('item-spawn-space-book-type-input');

    let cashier_username_input = document.getElementById('item-spawn-space-cashier-username-input');
    let cashier_password_input = document.getElementById('item-spawn-space-cashier-password-input');

    let spawned_book_name_input = document.getElementById('spawned-book-name-input');
    let spawned_book_price_input = document.getElementById('spawned-book-price-input');
    let spawned_book_stock_input = document.getElementById('spawned-book-stock-input');
    let spawned_book_publisher_input = document.getElementById('spawned-book-publisher-input');
    let spawned_book_type_input = document.getElementById('spawned-book-type-input');
    let spawned_book_author_input = document.getElementById('spawned-book-author-input');
    let spawned_book_code_input = document.getElementById('spawned-book-code-input');
    if(author_input){
        $.ajax({
            type: 'POST',
            url: '/booksystem/createAuthor/',
            data: {
                'author_name':author_input.value,
                'current_book_system_pk':current_book_system_pk,
                'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function () {
                
                /* Adding data to local DB one also */
                authorLocalList.push(author_input.value);
                /* Success Message */
                n = new Notification( "Successfull!", {
                    body: "Data Base Updated Successfully!", 
                    icon : "star.ico"
                });
            }
        });
    }else if(publisher_input){
        $.ajax({
            type: 'POST',
            url: '/booksystem/createPublisher/',
            data: {
                'book_publisher_name':publisher_input.value,
                'current_book_system_pk':current_book_system_pk,
                'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function () {
                
                /* Adding data to local DB one also */
                bookPublisherLocalList.push(publisher_input.value);
                /* Success Message */
                n = new Notification( "Successfull!", {
                    body: "Data Base Updated Successfully!", 
                    icon : "star.ico"
                });
            }
        });
    }else if(book_type_input){
        $.ajax({
            type: 'POST',
            url: '/booksystem/createBookType/',
            data: {
                'book_type_name':book_type_input.value,
                'current_book_system_pk':current_book_system_pk,
                'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function () {
                
                /* Adding data to local DB one also */
                bookTypeLocalList.push(book_type_input.value);
                /* Success Message */
                n = new Notification( "Successfull!", {
                    body: "Data Base Updated Successfully!", 
                    icon : "star.ico"
                });
            }
        });
    }else if(cashier_username_input && cashier_password_input){
        $.ajax({
            type: 'POST',
            url: '/booksystem/createCashier/',
            data: {
                'cashier_username':cashier_username_input.value,
                'cashier_password':cashier_password_input.value,
                'current_book_system_pk':current_book_system_pk,
                'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function () {
                
                /* Success Message */
                n = new Notification( "Successfull!", {
                    body: "Data Base Updated Successfully!", 
                    icon : "star.ico"
                });
            }
        });
    }else if(spawned_book_name_input && spawned_book_price_input && spawned_book_stock_input && spawned_book_publisher_input && spawned_book_type_input && spawned_book_author_input && spawned_book_code_input){
        $.ajax({
            type: 'POST',
            url: '/booksystem/createBook/',
            data: {
                'book_name':spawned_book_name_input.value,
                'book_price':spawned_book_price_input.value,
                'book_stock':spawned_book_stock_input.value,
                'book_publisher':spawned_book_publisher_input.value,
                'book_type':spawned_book_type_input.value,
                'book_author':spawned_book_author_input.value,
                'book_item_code':spawned_book_code_input.value,
                'current_book_system_pk':current_book_system_pk,
                'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function () {
                
                /* Success Message */
                n = new Notification( "Successfull!", {
                    body: "Data Base Updated Successfully!", 
                    icon : "star.ico"
                });
            }
        });
    }
}

/* More Options */
function more_option_frontend(){
    window.location.assign(`/booksystem/${current_book_system_pk}/`);
}

function more_option_clear(){

    let inputList = document.getElementsByTagName('input');
    for(let e in inputList){
        inputList[e].value = ' ';
    };

}

function more_option_dashboard(){
    window.location.assign('/dashboard/');
}