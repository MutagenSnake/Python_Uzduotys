//function openInNewWindow() {
//   var img_src = document.getElementById("Image");
//   var url = img_src.src
//   window.open(url,'Image');
//}

window.onclick = e => {
//    console.log(e.target);
//    console.log(e.target.src);
    var parent = e.target.parentElement.className
    console.log(parent)
    if (parent === "picture") {
        var url = e.target.src;
        window.open(url,'Image');
        }}