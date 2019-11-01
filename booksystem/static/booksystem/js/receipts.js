function openReceiptSettings(){
    let newWindow = window.open(
        `/booksystem/${current_book_system_pk}/receipts/settings/`, 
        "_blank", 
        "width=600,height=600",
        "toolbar=0",
        "titlebar=0",
        "status=0",
        "scrollbars=0",
        "resizable=no",
        "menubar=0",
    );
};

function back_to_frontend(){
    window.location.assign(`/booksystem/${current_book_system_pk}/`);
}