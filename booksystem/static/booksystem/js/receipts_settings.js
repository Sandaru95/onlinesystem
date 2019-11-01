function closeReceiptSettings(){
    window.close();
};

function updateReceiptSettings(){
    console.log('Function fired!');
    let publisherName = document.getElementById('publisher-name').value;
    let publisherAddress = document.getElementById('publisher-address').value;
    let greentingText = document.getElementById('last-greenting-text').value;
    let DateBoolean = document.getElementById('date-select').value;
    let noItemsBoolean = document.getElementById('no-items-select').value;
    let subTotalBoolean = document.getElementById('subtotal-select').value;
    let totalBoolean = document.getElementById('total-select').value;
    $.ajax({
        type: 'POST',
        url: `/booksystem/${current_book_system_pk}/receipts/settings/`,
        data: {
            'publisherName' : publisherName,
            'publisherAddress' : publisherAddress,
            'greentingText' : greentingText,
            'DateBoolean' : DateBoolean,
            'noItemsBoolean' : noItemsBoolean,
            'subTotalBoolean' : subTotalBoolean,
            'totalBoolean' : totalBoolean,
            'current_book_system_pk':current_book_system_pk,
            'csrfmiddlewaretoken': $("input[name='csrfmiddlewaretoken']").val()
        },
        success: function (json) {
            console.log('success is called!');
            eval(json);
        }
    });
};