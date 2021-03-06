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
!function(t){"object"==typeof exports&&"object"==typeof module?t(require("../../lib/codemirror")):"function"==typeof define&&define.amd?define(["../../lib/codemirror"],t):t(CodeMirror)}(function(t){"use strict";function e(t,e){function i(t){clearTimeout(n.doRedraw),n.doRedraw=setTimeout(function(){n.redraw()},t)}this.cm=t,this.options=e,this.buttonHeight=e.scrollButtonHeight||t.getOption("scrollButtonHeight"),this.annotations=[],this.doRedraw=this.doUpdate=null,this.div=t.getWrapperElement().appendChild(document.createElement("div")),this.div.style.cssText="position: absolute; right: 0; top: 0; z-index: 7; pointer-events: none",this.computeScale();var n=this;t.on("refresh",this.resizeHandler=function(){clearTimeout(n.doUpdate),n.doUpdate=setTimeout(function(){n.computeScale()&&i(20)},100)}),t.on("markerAdded",this.resizeHandler),t.on("markerCleared",this.resizeHandler),!1!==e.listenForChanges&&t.on("change",this.changeHandler=function(){i(250)})}t.defineExtension("annotateScrollbar",function(t){return"string"==typeof t&&(t={className:t}),new e(this,t)}),t.defineOption("scrollButtonHeight",0),e.prototype.computeScale=function(){var t=this.cm,e=(t.getWrapperElement().clientHeight-t.display.barHeight-2*this.buttonHeight)/t.getScrollerElement().scrollHeight;if(e!=this.hScale)return this.hScale=e,!0},e.prototype.update=function(t){this.annotations=t,this.redraw()},e.prototype.redraw=function(t){!1!==t&&this.computeScale();var i=this.cm,e=this.hScale,n=document.createDocumentFragment(),o=this.annotations,r=i.getOption("lineWrapping"),a=r&&1.5*i.defaultTextHeight(),s=null,h=null;function l(t,e){return s!=t.line&&(s=t.line,h=i.getLineHandle(s)),h.widgets&&h.widgets.length||r&&h.height>a?i.charCoords(t,"local")[e?"top":"bottom"]:i.heightAtLine(h,"local")+(e?0:h.height)}var d=i.lastLine();if(i.display.barWidth)for(var c,p=0;p<o.length;p++){var u=o[p];if(!(u.to.line>d)){for(var f,m,g=c||l(u.from,!0)*e,H=l(u.to,!1)*e;p<o.length-1&&!(o[p+1].to.line>d)&&!(H+.9<(c=l(o[p+1].from,!0)*e));)H=l((u=o[++p]).to,!1)*e;H!=g&&(f=Math.max(H-g,3),(m=n.appendChild(document.createElement("div"))).style.cssText="position: absolute; right: 0px; width: "+Math.max(i.display.barWidth-1,2)+"px; top: "+(g+this.buttonHeight)+"px; height: "+f+"px",m.className=this.options.className,u.id&&m.setAttribute("annotation-id",u.id))}}this.div.textContent="",this.div.appendChild(n)},e.prototype.clear=function(){this.cm.off("refresh",this.resizeHandler),this.cm.off("markerAdded",this.resizeHandler),this.cm.off("markerCleared",this.resizeHandler),this.changeHandler&&this.cm.off("change",this.changeHandler),this.div.parentNode.removeChild(this.div)}});