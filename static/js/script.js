(function(){

  var clouds = document.querySelectorAll(".cloud");

  for(let i=0; i < clouds.length; ++i){
    setLeft(clouds[i], i);
  }


  function setLeft(item, i){
    item.style.transform = `translate3d(${i * 100}px, 0px, 0px)`;
  }

  function increment(item){
    let xPosition = +item.style.transform.split('px')[0].split('(')[1];
    let newXPosition = reset(xPosition);
    
    item.style.transform = `translate3d(${newXPosition}px, 0px, 0px)`;
  }

  function reset(xPosition){
    if(xPosition >= window.innerWidth){
      return 0;
    }
    else {
      return xPosition + 1;
    }
  }


  setInterval(function(){
    clouds.forEach(increment);
  },50)


})()

