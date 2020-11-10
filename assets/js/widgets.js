$(function(){
  'use strict';


  $('#spark1').sparkline('html', {
    type: 'bar',
    barWidth: 8,
    height: 30,
    barColor: '#29B0D0',
    chartRangeMax: 12
  });

  $('#spark2').sparkline('html', {
    type: 'bar',
    barWidth: 8,
    height: 30,
    barColor: '#6F42C1',
    chartRangeMax: 12
  });

  $('#spark3').sparkline('html', {
    type: 'bar',
    barWidth: 8,
    height: 30,
    barColor: '#20C997',
    chartRangeMax: 12
  });

  $('#spark4').sparkline('html', {
    type: 'bar',
    barWidth: 8,
    height: 30,
    barColor: '#0866C6',
    chartRangeMax: 12
  });

  // peity charts
  $('.peity-line').peity('line');
  $('.peity-donut').peity('donut');


  var rs1 = new Rickshaw.Graph({
    element: document.querySelector('#rickshaw1'),
    renderer: 'bar',
    stack: false,
    max: 50,
    series: [{
      data: [
        { x: 0, y: 20 },
        { x: 1, y: 25 },
        { x: 2, y: 10 },
        { x: 3, y: 15 },
        { x: 4, y: 20 },
        { x: 5, y: 40 },
        { x: 6, y: 15 },
        { x: 7, y: 40 },
        { x: 8, y: 25 }
      ],
      color: '#5058AB'
    },
    {
      data: [
        { x: 0, y: 10 },
        { x: 1, y: 30 },
        { x: 2, y: 45 },
        { x: 3, y: 30 },
        { x: 4, y: 42 },
        { x: 5, y: 20 },
        { x: 6, y: 30 },
        { x: 7, y: 15 },
        { x: 8, y: 20 }
      ],
      color: '#14A0C1'
    }]
  });

  rs1.render();

  // Responsive Mode
  new ResizeSensor($('.br-mainpanel'), function(){
    rs1.configure({
      width: $('#rickshaw1').width(),
      height: $('#rickshaw1').height()
    });
    rs1.render();
  });

  var rs2 = new Rickshaw.Graph({
    element: document.querySelector('#rickshaw2'),
    renderer: 'area',
    max: 50,
    series: [{
      data: [
        { x: 0, y: 40 },
        { x: 1, y: 49 },
        { x: 2, y: 38 },
        { x: 3, y: 30 },
        { x: 4, y: 32 },
        { x: 5, y: 40 },
        { x: 6, y: 20 },
        { x: 7, y: 10 },
        { x: 8, y: 20 },
        { x: 9, y: 25 },
        { x: 10, y: 35 },
        { x: 11, y: 20 },
        { x: 12, y: 40 },
        { x: 13, y: 25 }
      ],
      color: '#01CB99'
    }]
  });
  rs2.render();

  // Responsive Mode
  new ResizeSensor($('.br-mainpanel'), function(){
    rs2.configure({
      width: $('#rickshaw2').width(),
      height: $('#rickshaw2').height()
    });
    rs2.render();
  });

  var ch5 = new Rickshaw.Graph({
    element: document.querySelector('#ch5'),
    renderer: 'area',
    max: 80,
    series: [{
      data: [
        { x: 0, y: 40 },
        { x: 1, y: 45 },
        { x: 2, y: 30 },
        { x: 3, y: 40 },
        { x: 4, y: 50 },
        { x: 5, y: 40 },
        { x: 6, y: 20 },
        { x: 7, y: 10 },
        { x: 8, y: 20 },
        { x: 9, y: 25 },
        { x: 10, y: 35 },
        { x: 11, y: 20 },
        { x: 12, y: 40 }
      ],
      color: '#0866C6'
    }]
  });
  ch5.render();

  // Responsive Mode
  new ResizeSensor($('.br-mainpanel'), function(){
    ch5.configure({
      width: $('#ch5').width(),
      height: $('#ch5').height()
    });
    ch5.render();
  });

  var ch6 = new Rickshaw.Graph({
    element: document.querySelector('#ch6'),
    renderer: 'area',
    max: 80,
    series: [{
      data: [
        { x: 0, y: 40 },
        { x: 1, y: 45 },
        { x: 2, y: 30 },
        { x: 3, y: 40 },
        { x: 4, y: 50 },
        { x: 5, y: 40 },
        { x: 6, y: 20 },
        { x: 7, y: 10 },
        { x: 8, y: 20 },
        { x: 9, y: 25 },
        { x: 10, y: 35 },
        { x: 11, y: 20 },
        { x: 12, y: 40 }
      ],
      color: '#6F42C1'
    }]
  });
  ch6.render();

  // Responsive Mode
  new ResizeSensor($('.br-mainpanel'), function(){
    ch6.configure({
      width: $('#ch6').width(),
      height: $('#ch6').height()
    });
    ch6.render();
  });

  var ch7 = new Rickshaw.Graph({
    element: document.querySelector('#ch7'),
    renderer: 'area',
    max: 80,
    series: [{
      data: [
        { x: 0, y: 40 },
        { x: 1, y: 45 },
        { x: 2, y: 30 },
        { x: 3, y: 40 },
        { x: 4, y: 50 },
        { x: 5, y: 40 },
        { x: 6, y: 20 },
        { x: 7, y: 10 },
        { x: 8, y: 20 },
        { x: 9, y: 25 },
        { x: 10, y: 35 },
        { x: 11, y: 20 },
        { x: 12, y: 40 }
      ],
      color: '#20C997'
    }]
  });
  ch7.render();

  // Responsive Mode
  new ResizeSensor($('.br-mainpanel'), function(){
    ch7.configure({
      width: $('#ch7').width(),
      height: $('#ch7').height()
    });
    ch7.render();
  });

  var ch8 = new Rickshaw.Graph({
    element: document.querySelector('#ch8'),
    renderer: 'area',
    max: 50,
    series: [{
      data: [
        { x: 0, y: 40 },
        { x: 1, y: 49 },
        { x: 2, y: 38 },
        { x: 3, y: 30 },
        { x: 4, y: 32 },
        { x: 5, y: 40 },
        { x: 6, y: 20 },
        { x: 7, y: 10 },
        { x: 8, y: 20 },
        { x: 9, y: 25 },
        { x: 10, y: 35 },
        { x: 11, y: 20 },
        { x: 12, y: 35 }
      ],
      color: '#0866C6'
    }]
  });
  ch8.render();

  // Responsive Mode
  new ResizeSensor($('.br-mainpanel'), function(){
    ch8.configure({
      width: $('#ch8').width(),
      height: $('#ch8').height()
    });
    ch8.render();
  });

  var ch9 = new Rickshaw.Graph({
    element: document.querySelector('#ch9'),
    renderer: 'area',
    max: 50,
    series: [{
      data: [
        { x: 0, y: 35 },
        { x: 1, y: 49 },
        { x: 2, y: 38 },
        { x: 3, y: 30 },
        { x: 4, y: 32 },
        { x: 5, y: 40 },
        { x: 6, y: 20 },
        { x: 7, y: 10 },
        { x: 8, y: 20 },
        { x: 9, y: 25 },
        { x: 10, y: 35 },
        { x: 11, y: 20 },
        { x: 12, y: 40 }
      ],
      color: '#0866C6'
    }]
  });
  ch9.render();

  // Responsive Mode
  new ResizeSensor($('.br-mainpanel'), function(){
    ch9.configure({
      width: $('#ch9').width(),
      height: $('#ch9').height()
    });
    ch9.render();
  });


  var ch10 = new Rickshaw.Graph({
    element: document.querySelector('#ch10'),
    renderer: 'bar',
    max: 50,
    series: [{
      data: [
        { x: 0, y: 40 },
        { x: 1, y: 49 },
        { x: 2, y: 38 },
        { x: 3, y: 30 },
        { x: 4, y: 32 },
        { x: 5, y: 40 },
        { x: 6, y: 20 },
        { x: 7, y: 10 },
        { x: 8, y: 20 },
        { x: 9, y: 25 },
        { x: 10, y: 35 },
        { x: 11, y: 20 },
        { x: 12, y: 35 }
      ],
      color: '#6F42C1'
    }]
  });
  ch10.render();

  // Responsive Mode
  new ResizeSensor($('.br-mainpanel'), function(){
    ch10.configure({
      width: $('#ch10').width(),
      height: $('#ch10').height()
    });
    ch10.render();
  });

  var ch11 = new Rickshaw.Graph({
    element: document.querySelector('#ch11'),
    renderer: 'bar',
    max: 50,
    series: [{
      data: [
        { x: 0, y: 35 },
        { x: 1, y: 49 },
        { x: 2, y: 38 },
        { x: 3, y: 30 },
        { x: 4, y: 32 },
        { x: 5, y: 40 },
        { x: 6, y: 20 },
        { x: 7, y: 10 },
        { x: 8, y: 20 },
        { x: 9, y: 25 },
        { x: 10, y: 35 },
        { x: 11, y: 20 },
        { x: 12, y: 40 }
      ],
      color: '#6F42C1'
    }]
  });
  ch11.render();

  // Responsive Mode
  new ResizeSensor($('.br-mainpanel'), function(){
    ch11.configure({
      width: $('#ch11').width(),
      height: $('#ch11').height()
    });
    ch11.render();
  });

});
