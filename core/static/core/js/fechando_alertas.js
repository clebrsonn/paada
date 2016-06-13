/**
 * Created by douglas on 12/06/16.
 */
window.setTimeout(function () {
    $(".alert").fadeTo(500, 0).slideUp(500, function () {
        $(this).remove();
    });
}, 2000);