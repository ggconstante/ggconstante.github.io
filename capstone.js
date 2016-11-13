var increaseButton = function(){//this is you increase button your calling
        var divIncreaseFont = document.getElementById("fontIncrease");//it is finding the element of the html that has the same id as the fontIncrease
            if(divIncreaseFont.style.fontSize == "")//this is comparing bigger.style.fontSize to an emptyString
            divIncreaseFont.style.fontSize = "20px";
        var pixelIncrease = parseInt(divIncreaseFont.style.fontSize);//this will convert it into integer
            divIncreaseFont.style.fontSize =  pixelIncrease + 1 + "px";//this will convert the string into an integer and increases each time you press the font by 1
        }
var hideButton = function(){//this is for the hide
        var divHide = document.getElementById("hideMe");//this is the div you are calling
        var buttonHide = document.getElementById("click");//this is your button..you press this guy..
        divHide.style.visibility = "hidden";//this will hide your paragraph
        buttonHide.onclick = showButton;//this is doing the showButton
        buttonHide.value = "Show";                  //this is you make hide to show
        }

var showButton = function(){//this is for the show
        var buttonShow = document.getElementById("click");
        var divShow = document.getElementById("hideMe");
            divShow.style.visibility = "visible";
            buttonShow.onclick = hideButton;
            buttonShow.value = "Hide";
        }
        
        // //this is for the double-click
        // function buttonDouble(x){
        // x.height = parseInt(x.height) + 10;
        // x.width = parseInt(x.width) + 10;
        // }
        
        //this is for move to the right
        function buttonToRight(capstone){
        capstone.style.left = parseInt(capstone.style.left) + 30 + 'px';
        } 