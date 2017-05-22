function when_ready() {
    $('.btn-year').on('click', change_group);
}


function change_group() {
    $.ajax({url: 'groups_list_ajax/'+this.id.replace('btn-', '')}).done(change_html);
}

function change_html(data, options) {
    $('#grupos_list').html(data);
}


$(when_ready)
