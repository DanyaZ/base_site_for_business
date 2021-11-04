
$(function(){
  let vh = window.innerHeight / 100
  let vw = document.documentElement.clientWidth / 100




  // реализация slick слайдера новостей
  if(vw > 9.92){
    $('.news__items').slick({
      autoplay: false,
      dots: false,
      infinite: false,
      prevArrow: $('.news__btn-prev'),
      nextArrow: $('.news__btn-next'),
      slidesToShow: 3,
    }).on('setPosition', function (event) {
      $(".news__items .news__item-inner").css('height', $('.news__items').height() - 40 + 'px');
    });
  }else if(vw > 7){
    $('.news__items').slick({
      autoplay: false,
      dots: false,
      infinite: false,
      prevArrow: $('.news__btn-prev'),
      nextArrow: $('.news__btn-next'),
      slidesToShow: 2,
    }).on('setPosition', function (event) {
      $(".news__items .news__item-inner").css('height', $('.news__items').height() - 40 + 'px');
    });
  }else{
    $('.news__items').slick({
      autoplay: false,
      dots: false,
      infinite: false,
      prevArrow: $('.news__btn-prev'),
      nextArrow: $('.news__btn-next'),
      slidesToShow: 1,
    }).on('setPosition', function (event) {
      $(".news__items .news__item-inner").css('height', $('.news__items').height() - 40 + 'px');
    });
  }
  // ---реализация slick слайдера новостей

  // закрывание меню куки
  $(".cookies__btn").click(function(){
    $('.cookies').hide()
  })
  // ---закрывание меню куки

})
