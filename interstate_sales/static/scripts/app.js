'use strict';

// function for mobile menu on page ready
$(function(){
  if (!sessionStorage.visited){
    $('.overlay').show();
  } else if (sessionStorage.visited = true) {
    $('.overlay').hide();
  }

  $('.hidden').hide();

  $('.burger img').on('click', function(){
    if ($('#nav').is(':visible')){
      $('#nav').slideUp('fast');
    } else {
      $('.subnav').hide();
      $('#nav').slideDown('fast');
    }
  });

  // ----hide menus when link is clicked -->
  $('#nav li a').on('click', function(){
    if ($('.subnav').is(':visible')){
      $('.subnav').hide();
    }
  });

  $('#subnav a').on('click', function(){
    $('.subnav').hide();
    $('#nav').hide();
  });
  // ------------------------------------

  // -----nav item submenu -->
  $('#guardrail').on('click', function(){
    $('#guardrail .subnav').slideDown('fast');
  });

  $('#paint').on('click', function(){
    $('#paint .subnav').slideDown('fast');
  });

  $('#markings').on('click', function(){
    $('#markings .subnav').slideDown('fast');
  });

  $('#safety').on('click', function(){
    $('#safety .subnav').slideDown('fast');
  });

  $('#signs').on('click', function(){
    $('#signs .subnav').slideDown('fast');
  });

  $('#equipment').on('click', function(){
    $('#equipment .subnav').slideDown('fast');
  });

  $('#team').on('click', function(){
    $('#team .subnav').slideDown('fast');
  });

  $('#downloads').on('click', function(){
    $('#downloads .subnav').slideDown('fast');
  });
  // --------------------------------------

  $('.overlay').on('click', function(){
    sessionStorage.visited = true;
    // console.log(visited);
    $('.overlay').fadeOut('slow');
  });

  // // hide nav into burger when width is small
  // $('#home, #about, #events').on('click', function(){
  //   if (window.innerWidth <= 739){
  //     $('#main-nav').slideUp('fast');
  //   }
  // });

  // displays dropdown list on click for mobile
  $('.dropdown').on('click', function(){
    if ($('.dropdown-content').is(':hidden')){
      // $('#project-list').animate({width: 'toggle'},350);
      $('.dropdown-content').slideDown();
    } else {
      $('.dropdown-content').slideUp();
    }
  });
});

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
// $(function(){
//   if (!sessionStorage.visited){
//     $('.overlay').show();
//   } else {
//     $('.overlay').hide();
//   }
//
//   $('.overlay').on('click', function(){
//     sessionStorage.visited = true;
//     // console.log(visited);
//     $('.overlay').fadeOut('slow');
//   });
// });

$(function () {
  $( window ).on("beforeunload", function() {
    sessionStorage.visited = false;
  });
});
