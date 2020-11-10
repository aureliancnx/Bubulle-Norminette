$(function(){
  'use strict'

  var ch1 = new Chartist.Line('#ch1', {
    labels: [1, 2, 3, 4, 5, 6, 7, 8],
    series: [
      [5, 9, 7, 8, 5, 3, 5, 4],
      [10, 15, 10, 17, 8, 11, 16, 10]
    ]
  }, {
    high: 30,
    low: 0,
    axisY: {
      onlyInteger: true
    },
    showArea: true,
    fullWidth: true,
    chartPadding: {
      bottom: 0,
      left: 0
    }
  });

  new ResizeSensor($('.br-mainpanel'), function(){
    ch1.update();
    ch1.update();
  });

  $('.peity-line').peity('line');
  $('.peity-donut').peity('donut');

});
