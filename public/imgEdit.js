
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

    function getImage()
    {
	return canvas.toDataURL("image/png");
    }

    function addImage( url, x, y  )
    {
	var image = new Image;
	image.onload = function(){
	    ctx.drawImage(image,x,y);
	};
	image.src = url;
    }

    var publicExport =
        {
            setCanvas: setCanvas,
	    loadImage: loadImage,
	    getImage: getImage,
	    addImage: addImage,
            init: init
        };

    return publicExport;
}();

Fluffy.ImgEdit.init();
