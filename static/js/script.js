(function(){

  var moon = document.querySelector(".moon");
  var clouds = document.querySelectorAll(".cloud");

  moon.style.transform = `translate3d(0px, 0px, 0px)`;

  for(let i=0; i < clouds.length; ++i){
    setLeft(clouds[i], i);
  }


  function setLeft(item, i){
    item.style.transform = `translate3d(${i * 100}px, 0px, 0px)`;
  }

  function increment(item,i){
    let xPosition = +item.style.transform.split('px')[0].split('(')[1];
    let newXPosition = reset(xPosition,i);
    
    item.style.transform = `translate3d(${newXPosition}px, 0px, 0px)`;
  }

  function reset(xPosition, i){
    if(xPosition >= window.innerWidth){
      return 0;
    }
    else {
      return xPosition + i;
    }
  }


  setInterval(function(){
    clouds.forEach(increment,1);
  },100)

  setInterval(function(){
    increment(moon,1);
  },150)


})()

