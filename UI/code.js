function myFunction() {
    var x, text;

     var cont = "ali@gmail.com"
    x = document.getElementById("myemail").value;

    if(cont.localeCompare(x)){
        text = "**Input not valid";
        document.getElementById("contdis").style.color ="red";

    } else {
        text = "**Input OK";
        document.getElementById("contdis").style.color ="green";

    }
    document.getElementById("contdis").innerHTML = text;

}