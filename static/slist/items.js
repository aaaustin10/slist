$(document).ready(function()
{
    $('.item').on('click', function()
    {
        $(this).toggleClass('marked');
    });

    function do_post(action, data)
    {
        post_data = {
            'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val(),
            'action': action,
        }
        $.extend(post_data, data)

        $.ajax(
        {
            type: 'post',
            data: post_data,
            success: function(data, textStatus)
            {
                window.location.href = data;
            },
        });
    }

    $('#delete_items').on('click', function()
    {
        item_ids = $('.marked').map(function(){ return $(this).data('id'); })
        do_post('delete_items', { item_names: item_ids.toArray() })
    })
    $('#delete_list').on('click', function(){ do_post('delete_list', {}); })
    $('#create').on('keyup', function(e){ if (e.keyCode == 13) { do_post('create', { item_name: $(this).val() }); } })
});
