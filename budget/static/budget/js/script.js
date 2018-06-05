
(function(){
  document.querySelector('#categoryInput').addEventListener('keydown', function(e){
    if (e.keyCode != 13) {
      return;
    }

    e.preventDefault();

    var categoryName = this.value;
    this.value = '';
    addNewCategory(categoryName);
    updateCategoriesString();

  })

  function addNewCategory(name){

    document.querySelector('#categorylist').insertAdjacentHTML('beforeend', '<li class="mycategory"><span class="name">'+name+'</span><span onclick="removeCategory(this)"><i class="fas fa-ban"></i></span></li>');
  }


})()

function fetchCategoryArray(){
  var categories = []
  document.querySelectorAll('.mycategory').forEach(function(e){
    name=e.querySelector('.name').innerHTML
    if(name==''){
      return;
    }
    categories.push(name)
  })

  return categories;
}


function updateCategoriesString(){
    categories = fetchCategoryArray()
    document.querySelector('input[name="categoriesString"]').value=categories.join(',')
}



function removeCategory(e){
  e.parentElement.remove()
  updateCategoriesString()
}
