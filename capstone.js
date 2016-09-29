var increaseButton = function(){//this is you increase button your calling
        var divIncreaseFont = document.getElementById("fontIncrease");//it is finding the element of the html that has the same id as the fontIncrease
            if(divIncreaseFont.style.fontSize == "")//this is comparing bigger.style.fontSize to an emptyString
            divIncreaseFont.style.fontSize = "20px";
        var pixelIncrease = parseInt(divIncreaseFont.style.fontSize);//this will convert it into integer
            divIncreaseFont.style.fontSize =  pixelIncrease + 1 + "px";//this will convert the string into an integer and increases each time you press the font by 1
        }