$(function(){

  let vh = window.innerHeight / 100
  let vw = document.documentElement.clientWidth / 100

  // реализация выпадения и скравания блока фильтров
  $('.show-filter').click(function(){
    let show = $('.filters').attr('show')

    if(show == 'false'){
      $('.filters').css('display', 'block')
      $('.filters').attr('show', 'true')
    }else if(show == 'true'){
      $('.filters').css('display', 'none')
      $('.filters').attr('show', 'false')
    }

  })
  // ---реализация выпадения и скравания блока фильтроы

  $('.blog__btn').click(function(){
    $('.filters').css('display', 'none')
    $('.filters').attr('show', 'false')
  })

  $('.filters__item').click( function(){
    if( $(this).attr('active') == 'false'){
      $(this).addClass('filters__item--active')
      $(this).attr('active', 'true')
    }else if
    ($(this).attr('active') == 'true'){
      $(this).removeClass('filters__item--active')
      $(this).attr('active', 'false')
    }
  })
})
// function viewDiv(){
//   document.getElementsByClassName("message").style.display = "none";
// };
