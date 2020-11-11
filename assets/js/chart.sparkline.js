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
$(function(){"use strict";$("#sparkline1").sparkline("html",{width:200,height:70,lineColor:"#0083CD",fillColor:!1}),$("#sparkline2").sparkline("html",{width:200,height:70,lineColor:"#B654C3",fillColor:!1}),$("#sparkline3").sparkline("html",{width:200,height:70,lineColor:"#0083CD",fillColor:"rgba(0,131,205,0.2)"}),$("#sparkline4").sparkline("html",{width:200,height:70,lineColor:"#B654C3",fillColor:"rgba(182,84,195,0.2)"}),$("#sparkline5").sparkline("html",{type:"bar",barWidth:10,height:70,barColor:"#0083CD",chartRangeMax:12}),$("#sparkline6").sparkline("html",{type:"bar",barWidth:10,height:70,barColor:"#B654C3",chartRangeMax:12}),$("#sparkline7").sparkline("html",{type:"bar",barWidth:10,height:70,barColor:"#0083CD",chartRangeMax:12}),$("#sparkline7").sparkline([4,5,6,7,4,5,8,7,6,6,4,7,6,4,7],{composite:!0,type:"bar",barWidth:10,height:70,barColor:"#11546F",chartRangeMax:12}),$("#sparkline8").sparkline("html",{type:"bar",barWidth:10,height:70,barColor:"#E97B9E",chartRangeMax:12}),$("#sparkline8").sparkline([4,5,6,7,4,5,8,7,6,6,4,7,6,4,7],{composite:!0,type:"bar",barWidth:10,height:70,barColor:"#92288D",chartRangeMax:12}),$("#sparkline9").sparkline("html",{type:"pie",height:70,sliceColors:["#F4C62B","#F6931E","#8CC63E"]}),$("#sparkline10").sparkline("html",{type:"pie",height:70,sliceColors:["#F4C62B","#F6931E","#8CC63E","#93268F","#EB1E79","#828BC4","#E97A9B","#0083CD"]})});