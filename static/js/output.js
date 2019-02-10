  function postText(){
        $.post( "/analize", $("#editor" ).text())
          .done(function( data ) {
            $("#editor" ).html(data.response);


var url;


// If the server provides video url, play it.
if(data.url != "" && typeof(data.url) != "undefined") url = data.url;
else if(data.emotion == "happy") url = "https://www.youtube.com/embed/y6Sxv-sUYtM";
else if(data.emotion == "sad") url = "https://www.youtube.com/embed/sFukyIIM1XI"
else if(data.emotion == "angry") url = "https://www.youtube.com/embed/BsVq5R_F6RA"
else if(data.emotion == "excited") url = "https://www.youtube.com/embed/ZaI2IlHwmgQ"
else if(data.emotion == "fearful") url = "https://www.youtube.com/embed/uV_CGpMsEhY"
else url = "https://www.youtube.com/embed/CQ85sUNBK7w"

var obj = {"video": {"value": "<iframe title='YouTube video player' type=\"text/html\" width='640' height='390' src="+url+" frameborder='0' allowFullScreen></iframe>"}};


$("#test").html(obj.video.value);





        });
    }