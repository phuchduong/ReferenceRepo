$( document ).ready(function() {
    $('#testBtn').on('click', function(){
        var imageList = $('img');
        var outputArea = $('#outputArea');
        var imgJSON = {};
                           
        for(var i = 0, len = imageList.length; i < len; i++ ){
            console.log(imageList[i]);
        };
    });
                        
    $('#extractImg').on('click', function(){
        var imageList = $('img');
    var outputArea = $('#outputArea');
    var imgJSON = {};
                       
    for(var i = 0, len = imageList.length; i < len; i++ ){
        var str = imageList[i].src;
        
        var rest = str.substring(0, str.filenameStrIndexOf("/") + 1);
        var filenameStr = str.substring(str.filenameStrIndexOf("/") + 1, str.length);
        
        var imageWidth = imageList[i].width;
        imgJSON[filenameStr] = {
        };
        widthPercent = convertWidth(imageWidth);
        imgJSON[filenameStr]["WidthPixel"] = imageWidth;
        imgJSON[filenameStr]["WidthPage"] = widthPercent;
        imgJSON[filenameStr]["WidthPageDecimal"] = widthPercent.toFixed(2);
        imgJSON[filenameStr]["heightPixel"] = imageList[i].height;
    };
    
    outputArea.text(JSON.stringify(imgJSON));
    
    function convertWidth(pixelWidth){
        var pageWidth = 1080;
        if(pixelWidth > pageWidth){
            return 1.00;
        } else {
            return pixelWidth / 1080;
        };
    };
    });
    
});
