$(function(){

  'use strict'

  /************************ BAR CHART 1 *************************/
  var chartdata = [
    {
      name: 'Oranges',
      type: 'bar',
      data: [20, 20, 36, 12, 15]
    },
    {
      name: 'Apples',
      type: 'bar',
      data: [8, 5, 25, 10, 10]
    }
  ];

  var chart = document.getElementById('chartBar1');
  var barChart = echarts.init(chart);

  var option = {
    grid: {
      top: '6',
      right: '0',
      bottom: '17',
      left: '25',
    },
    xAxis: {
      data: [ '2006', '2008', '2010', '2012', '2014'],
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    yAxis: {
      splitLine: {
        lineStyle: {
          color: '#ddd'
        }
      },
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    series: chartdata
  };

  barChart.setOption(option);


  /********************** BAR CHART 2 **************************/
  var chartdata2 = [
    {
      name: 'Oranges',
      type: 'bar',
      data: [20, 20, 36, 12, 15]
    },
    {
      name: 'Apples',
      type: 'bar',
      data: [8, 5, 25, 10, 10]
    },
    {
      name: 'Grapes',
      type: 'bar',
      data: [15, 10, 20, 20, 25]
    }
  ];

  var chart2 = document.getElementById('chartBar2');
  var barChart2 = echarts.init(chart2);

  var option2 = {
    grid: {
      top: '6',
      right: '0',
      bottom: '17',
      left: '25',
    },
    xAxis: {
      data: [ '2006', '2008', '2010', '2012', '2014'],
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    yAxis: {
      splitLine: {
        lineStyle: {
          color: '#ddd'
        }
      },
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    series: chartdata2,
    color:[ '#693391','#E7016E','#109EDC']
  };

  barChart2.setOption(option2);


  /***************** BAR CHART 3 ********************/
  var option3 = {
    grid: {
      top: '6',
      right: '0',
      bottom: '17',
      left: '32',
    },
    xAxis: {
      type: 'value',
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    yAxis: {
      type: 'category',
      data: [ '2006', '2008', '2010', '2012', '2014'],
      splitLine: {
        lineStyle: {
          color: '#ddd'
        }
      },
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    series: chartdata
  };

  var chart3 = document.getElementById('chartBar3');
  var barChart3 = echarts.init(chart3);
  barChart3.setOption(option3);


  /***************** BAR CHART 4 *********************/
  var option4 = {
    grid: {
      top: '6',
      right: '0',
      bottom: '17',
      left: '32',
    },
    xAxis: {
      type: 'value',
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    yAxis: {
      type: 'category',
      data: [ '2006', '2008', '2010', '2012', '2014'],
      splitLine: {
        lineStyle: {
          color: '#ddd'
        }
      },
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    series: chartdata2,
    color:[ '#693391','#E7016E','#109EDC']
  };

  var chart4 = document.getElementById('chartBar4');
  var barChart4 = echarts.init(chart4);
  barChart4.setOption(option4);


  

  /****************** STACKED BAR CHART ********************/
  var chartdata3 = [
    {
      name: 'Oranges',
      type: 'bar',
      stack: 'Stack',
      data: [20, 20, 36, 12, 15]
    },
    {
      name: 'Apples',
      type: 'bar',
      stack: 'Stack',
      data: [8, 5, 25, 10, 10]
    },
    {
      name: 'Grapes',
      type: 'bar',
      stack: 'Stack',
      data: [15, 10, 20, 20, 25]
    }
  ];

  var option5 = {
    grid: {
      top: '6',
      right: '0',
      bottom: '17',
      left: '25',
    },
    xAxis: {
      data: [ '2006', '2008', '2010', '2012', '2014'],
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    yAxis: {
      splitLine: {
        lineStyle: {
          color: '#ddd'
        }
      },
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    series: chartdata3
  };

  var chart5 = document.getElementById('chartBar5');
  var barChart5 = echarts.init(chart5);
  barChart5.setOption(option5);



  /****************** BAR CHART 6 *******************/
  var option6 = {
    grid: {
      top: '6',
      right: '10',
      bottom: '17',
      left: '32',
    },
    xAxis: {
      type: 'value',
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    yAxis: {
      type: 'category',
      data: [ '2006', '2008', '2010', '2012', '2014'],
      splitLine: {
        lineStyle: {
          color: '#ddd'
        }
      },
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    series: chartdata3
  };

  var chart6 = document.getElementById('chartBar6');
  var barChart6 = echarts.init(chart6);
  barChart6.setOption(option6);


  /********************** LINE CHART ***********************/
  var chartdata4 = [
    {
      name: 'Oranges',
      type: 'line',
      data: [20, 20, 36, 18, 15, 20, 25, 20]
    }
  ];

  var option7 = {
    grid: {
      top: '6',
      right: '0',
      bottom: '17',
      left: '25',
    },
    xAxis: {
      data: [ '2006', '2008', '2010', '2012', '2014', '2015','2016', '2017'],
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    yAxis: {
      splitLine: {
        lineStyle: {
          color: '#ddd'
        }
      },
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    series: chartdata4
  };

  var chart7 = document.getElementById('chartLine1');
  var lineChart = echarts.init(chart7);
  lineChart.setOption(option7);


  /** ***************** LINE CHART 2 ********************/
  var chartdata5 = [
    {
      name: 'Oranges',
      type: 'line',
      smooth: true,
      data: [20, 20, 36, 18, 15, 20, 25, 20]
    }
  ];

  var option8 = {
    grid: {
      top: '6',
      right: '0',
      bottom: '17',
      left: '25',
    },
    xAxis: {
      data: [ '2006', '2008', '2010', '2012', '2014', '2015','2016', '2017'],
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    yAxis: {
      splitLine: {
        lineStyle: {
          color: '#ddd'
        }
      },
      axisLine: {
        lineStyle: {
          color: '#ccc'
        }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    series: chartdata5,
    color:[ '#693391']
  };

  var chart8 = document.getElementById('chartLine2');
  var lineChart2 = echarts.init(chart8);
  lineChart2.setOption(option8);


  /*************** AREA CHARTS *****************/
  var areaData = [
    {
      name: 'Oranges',
      type: 'line',
      data: [20, 20, 36, 12, 15,25],
      lineStyle: {
        normal: { width: 1 }
      },
      itemStyle: {
        normal: {
          areaStyle: { type: 'default' }
        }
      }
    },
    {
      name: 'Apples',
      type: 'line',
      data: [8, 5, 25, 10, 10, 20],
      lineStyle: {
        normal: { width: 1 }
      },
      itemStyle: {
        normal: {
          areaStyle: { type: 'default' }
        }
      }
    }
  ];

  var optionArea = {
    grid: {
      top: '6',
      right: '12',
      bottom: '17',
      left: '25',
    },
    xAxis: {
      data: [ '2006', '2008', '2010', '2012', '2014', '2016'],
      boundaryGap: false,
      axisLine: {
        lineStyle: { color: '#ccc' }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    yAxis: {
      splitLine: {
        lineStyle: { color: '#ddd' }
      },
      axisLine: {
        lineStyle: { color: '#ccc' }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    series: areaData
  };


  var chartArea = document.getElementById('chartArea1');
  var areaChart = echarts.init(chartArea);
  areaChart.setOption(optionArea);


  /***************** AREA DATA 2 *****************/
  var areaData2 = [
    {
      name: 'Oranges',
      type: 'line',
      smooth: true,
      data: [20, 20, 36, 12, 15,25],
      lineStyle: {
        normal: { width: 1 }
      },
      itemStyle: {
        normal: {
          areaStyle: { type: 'default' }
        }
      }
    },
    {
      name: 'Apples',
      type: 'line',
      smooth: true,
      data: [8, 5, 25, 10, 10, 20],
      lineStyle: {
        normal: { width: 1 }
      },
      itemStyle: {
        normal: {
          areaStyle: { type: 'default' }
        }
      }
    }
  ];

  var optionArea2 = {
    grid: {
      top: '6',
      right: '12',
      bottom: '17',
      left: '25',
    },
    xAxis: {
      data: [ '2006', '2008', '2010', '2012', '2014', '2016'],
      boundaryGap: false,
      axisLine: {
        lineStyle: { color: '#ccc' }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    yAxis: {
      splitLine: {
        lineStyle: { color: '#ddd' }
      },
      axisLine: {
        lineStyle: { color: '#ccc' }
      },
      axisLabel: {
        fontSize: 10,
        color: '#666'
      }
    },
    series: areaData2,
    color:[ '#693391','#E7016E']
  };

  var chartArea2 = document.getElementById('chartArea2');
  var areaChart2 = echarts.init(chartArea2);
  areaChart2.setOption(optionArea2);


  /**************** PIE CHART ************/
  var pieData = [{
    name: 'Fruits',
    type: 'pie',
    radius: '80%',
    center: ['50%', '57.5%'],
    data: [
      {value: 335, name: 'Apple'},
      {value: 310, name: 'Orange'},
      {value: 234, name: 'Grapes'},
      {value: 135, name: 'Lemon'},
      {value: 154, name: 'Banana'}
    ],
    label: {
      normal: {
        fontFamily: 'Roboto, sans-serif',
        fontSize: 11
      }
    },
    labelLine: {
      normal: {
        show: false
      }
    },
    markLine: {
      lineStyle: {
        normal: {
          width: 1
        }
      }
    }
  }];

  var pieOption = {
    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b}: {c} ({d}%)',
      textStyle: {
        fontSize: 11,
        fontFamily: 'Roboto, sans-serif'
      }
    },
    series: pieData
  };

  var pie = document.getElementById('chartPie');
  var pieChart = echarts.init(pie);
  pieChart.setOption(pieOption);


  /**************** DONUT CHART ************/
  var donutData = [{
    name: 'Fruits',
    type: 'pie',
    radius: ['40%','80%'],
    center: ['50%', '57.5%'],
    data: [
      {value: 335, name: 'Apple'},
      {value: 310, name: 'Orange'},
      {value: 234, name: 'Grapes'},
      {value: 135, name: 'Lemon'},
      {value: 154, name: 'Banana'}
    ],
    label: {
      normal: {
        fontFamily: 'Roboto, sans-serif',
        fontSize: 11
      }
    },
    labelLine: {
      normal: {
        show: false
      }
    },
    markLine: {
      lineStyle: {
        normal: {
          width: 1
        }
      }
    }
  }];

  var donutOption = {
    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b}: {c} ({d}%)',
      textStyle: {
        fontSize: 11,
        fontFamily: 'Roboto, sans-serif'
      }
    },
    series: donutData
  };

  var donut = document.getElementById('chartDonut');
  var donutChart = echarts.init(donut);
  donutChart.setOption(donutOption);



  /** making all charts responsive when resize **/
  function resizeAllECharts() {
    barChart.resize();
    barChart2.resize();
    barChart3.resize();
    barChart4.resize();
    barChart5.resize();
    barChart6.resize();
    lineChart.resize();
    lineChart2.resize();
    areaChart.resize();
    areaChart2.resize();
    pieChart.resize();
    donutChart.resize();
  }

  new ResizeSensor($('.br-mainpanel'), function(){
    resizeAllECharts();
  });

});
