
var Fluffy = Fluffy || {}; // setup namespace

Fluffy.ImgEdit = function() // setup module 
{
    var cavans;
    var ctx;

    var baseImage;
    var setLogo;

    function init()
    {
	setLogo = true;
    }

    function setCanvas( c )
    {
	canvas = c;
	ctx = canvas.getContext('2d');
    }

    function loadImage( url )
    {
	baseImage = new Image;
	baseImage.onload = function(){
	    ctx.drawImage(baseImage,0,0);
	    setLogo = false;
	};
	baseImage.src = url;
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
	    setLogo = true;
	};
	image.src = url;
    }

    function animateImage( url, x, y  )
    {
	if ( setLogo ) {
	    return;
	}
	var image = new Image;
	ctx.drawImage(baseImage,0,0);
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
	    animateImage: animateImage,
            init: init
        };

    return publicExport;
}();

Fluffy.ImgEdit.init();
