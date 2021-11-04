$(function(){

  let vh = window.innerHeight / 100
  let vw = document.documentElement.clientWidth / 100

  // реализация выпадения и скравания header-menu
  $('#dropdown-menu-btn').click(function(){
    let show = $(this).attr('show');

    if (show == 'false'){
      $(this).attr('show', 'true')
      $(this).addClass('dropdown-menu-btn--active')
      $('#dropdown-menu').animate({top: '113px'})
    }else{
      $(this).attr('show', 'false')
      $(this).removeClass('dropdown-menu-btn--active')
      $('#dropdown-menu').animate({top: '-100%'})
    }
  })
  // ---реализация выпадения и скравания header-menu
})
