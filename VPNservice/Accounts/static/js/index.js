    var count = 0
    document.querySelector(".myButton").addEventListener("mouseover",function(){
        var messageDiv = document.querySelector(".message");
        messageDiv.innerHTML = `Додали нове повідомлення ${count}`;
        messageDiv.style.color = "red";
        count += 1 
    })


    //document.querySelector("#myIdButton").addEventListener("click",function(){
        //alert("Ура! Наше перше повідомлення від ID!!!")
    //})