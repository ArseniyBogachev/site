const mainElement = document.documentElement;
const block = document.querySelectorAll('#cat-id')
const WidthObject = mainElement.clientWidth;
const video = document.getElementById('video');

if (WidthObject <= 1472){
    for (let i of block){
         i.innerText = i.innerText.slice(0, 200) + '...';
    }
};

window.onload = function() {
    document.getElementById('video').play();
    video.setAttribute('autoplay','autoplay');
    console.log('1')
};
