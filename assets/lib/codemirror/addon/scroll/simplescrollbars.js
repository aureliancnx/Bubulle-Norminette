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
!function(t){"object"==typeof exports&&"object"==typeof module?t(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],t):t(CodeMirror)}(function(h){"use strict";function i(t,e,o){this.orientation=e,this.scroll=o,this.screen=this.total=this.size=1,this.pos=0,this.node=document.createElement("div"),this.node.className=t+"-"+e,this.inner=this.node.appendChild(document.createElement("div"));var r=this;function i(t){var e=h.wheelEventPixels(t)["horizontal"==r.orientation?"x":"y"],o=r.pos;r.moveTo(r.pos+e),r.pos!=o&&h.e_preventDefault(t)}h.on(this.inner,"mousedown",function(t){var e,o,i;function n(){h.off(document,"mousemove",s),h.off(document,"mouseup",n)}function s(t){if(1!=t.which)return n();r.moveTo(i+(t[e]-o)*(r.total/r.size))}1==t.which&&(h.e_preventDefault(t),e="horizontal"==r.orientation?"pageX":"pageY",o=t[e],i=r.pos,h.on(document,"mousemove",s),h.on(document,"mouseup",n))}),h.on(this.node,"click",function(t){h.e_preventDefault(t);var e=r.inner.getBoundingClientRect(),o="horizontal"==r.orientation?t.clientX<e.left?-1:t.clientX>e.right?1:0:t.clientY<e.top?-1:t.clientY>e.bottom?1:0;r.moveTo(r.pos+o*r.screen)}),h.on(this.node,"mousewheel",i),h.on(this.node,"DOMMouseScroll",i)}i.prototype.setPos=function(t,e){return t<0&&(t=0),t>this.total-this.screen&&(t=this.total-this.screen),!(!e&&t==this.pos)&&(this.pos=t,this.inner.style["horizontal"==this.orientation?"left":"top"]=t*(this.size/this.total)+"px",!0)},i.prototype.moveTo=function(t){this.setPos(t)&&this.scroll(t,this.orientation)};function o(t,e,o){this.addClass=t,this.horiz=new i(t,"horizontal",o),e(this.horiz.node),this.vert=new i(t,"vertical",o),e(this.vert.node),this.width=null}i.prototype.update=function(t,e,o){var i=this.screen!=e||this.total!=t||this.size!=o;i&&(this.screen=e,this.total=t,this.size=o);var n=this.screen*(this.size/this.total);n<10&&(this.size-=10-n,n=10),this.inner.style["horizontal"==this.orientation?"width":"height"]=n+"px",this.setPos(this.pos,i)},o.prototype.update=function(t){var e;null!=this.width||(e=window.getComputedStyle?window.getComputedStyle(this.horiz.node):this.horiz.node.currentStyle)&&(this.width=parseInt(e.height));var o=this.width||0,i=t.scrollWidth>t.clientWidth+1,n=t.scrollHeight>t.clientHeight+1;return this.vert.node.style.display=n?"block":"none",this.horiz.node.style.display=i?"block":"none",n&&(this.vert.update(t.scrollHeight,t.clientHeight,t.viewHeight-(i?o:0)),this.vert.node.style.bottom=i?o+"px":"0"),i&&(this.horiz.update(t.scrollWidth,t.clientWidth,t.viewWidth-(n?o:0)-t.barLeft),this.horiz.node.style.right=n?o+"px":"0",this.horiz.node.style.left=t.barLeft+"px"),{right:n?o:0,bottom:i?o:0}},o.prototype.setScrollTop=function(t){this.vert.setPos(t)},o.prototype.setScrollLeft=function(t){this.horiz.setPos(t)},o.prototype.clear=function(){var t=this.horiz.node.parentNode;t.removeChild(this.horiz.node),t.removeChild(this.vert.node)},h.scrollbarModel.simple=function(t,e){return new o("CodeMirror-simplescroll",t,e)},h.scrollbarModel.overlay=function(t,e){return new o("CodeMirror-overlayscroll",t,e)}});