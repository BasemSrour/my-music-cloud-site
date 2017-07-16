$('.toggle_favorite').click(function()
{
    var album_id;
    album_id = $(this).attr("data-albumid");
    $.get('/music/' + album_id + '/favorite_album/', {}, function(data){
        $('#fav_button-' + album_id)[0].classList.toggle("active");
    });
});
