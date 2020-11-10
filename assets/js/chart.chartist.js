$(function(){
  'use strict'


  /************ LINE CHART 1 ***************/

  var line1 = new Chartist.Line('#chartLine1', {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    series: [
      [12, 9, 7, 8, 5]
    ]
  },{
    high: 30,
    axisY: {
      onlyInteger: true
    },
    fullWidth: true,
    chartPadding: {
      bottom: 0,
      left: 0
    }
  });

  // resize chart when container changest it's width
  new ResizeSensor($('.br-mainpanel'), function(){
    line1.update();
  });


  /*********** LINE CHART 2 ******************/
  var line2 = new Chartist.Line('#chartLine2', {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    series: [
      [12, 9, 7, 8, 5],
      [2, 1, 5, 7, 3],
      [1, 3, 4, 5, 6]
    ]
  },{
    high: 30,
    axisY: {
      onlyInteger: true
    },
    fullWidth: true,
    chartPadding: {
      bottom: 0,
      left: 0
    }
  });

  // resize chart when container changest it's width
  new ResizeSensor($('.br-mainpanel'), function(){
    line2.update();
  });


  /*********************** AREA CHART 1 *********************/

  var area1 = new Chartist.Line('#chartArea1', {
    labels: [1, 2, 3, 4, 5, 6, 7, 8],
    series: [
      [5, 9, 7, 8, 5, 3, 5, 4]
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

  var area2 = new Chartist.Line('#chartArea2', {
    labels: [1, 2, 3, 4, 5, 6, 7, 8],
    series: [
      [5, 9, 7, 8, 5, 3, 5, 4],
      [10, 15, 10, 20, 18, 11, 16, 18]
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

  // resize chart when container changest it's width
  new ResizeSensor($('.br-mainpanel'), function(){
    area1.update();
    area2.update();
  });


  /********************* BAR CHART ****************/
  var bar1 = new Chartist.Bar('#chartBar1', {
    labels: [1, 2, 3, 4, 5, 6, 7, 8],
    series: [
      [5, 9, 7, 8, 5, 3, 5, 4]
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

  var bar2 = new Chartist.Bar('#chartBar2', {
    labels: [1, 2, 3, 4, 5, 6, 7, 8],
    series: [
      [5, 9, 7, 8, 5, 3, 5, 4],
      [10, 15, 10, 20, 18, 11, 16, 18]
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


  // resize chart when container changest it's width
  new ResizeSensor($('.br-mainpanel'), function(){
    bar1.update();
    bar2.update();
  });


  /********************* HORIZONTAL BARS CHART ****************/

  var bar3 = new Chartist.Bar('#chartBar3', {
    labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    series: [
      [5, 9, 7, 8, 5, 3, 5]
    ]
  }, {
    high: 30,
    low: 0,
    axisY: {
      onlyInteger: true
    },
    horizontalBars: true,
    showArea: true,
    fullWidth: true,
    chartPadding: {
      bottom: 0,
      left: 40
    }
  });

  var bar4 = new Chartist.Bar('#chartBar4', {
    labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    series: [
      [5, 9, 7, 8, 5, 3, 5],
      [10, 15, 10, 20, 18, 11, 16]
    ]
  }, {
    high: 30,
    low: 0,
    axisY: {
      onlyInteger: true
    },
    horizontalBars: true,
    showArea: true,
    fullWidth: true,
    chartPadding: {
      bottom: 0,
      left: 40
    }
  });


  // resize chart when container changest it's width
  new ResizeSensor($('.br-mainpanel'), function(){
    bar3.update();
    bar4.update();
  });



  /***************** STACKED BAR CHARTS ********************/

  var bar5 = new Chartist.Bar('#chartBar5', {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    series: [
      [800000, 1200000, 1400000, 1300000],
      [200000, 400000, 500000, 300000],
      [100000, 200000, 400000, 600000]
    ]
  }, {
    stackBars: true,
    axisY: {
      labelInterpolationFnc: function(value) {
        return (value / 1000) + 'k';
      }
    }
  }).on('draw', function(data) {
    if(data.type === 'bar') {
      data.element.attr({
        style: 'stroke-width: 30px'
      });
    }
  });


  var bar6 = new Chartist.Bar('#chartBar6', {
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    series: [
      [800000, 1200000, 1400000, 1300000],
      [200000, 400000, 500000, 300000],
      [100000, 200000, 400000, 600000]
    ]
  }, {
    stackBars: true,
    horizontalBars: true,
    axisX: {
      labelInterpolationFnc: function(value) {
        return (value / 1000) + 'k';
      }
    },
    chartPadding: {
      bottom: 0,
      left: 0,
      right: 40
    }
  }).on('draw', function(data) {
    if(data.type === 'bar') {
      data.element.attr({
        style: 'stroke-width: 30px'
      });
    }
  });

  // resize chart when container changest it's width
  new ResizeSensor($('.br-mainpanel'), function(){
    bar5.update();
    bar6.update();
  });



  /********************* PIE CHART *********************/

  var sum = function(a, b) { return a + b };

  var data = {
    series: [5, 3, 4]
  };

  var pie1 = new Chartist.Pie('#chartPie1', data, {
    labelInterpolationFnc: function(value) {
      return Math.round(value / data.series.reduce(sum) * 100) + '%';
    }
  });


  /**************** PIE CHART 2 *******************/

  var data2 = {
    series: [5, 3, 4, 6, 2]
  };

  var pie2 = new Chartist.Pie('#chartPie2', data2, {
    labelInterpolationFnc: function(value) {
      return Math.round(value / data.series.reduce(sum) * 100) + '%';
    }
  });


  // resize chart when container changest it's width
  new ResizeSensor($('.br-mainpanel'), function(){
    pie1.update();
    pie2.update();
  });


  /**************** DONUT CHARTS ****************/
  var donut1 = new Chartist.Pie('#chartDonut1', {
    series: [20, 10, 30]
  }, {
    donut: true,
    donutWidth: 60,
    donutSolid: true,
    startAngle: 270,
    showLabel: true
  });

  var donut2 = new Chartist.Pie('#chartDonut2', {
    series: [20, 10, 30, 40, 25]
  }, {
    donut: true,
    donutWidth: 60,
    donutSolid: true,
    startAngle: 270,
    showLabel: true
  });

  // resize chart when container changest it's width
  new ResizeSensor($('.br-mainpanel'), function(){
    donut1.update();
    donut2.update();
  });


});
