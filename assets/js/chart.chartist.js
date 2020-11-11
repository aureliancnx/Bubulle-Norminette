/*
 * Copyright (c) 2020 aureliancnx
 *
 * MIT LICENSE
 *
 * This project is part of aureliancnx.
 * See https://github.com/aureliancnx/Bubulle-Norminette for further info.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE. */
$(function(){"use strict";var e=new Chartist.Line("#chartLine1",{labels:["Mon","Tue","Wed","Thu","Fri"],series:[[12,9,7,8,5]]},{high:30,axisY:{onlyInteger:!0},fullWidth:!0,chartPadding:{bottom:0,left:0}});new ResizeSensor($(".br-mainpanel"),function(){e.update()});var t=new Chartist.Line("#chartLine2",{labels:["Mon","Tue","Wed","Thu","Fri"],series:[[12,9,7,8,5],[2,1,5,7,3],[1,3,4,5,6]]},{high:30,axisY:{onlyInteger:!0},fullWidth:!0,chartPadding:{bottom:0,left:0}});new ResizeSensor($(".br-mainpanel"),function(){t.update()});var a=new Chartist.Line("#chartArea1",{labels:[1,2,3,4,5,6,7,8],series:[[5,9,7,8,5,3,5,4]]},{high:30,low:0,axisY:{onlyInteger:!0},showArea:!0,fullWidth:!0,chartPadding:{bottom:0,left:0}}),n=new Chartist.Line("#chartArea2",{labels:[1,2,3,4,5,6,7,8],series:[[5,9,7,8,5,3,5,4],[10,15,10,20,18,11,16,18]]},{high:30,low:0,axisY:{onlyInteger:!0},showArea:!0,fullWidth:!0,chartPadding:{bottom:0,left:0}});new ResizeSensor($(".br-mainpanel"),function(){a.update(),n.update()});var r=new Chartist.Bar("#chartBar1",{labels:[1,2,3,4,5,6,7,8],series:[[5,9,7,8,5,3,5,4]]},{high:30,low:0,axisY:{onlyInteger:!0},showArea:!0,fullWidth:!0,chartPadding:{bottom:0,left:0}}),i=new Chartist.Bar("#chartBar2",{labels:[1,2,3,4,5,6,7,8],series:[[5,9,7,8,5,3,5,4],[10,15,10,20,18,11,16,18]]},{high:30,low:0,axisY:{onlyInteger:!0},showArea:!0,fullWidth:!0,chartPadding:{bottom:0,left:0}});new ResizeSensor($(".br-mainpanel"),function(){r.update(),i.update()});var s=new Chartist.Bar("#chartBar3",{labels:["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],series:[[5,9,7,8,5,3,5]]},{high:30,low:0,axisY:{onlyInteger:!0},horizontalBars:!0,showArea:!0,fullWidth:!0,chartPadding:{bottom:0,left:40}}),o=new Chartist.Bar("#chartBar4",{labels:["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],series:[[5,9,7,8,5,3,5],[10,15,10,20,18,11,16]]},{high:30,low:0,axisY:{onlyInteger:!0},horizontalBars:!0,showArea:!0,fullWidth:!0,chartPadding:{bottom:0,left:40}});new ResizeSensor($(".br-mainpanel"),function(){s.update(),o.update()});var l=new Chartist.Bar("#chartBar5",{labels:["Q1","Q2","Q3","Q4"],series:[[8e5,12e5,14e5,13e5],[2e5,4e5,5e5,3e5],[1e5,2e5,4e5,6e5]]},{stackBars:!0,axisY:{labelInterpolationFnc:function(e){return e/1e3+"k"}}}).on("draw",function(e){"bar"===e.type&&e.element.attr({style:"stroke-width: 30px"})}),h=new Chartist.Bar("#chartBar6",{labels:["Q1","Q2","Q3","Q4"],series:[[8e5,12e5,14e5,13e5],[2e5,4e5,5e5,3e5],[1e5,2e5,4e5,6e5]]},{stackBars:!0,horizontalBars:!0,axisX:{labelInterpolationFnc:function(e){return e/1e3+"k"}},chartPadding:{bottom:0,left:0,right:40}}).on("draw",function(e){"bar"===e.type&&e.element.attr({style:"stroke-width: 30px"})});new ResizeSensor($(".br-mainpanel"),function(){l.update(),h.update()});function d(e,t){return e+t}var u={series:[5,3,4]},c=new Chartist.Pie("#chartPie1",u,{labelInterpolationFnc:function(e){return Math.round(e/u.series.reduce(d)*100)+"%"}}),w=new Chartist.Pie("#chartPie2",{series:[5,3,4,6,2]},{labelInterpolationFnc:function(e){return Math.round(e/u.series.reduce(d)*100)+"%"}});new ResizeSensor($(".br-mainpanel"),function(){c.update(),w.update()});var b=new Chartist.Pie("#chartDonut1",{series:[20,10,30]},{donut:!0,donutWidth:60,donutSolid:!0,startAngle:270,showLabel:!0}),f=new Chartist.Pie("#chartDonut2",{series:[20,10,30,40,25]},{donut:!0,donutWidth:60,donutSolid:!0,startAngle:270,showLabel:!0});new ResizeSensor($(".br-mainpanel"),function(){b.update(),f.update()})});