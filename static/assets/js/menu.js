var menuList = document.getElementById("menuList");

menuList.style.maxHeight = "0px";
menuList.style.backgroundColor = "white";

function togglemenu(){

    if(menuList.style.maxHeight == "0px")
    {
        menuList.style.maxHeight = "800px";
        menuList.style.backgroundColor = "black";

    }
    else 
    {
        menuList.style.maxHeight = "0px";
        menuList.style.backgroundColor = "white";
    }
}