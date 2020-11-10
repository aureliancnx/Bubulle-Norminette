$(function(){
  'use strict';

  new Morris.Bar({
    element: 'morrisBar1',
    data: [
      { y: '2006', a: 100, b: 90 },
      { y: '2007', a: 75,  b: 65 },
      { y: '2008', a: 50,  b: 40 },
      { y: '2009', a: 75,  b: 65 },
      { y: '2010', a: 50,  b: 40 },
    ],
    xkey: 'y',
    ykeys: ['a', 'b'],
    labels: ['Series A', 'Series B'],
    barColors: ['#5058AB', '#14A0C1'],
    gridTextSize: 11,
    hideHover: 'auto',
    resize: true
  });

  new Morris.Bar({
    element: 'morrisBar2',
    data: [
      { y: '2006', a: 100, b: 90 },
      { y: '2007', a: 75,  b: 65 },
      { y: '2008', a: 50,  b: 40 },
      { y: '2009', a: 75,  b: 65 },
      { y: '2010', a: 50,  b: 40 },
    ],
    xkey: 'y',
    ykeys: ['a', 'b'],
    labels: ['Series A', 'Series B'],
    barColors: ['#5058AB', '#14A0C1'],
    stacked: true,
    gridTextSize: 11,
    hideHover: 'auto',
    resize: true
  });

  new Morris.Bar({
    element: 'morrisBar3',
    data: [
      { y: '2006', a: 100, b: 90, c: 80 },
      { y: '2007', a: 75,  b: 65, c: 75 },
      { y: '2008', a: 50,  b: 40, c: 45 },
      { y: '2009', a: 75,  b: 65, c: 85 },
    ],
    xkey: 'y',
    ykeys: ['a', 'b', 'c'],
    labels: ['Series A', 'Series B', 'Series C'],
    barColors: ['#5058AB', '#14A0C1','#01CB99'],
    gridTextSize: 11,
    hideHover: 'auto',
    resize: true
  });

  new Morris.Bar({
    element: 'morrisBar4',
    data: [
      { y: '2006', a: 100, b: 90, c: 80 },
      { y: '2007', a: 75,  b: 65, c: 75 },
      { y: '2008', a: 50,  b: 40, c: 45 },
      { y: '2009', a: 75,  b: 65, c: 85 },
      { y: '2009', a: 65,  b: 60, c: 60 },
    ],
    xkey: 'y',
    ykeys: ['a', 'b', 'c'],
    labels: ['Series A', 'Series B', 'Series C'],
    barColors: ['#5058AB', '#14A0C1','#01CB99'],
    stacked: true,
    gridTextSize: 11,
    hideHover: 'auto',
    resize: true
  });


  new Morris.Line({
    element: 'morrisLine1',
    data: [
      { y: '2006', a: 20, b: 10 },
      { y: '2007', a: 30,  b: 15 },
      { y: '2008', a: 60,  b: 40 },
      { y: '2009', a: 40,  b: 25 },
      { y: '2010', a: 30,  b: 15 },
      { y: '2011', a: 45,  b: 20 },
      { y: '2012', a: 60, b: 40 }
    ],
    xkey: 'y',
    ykeys: ['a', 'b'],
    labels: ['Series A', 'Series B'],
    lineColors: ['#14A0C1', '#5058AB'],
    lineWidth: 1,
    ymax: 'auto 100',
    gridTextSize: 11,
    hideHover: 'auto',
    smooth: false,
    resize: true
  });

  new Morris.Line({
    element: 'morrisLine2',
    data: [
      { y: '2006', a: 20, b: 10, c: 40 },
      { y: '2007', a: 30, b: 15, c: 45 },
      { y: '2008', a: 50, b: 40, c: 65 },
      { y: '2009', a: 40, b: 25, c: 55 },
      { y: '2010', a: 30, b: 15, c: 45 },
      { y: '2011', a: 45, b: 20, c: 65 },
      { y: '2012', a: 60, b: 40, c: 70 }
    ],
    xkey: 'y',
    ykeys: ['a', 'b', 'c'],
    labels: ['Series A', 'Series B', 'Series C'],
    lineColors: ['#14A0C1', '#5058AB', '#72DF00'],
    lineWidth: 1,
    ymax: 'auto 100',
    gridTextSize: 11,
    hideHover: 'auto',
    resize: true
  });

  new Morris.Area({
    element: 'morrisArea1',
    data: [
      { y: '2006', a: 50, b: 40 },
      { y: '2007', a: 25,  b: 15 },
      { y: '2008', a: 20,  b: 40 },
      { y: '2009', a: 75,  b: 65 },
      { y: '2010', a: 50,  b: 40 },
      { y: '2011', a: 75,  b: 65 },
      { y: '2012', a: 100, b: 90 }
    ],
    xkey: 'y',
    ykeys: ['a', 'b'],
    labels: ['Series A', 'Series B'],
    lineColors: ['#14A0C1', '#5058AB'],
    lineWidth: 1,
    fillOpacity: 0.5,
    gridTextSize: 11,
    hideHover: 'auto',
    resize: true
  });

  new Morris.Area({
    element: 'morrisArea2',
    data: [
      { y: '2006', a: 20, b: 10, c: 40 },
      { y: '2007', a: 30, b: 15, c: 45 },
      { y: '2008', a: 50, b: 40, c: 65 },
      { y: '2009', a: 40, b: 25, c: 55 },
      { y: '2010', a: 30, b: 15, c: 45 },
      { y: '2011', a: 45, b: 20, c: 65 },
      { y: '2012', a: 60, b: 40, c: 70 }
    ],
    xkey: 'y',
    ykeys: ['a', 'b', 'c'],
    labels: ['Series A', 'Series B', 'Series C'],
    lineColors: ['#14A0C1', '#5058AB', '#72DF00'],
    lineWidth: 1,
    fillOpacity: 0.5,
    gridTextSize: 11,
    hideHover: 'auto',
    resize: true
  });

  new Morris.Donut({
    element: 'morrisDonut1',
    data: [
      {label: "Men", value: 12},
      {label: "Women", value: 30},
      {label: "Kids", value: 20}
    ],
    colors: ['#3D449C','#268FB2','#74DE00'],
    resize: true
  });

  new Morris.Donut({
    element: 'morrisDonut2',
    data: [
      {label: "Men", value: 12},
      {label: "Women", value: 30},
      {label: "Kids", value: 20},
      {label: "Infant", value: 25}
    ],
    colors: ['#3D449C','#268FB2','#2DC486','#74DE00'],
    resize: true
  });

});
