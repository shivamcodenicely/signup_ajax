function login() {
    alert("hellloooooooooo");
    var pwd = document.getElementById('pwd').value;
    var email = document.getElementById('email').value;

    $.ajax({
        url: '/signup/validate/',
        type: 'GET',
        data: {
            'email': email, 'pwd': pwd,
        },
        dataType: 'json',
        success: function (contxt) {
            {
                console.log(contxt)
                alert("Successful");
                window.location.href='profile';
            }

        }
    });
}


function forget() {
    alert("hellloooooooooo");
//    var pwd = document.getElementById('contact').value;
    var email = document.getElementById('email').value;

    $.ajax({
        url: '/signup/forget_function/',
        type: 'POST',
        data: {
            'email': email,
        },
        dataType: 'json',
        success: function (contxt) {
            {
                console.log(contxt)
                alert("Forget Successful");
                window.location.href = 'loginajax';
            }
         }

    });
}



