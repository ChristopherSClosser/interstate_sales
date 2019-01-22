'use strict';

// scroll to top - show hide arrow button
$(function(){
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
        $('.scrollup').fadeIn();
    } else {
        $('.scrollup').fadeOut();
    }
  })
});

// displays gallery imgs in slide show format
$(function () {
  /* time and transition settings */
  let change_img_time 	= 6000,
    transition_speed	= 400,
    simple_slideshow	= $('#slider'),
    listItems	= simple_slideshow.children('li'),
    listLen	= listItems.length, i	= 0,

    changeList = function () {
      listItems.eq(i).fadeOut(transition_speed, function () {
        i += 1;
        if (i === listLen) {
          i = 0;
        }
        listItems.eq(i).fadeIn(transition_speed);
      });
    };

  listItems.not(':first').hide();
  setInterval(changeList, change_img_time);
});

// splash control
$(function(){
  if (!sessionStorage.visited){
    $('.overlay').show();
  } else {
    $('.overlay').hide();
  }

  $('.overlay').on('click', function(){
    sessionStorage.visited = true;
    // console.log(visited);
    $('.overlay').fadeOut('slow');
  });
});
