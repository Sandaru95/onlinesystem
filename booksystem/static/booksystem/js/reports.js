if(Notification.permission !== 'granted'){
    Notification.requestPermission();
}

function updateTheCashInfoView(){
    document.getElementById('cash-info-today').innerText = "Today Sales : Rs. " + String(todays_total);
    document.getElementById('cash-info-overall').innerText = "Overall Sales: Rs. " + String(overall_total);
    document.getElementById('cash-info-drawer').innerText = "Cash Drawer Amount: Rs. " + String(drawer_total);
};

function addCashToDrawer(){
    console.log('Cash add function fired!');
    let add_input = document.getElementById('drawer-add-input');
    $.ajax({
        type: 'POST',
        url: `/booksystem/${current_book_system_pk}/reports/addCash/`,
        data: {
            'amount_added':add_input.value,
            'current_book_system_pk': current_book_system_pk,
            'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
        },
        success: function () {
            console.log('Success in adding!');
            drawer_total += Number(add_input.value)
            updateTheCashInfoView();
            /* Success Message */
            n = new Notification( "Success!", {
                body: "Cash Added!", 
                icon : "star.ico"
            });
        }
    });
};

function drawCashFromDrawer(){
    console.log('Cash draw function fired!');
    let draw_input = document.getElementById('drawer-draw-input');
    $.ajax({
        type: 'POST',
        url: `/booksystem/${current_book_system_pk}/reports/drawCash/`,
        data: {
            'amount_drawed':draw_input.value,
            'current_book_system_pk': current_book_system_pk,
            'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
        },
        success: function () {
            console.log('Success in drawing!');
            drawer_total -= Number(draw_input.value)
            updateTheCashInfoView();
            /* Success Message */
            n = new Notification( "Success!", {
                body: "Cash Drawen", 
                icon : "star.ico"
            });
        }
    });
};

function drawerKick(){
    window.print();
    /* Success Message */
    n = new Notification( "Successfull!", {
        body: "Drawer Kicked!", 
        icon : "star.ico"
    });
}

/* More Options */
function more_option_dashboard(){
    window.location.assign('/dashboard/');
}

function more_option_frontend(){
    window.location.assign(`/booksystem/${current_book_system_pk}/`);
}

function more_option_clear(){
    document.getElementById('drawer-draw-input').value = '';
    document.getElementById('drawer-add-input').value = '';
}