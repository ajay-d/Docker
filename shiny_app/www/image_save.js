Shiny.addCustomMessageHandler("saveimage",
  function putImage(message) {
    var canvas1 = document.getElementById("imageView");
    if (canvas1.getContext) {
        var ctx = canvas1.getContext("2d");
        var myImage = canvas1.toDataURL("image/png");
        //var myImage = canvas1.toDataURL("image/png").replace("image/png", "image/octet-stream");
    }
    
    //send data back to sever
    Shiny.onInputChange("myimage", myImage);
    alert(JSON.stringify(message));
  }
);