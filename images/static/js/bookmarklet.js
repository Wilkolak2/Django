const siteUrl = '//127.0.0.1:8000/'
const styleUrl = siteUrl + 'static/css/bookmarklet.css'
const minWitdh = 250
const minHeight = 250

var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = siteUrl + '?r=' + Math.floor(Math.random()*9999999);
head.appendChild(link);

var body = document.getElementsByTagName('body')[0]
boxHtml = `
      <div id="bookmarklet">
        <a href="#" id="close">&times;</a>
        <h1>Wybierz zdjęcie do zapisania:</h1>
        <div class="images"></div>
      </div>
`
body.innerHTML += boxHtml

function bookmarkletLaunch(){
    bookmarklet = document.getElementById('bookmarklet');
    var imagesFound = bookmarklet.querySelector('.images');

    imagesFound.innerHTML = ''
    bookmarklet.style.display = 'block'
    bookmarklet.querySelector('#close').addEventListener('click', function(){
        bookmarklet.style.display = 'none'
    })
}