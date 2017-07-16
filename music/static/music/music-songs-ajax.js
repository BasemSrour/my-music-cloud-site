$('.toggle_favorite').click(function()
{
    var song_id;
    song_id = $(this).attr("data-songid");
    $.get('/music/' + song_id + '/favorite_song/', {}, function(data){
        $('#fav_button-' + song_id)[0].classList.toggle("active");
    });
});
