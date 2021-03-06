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
$(function(){"use strict";new Morris.Bar({element:"morrisBar1",data:[{y:"2006",a:100,b:90},{y:"2007",a:75,b:65},{y:"2008",a:50,b:40},{y:"2009",a:75,b:65},{y:"2010",a:50,b:40}],xkey:"y",ykeys:["a","b"],labels:["Series A","Series B"],barColors:["#5058AB","#14A0C1"],gridTextSize:11,hideHover:"auto",resize:!0}),new Morris.Bar({element:"morrisBar2",data:[{y:"2006",a:100,b:90},{y:"2007",a:75,b:65},{y:"2008",a:50,b:40},{y:"2009",a:75,b:65},{y:"2010",a:50,b:40}],xkey:"y",ykeys:["a","b"],labels:["Series A","Series B"],barColors:["#5058AB","#14A0C1"],stacked:!0,gridTextSize:11,hideHover:"auto",resize:!0}),new Morris.Bar({element:"morrisBar3",data:[{y:"2006",a:100,b:90,c:80},{y:"2007",a:75,b:65,c:75},{y:"2008",a:50,b:40,c:45},{y:"2009",a:75,b:65,c:85}],xkey:"y",ykeys:["a","b","c"],labels:["Series A","Series B","Series C"],barColors:["#5058AB","#14A0C1","#01CB99"],gridTextSize:11,hideHover:"auto",resize:!0}),new Morris.Bar({element:"morrisBar4",data:[{y:"2006",a:100,b:90,c:80},{y:"2007",a:75,b:65,c:75},{y:"2008",a:50,b:40,c:45},{y:"2009",a:75,b:65,c:85},{y:"2009",a:65,b:60,c:60}],xkey:"y",ykeys:["a","b","c"],labels:["Series A","Series B","Series C"],barColors:["#5058AB","#14A0C1","#01CB99"],stacked:!0,gridTextSize:11,hideHover:"auto",resize:!0}),new Morris.Line({element:"morrisLine1",data:[{y:"2006",a:20,b:10},{y:"2007",a:30,b:15},{y:"2008",a:60,b:40},{y:"2009",a:40,b:25},{y:"2010",a:30,b:15},{y:"2011",a:45,b:20},{y:"2012",a:60,b:40}],xkey:"y",ykeys:["a","b"],labels:["Series A","Series B"],lineColors:["#14A0C1","#5058AB"],lineWidth:1,ymax:"auto 100",gridTextSize:11,hideHover:"auto",smooth:!1,resize:!0}),new Morris.Line({element:"morrisLine2",data:[{y:"2006",a:20,b:10,c:40},{y:"2007",a:30,b:15,c:45},{y:"2008",a:50,b:40,c:65},{y:"2009",a:40,b:25,c:55},{y:"2010",a:30,b:15,c:45},{y:"2011",a:45,b:20,c:65},{y:"2012",a:60,b:40,c:70}],xkey:"y",ykeys:["a","b","c"],labels:["Series A","Series B","Series C"],lineColors:["#14A0C1","#5058AB","#72DF00"],lineWidth:1,ymax:"auto 100",gridTextSize:11,hideHover:"auto",resize:!0}),new Morris.Area({element:"morrisArea1",data:[{y:"2006",a:50,b:40},{y:"2007",a:25,b:15},{y:"2008",a:20,b:40},{y:"2009",a:75,b:65},{y:"2010",a:50,b:40},{y:"2011",a:75,b:65},{y:"2012",a:100,b:90}],xkey:"y",ykeys:["a","b"],labels:["Series A","Series B"],lineColors:["#14A0C1","#5058AB"],lineWidth:1,fillOpacity:.5,gridTextSize:11,hideHover:"auto",resize:!0}),new Morris.Area({element:"morrisArea2",data:[{y:"2006",a:20,b:10,c:40},{y:"2007",a:30,b:15,c:45},{y:"2008",a:50,b:40,c:65},{y:"2009",a:40,b:25,c:55},{y:"2010",a:30,b:15,c:45},{y:"2011",a:45,b:20,c:65},{y:"2012",a:60,b:40,c:70}],xkey:"y",ykeys:["a","b","c"],labels:["Series A","Series B","Series C"],lineColors:["#14A0C1","#5058AB","#72DF00"],lineWidth:1,fillOpacity:.5,gridTextSize:11,hideHover:"auto",resize:!0}),new Morris.Donut({element:"morrisDonut1",data:[{label:"Men",value:12},{label:"Women",value:30},{label:"Kids",value:20}],colors:["#3D449C","#268FB2","#74DE00"],resize:!0}),new Morris.Donut({element:"morrisDonut2",data:[{label:"Men",value:12},{label:"Women",value:30},{label:"Kids",value:20},{label:"Infant",value:25}],colors:["#3D449C","#268FB2","#2DC486","#74DE00"],resize:!0})});