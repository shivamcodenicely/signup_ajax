/**
 * Created by sony on 12/3/18.
 */


function signup() {

    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var uname = document.getElementById('uname').value;

    var pwd = document.getElementById('pwd').value;
    var email = document.getElementById('email').value;
    var contact = document.getElementById('contact').value;
    var profile_picture=document.getElementById('profile_picture').files;
    alert("hiiiiiiiiiiiiiiio")
//    var profile_picture = document.getElementById('profile_picture').files[0].name;
//    var profile_picture = new FormData($('#profile_picture').get(0));
//    var profile_picture=document.getElementById('profile_picture').get(0);
//    alert(profile_picture)

    $.ajax({
        url: '/signup/validate_username/',
        type: 'POST',
        data: {
            'email': email,
            'fname': fname,
            'lname': lname,
            'uname': uname,
            'contact': contact,
            'pwd': pwd,
//            'profile_picture': profile_picture,


        },
        dataType: 'json',
//        contentType: 'multipart/form-data',
//        processData: false,
//        contentType: false,
        success: function (contxt) {
                 alert('success');
                 console.log(contxt)
                if(contxt.success==true){
                    window.location.href = 'Otp';

                    // document.getElementById("email").value=contxt.email;
                    // document.getElementById("otp").value=contxt.otp;
                }
                else{
                alert("This User is already exist");
                }


            }
    });
}


function Otp() {
    var otp = document.getElementById('otp').value;
    var email = document.getElementById('email').value;

    $.ajax({
        url: '/signup/otp_validate/',
        type: 'POST',
        data: {
            'email': email, 'otp': otp,
        },
        dataType: 'json',
        success: function (contxt) {
            {
                alert("Successful");
                console.log(contxt)
                window.location.href='/signup/loginajax/';
            }
        }
    });
}



