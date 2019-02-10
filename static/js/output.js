  function postText(){
        $.post( "/analize", $("#editor" ).text())
          .done(function( data ) {
            $("#editor" ).html("You are " + data.emotion + "!");


var url;


//console.log(data);
if(data.url != "") url = data.url;
else if(data.emotion == "happy") url = "https://www.youtube.com/embed/y6Sxv-sUYtM";
else if(data.emotion == "sad") url = "https://www.youtube.com/embed/sFukyIIM1XI"
else if(data.emotion == "angry") url = "https://www.youtube.com/embed/BsVq5R_F6RA"
else if(data.emotion == "excited") url = "https://www.youtube.com/embed/ZaI2IlHwmgQ"
else if(data.emotion == "fearful") url = "https://www.youtube.com/embed/uV_CGpMsEhY"

var obj = {"video": {"value": "<iframe title='YouTube video player' type=\"text/html\" width='640' height='390' src=url frameborder='0' allowFullScreen></iframe>"}};


$("#test").html(obj.video.value);





        });
    }