function j() {
    alert("helllo");
    var jproduct1 = document.getElementById('1').value;
        alert(jproduct1)


    $.ajax({
        url: '/signup/jprod1',
        type: 'POST',
        data: {
            'jproduct1':jproduct1
        },
        dataType: 'json',
        success: function (contxt) {
            {
                console.log(contxt.mobile_list)
                alert("Successful");
                console.log(contxt.success)
                if(contxt.success==true){

                    console.log("hhhhhhhhhhhhhh")
                    window.location.href='/signup/profile1/?mobile_list='+contxt.mobile_list;
                    }
                else{
                    alert("Incorrect")
                }
            }

        }
    });
}



