import $ from "jquery";
import "materialize-css/dist/js/materialize";
import "select2";
import "../scss/dashboard.scss";

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(".modal-call").on("touchend click", function (e) {
    e.preventDefault();
    var url = $(this).data('href');
    $.get(url, function (data) {
        $("#modal").html(data);
        $("#modal").modal("open")
    })
});

$(document).ready(function () {
    $('.modal').modal({
            dismissible: true,
            opacity: .5,
            inDuration: 300,
            outDuration: 200,
            startingTop: '4%',
            endingTop: '10%',
            complete: function () {
                $(this).children().remove();
            },
            dismiss: function () {
                $(".modal").modal('close');
            }
        }
    );
    $('select').material_select();
    $(".side-act").sideNav();
});