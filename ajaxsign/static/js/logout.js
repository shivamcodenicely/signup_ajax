$('#logout-button').click(function() {
$.ajax({
    type: "POST",
    url: "logout",
    success: function() {
       alert("You have been successfully logged out");
       window.location.href = "signup/loginajax";
    },
    error: function() {
        alert("Error! Something unexpected happened");
    }
});
return false;
});