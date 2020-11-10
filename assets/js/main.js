
 'use strict';

 $(document).ready(function(){
  $('.show-sub + .br-menu-sub').slideDown();
  $('#btnLeftMenu').on('click', function(){
    var menuText = $('.menu-item-label,.menu-item-arrow');
    if($('body').hasClass('collapsed-menu')) {
      $('body').removeClass('collapsed-menu');
      $('.show-sub + .br-menu-sub').slideDown();
      $('.br-sideleft').one('transitionend', function(e) {
        menuText.removeClass('op-lg-0-force');
        menuText.removeClass('d-lg-none');
      });
    } else {
      $('body').addClass('collapsed-menu');
      $('.show-sub + .br-menu-sub').slideUp();
      menuText.addClass('op-lg-0-force');
      $('.br-sideleft').one('transitionend', function(e) {
        menuText.addClass('d-lg-none');
      });
    }
    return false;
  });
  $(document).on('mouseover', function(e){
    e.stopPropagation();
    if($('body').hasClass('collapsed-menu') && $('#btnLeftMenu').is(':visible')) {
      var targ = $(e.target).closest('.br-sideleft').length;
      if(targ) {
        $('body').addClass('expand-menu');
        $('.show-sub + .br-menu-sub').slideDown();
        var menuText = $('.menu-item-label,.menu-item-arrow');
        menuText.removeClass('d-lg-none');
        menuText.removeClass('op-lg-0-force');
      } else {
        $('body').removeClass('expand-menu');
        $('.show-sub + .br-menu-sub').slideUp();
        var menuText = $('.menu-item-label,.menu-item-arrow');
        menuText.addClass('op-lg-0-force');
        menuText.addClass('d-lg-none');
      }
    }
  });
  $('.br-menu-link').on('click', function(){
    var nextElem = $(this).next();
    var thisLink = $(this);
    if(nextElem.hasClass('br-menu-sub')) {
      if(nextElem.is(':visible')) {
        thisLink.removeClass('show-sub');
        nextElem.slideUp();
      } else {
        $('.br-menu-link').each(function(){
          $(this).removeClass('show-sub');
        });
        $('.br-menu-sub').each(function(){
          $(this).slideUp();
        });
        thisLink.addClass('show-sub');
        nextElem.slideDown();
      }
      return false;
    }
  });
  $('#btnLeftMenuMobile').on('click', function(){
    $('body').addClass('show-left');
    return false;
  });
  $('#btnRightMenu').on('click', function(){
    $('body').addClass('show-right');
    return false;
  });
  $(document).on('click', function(e){
    e.stopPropagation();
    if($('body').hasClass('show-left')) {
      var targ = $(e.target).closest('.br-sideleft').length;
      if(!targ) {
        $('body').removeClass('show-left');
      }
    }
    if($('body').hasClass('show-right')) {
      var targ = $(e.target).closest('.br-sideright').length;
      if(!targ) {
        $('body').removeClass('show-right');
      }
    }
  });
  var interval = setInterval(function() {
    var momentNow = moment();
    $('#brDate').html(momentNow.format('MMMM DD, YYYY') + ' '
      + momentNow.format('dddd')
      .substring(0,3).toUpperCase());
      $('#brTime').html(momentNow.format('hh:mm:ss A'));
  }, 100);
  if($().datepicker) {
    $('.form-control-datepicker').datepicker()
      .on("change", function (e) {
        console.log("Date changed: ", e.target.value);
    });
  }
  $('.overflow-y-auto').perfectScrollbar();
  $('.datepicker').datepicker();
  $('.switch-button').switchButton();
  $('.peity-bar').peity('bar');
  $('pre code').each(function(i, block) {
    hljs.highlightBlock(block);
  });
  $('[data-toggle="tooltip"]').tooltip();
  $('[data-popover-color="default"]').popover();
  $(document).on('click', function (e) {
    $('[data-toggle="popover"],[data-original-title]').each(function () {
        if (!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('.popover').has(e.target).length === 0) {
            (($(this).popover('hide').data('bs.popover')||{}).inState||{}).click = false  // fix for BS 3.3.6
        }
    });
  });
  if($().select2) {
    $('.select2').select2({
      minimumResultsForSearch: Infinity
    });
    $('.select2-show-search').select2({
      minimumResultsForSearch: ''
    });
    $('.select2-tag').select2({
      tags: true,
      tokenSeparators: [',', ' ']
    });
  }
});