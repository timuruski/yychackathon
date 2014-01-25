
var Fluffy = Fluffy || {}; // setup namespace

Fluffy.ImgEdit = function() // setup module 
{
    var cavans;
    var ctx;

    function init()
    {
    }

    function setCanvas( c )
    {
	canvas = c;
	ctx = canvas.getContext('2d');
    }

    function loadImage( url )
    {
	var image = new Image;
	image.onload = function(){
	    ctx.drawImage(image,0,0);
	};
	image.src = url;
    }

    function saveImage( url )
    {
    }

    function addImage( x, y, url )
    {
    }

    var publicExport =
        {
            setCanvas: setCanvas,
	    loadImage: loadImage,
	    saveImage: saveImage,
	    addImage: addImage,
            init: init
        };

    return publicExport;
}();

Fluffy.ImgEdit.init();
