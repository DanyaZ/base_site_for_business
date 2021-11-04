$(function(){

  let vh = window.innerHeight / 100
  let vw = document.documentElement.clientWidth / 100

  // реализация выпадения и скравания блока истории клиентов
    $('.historis__item-bottom').click(function(){
      let parent = this.parentElement
      let open = parent.getAttribute('open')
      if(open == 'false'){
        parent.setAttribute('open', 'true');
        $(parent).addClass('historis__item--open')
      }else if(open === 'true'){
        parent.setAttribute('open', 'false')
        $(parent).removeClass('historis__item--open')
      }
    })
  // ---реализация выпадения и скравания блока истории клиентов
})
