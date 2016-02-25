window.addEventListener('load', function(){
  var list = {};
  var x = 3;
  console.log('boo');
  var next_btn = document.getElementById('next_item');
  var finish_btn = document.getElementById('finish');

  next_btn.addEventListener('click', function(){
    console.log("Boo");
    var item = document.getElementById('item').value;
    var cost = document.getElementById('cost').value;
    if(item == '' || cost == '') {
      alert('You must enter an item name and a value!');
    } else {
      var item_location = [random(100), random(100)];
      var index = list.length;
      list['name'] = cost;
      console.log(list);
    }
  });
});

function random(limit) {
  return Math.floor(Math.random() * limit);
}

