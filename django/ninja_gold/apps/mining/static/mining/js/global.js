if (document.getElementById("farm")) {
    setTimeout("submitForm()", 5000); // set timout
}

function moveCar(loc) {

  var car = document.getElementById('car');

  if (car.style.left == '') {
    left = 50
  } else {
    left = car.style.left
    if (left == '15%') {
      left = 15;
    } else if (left == '40%') {
      left = 40;
    } else if (left == '65%') {
      left = 65;
    } else if (left == '90%') {
      left = 90;
    }
  }

  if (loc == 'farm') {
    max = 15;
  } else if (loc == 'cave') {
    max = 40;
  } else if (loc == 'house') {
    max = 65;
  } else if (loc == 'casino') {
    max = 90;
  }

  var id = setInterval(frame, 8);
  function frame() {
    if (left == max) {
      clearInterval(id);
    } else {
      if( left > max) {
        left--;
      } else {
        left++;
      }
      car.style.left = left + '%';
    }
  }

}
