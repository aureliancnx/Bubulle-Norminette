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
!function(e,t){"function"==typeof define&&define.amd?define(t):"object"==typeof exports?module.exports=t():e.ResizeSensor=t()}("undefined"!=typeof window?window:this,function(){if("undefined"==typeof window)return null;var A=window.requestAnimationFrame||window.mozRequestAnimationFrame||window.webkitRequestAnimationFrame||function(e){return window.setTimeout(e,20)};function i(e,t){var i=Object.prototype.toString.call(e),n="[object Array]"===i||"[object NodeList]"===i||"[object HTMLCollection]"===i||"[object Object]"===i||"undefined"!=typeof jQuery&&e instanceof jQuery||"undefined"!=typeof Elements&&e instanceof Elements,o=0,s=e.length;if(n)for(;o<s;o++)t(e[o]);else t(e)}var n=function(t,m){function w(){var i,n,o=[];this.add=function(e){o.push(e)},this.call=function(){for(i=0,n=o.length;i<n;i++)o[i].call()},this.remove=function(e){var t=[];for(i=0,n=o.length;i<n;i++)o[i]!==e&&t.push(o[i]);o=t},this.length=function(){return o.length}}i(t,function(e){var t,i,n,o,s,r,d,c,l,f,a,h,u,z,p,v,y;i=m,(t=e)&&(t.resizedAttached?t.resizedAttached.add(i):(t.resizedAttached=new w,t.resizedAttached.add(i),t.resizeSensor=document.createElement("div"),t.resizeSensor.className="resize-sensor",n="position: absolute; left: 0; top: 0; right: 0; bottom: 0; overflow: hidden; z-index: -1; visibility: hidden;",o="position: absolute; left: 0; top: 0; transition: 0s;",t.resizeSensor.style.cssText=n,t.resizeSensor.innerHTML='<div class="resize-sensor-expand" style="'+n+'"><div style="'+o+'"></div></div><div class="resize-sensor-shrink" style="'+n+'"><div style="'+o+' width: 200%; height: 200%"></div></div>',t.appendChild(t.resizeSensor),t.resizeSensor.offsetParent!==t&&(t.style.position="relative"),s=t.resizeSensor.childNodes[0],r=s.childNodes[0],d=t.resizeSensor.childNodes[1],h=t.offsetWidth,u=t.offsetHeight,(z=function(){r.style.width="100000px",r.style.height="100000px",s.scrollLeft=1e5,s.scrollTop=1e5,d.scrollLeft=1e5,d.scrollTop=1e5})(),p=function(){l=0,c&&(h=f,u=a,t.resizedAttached&&t.resizedAttached.call())},(y=function(e,t,i){e.attachEvent?e.attachEvent("on"+t,i):e.addEventListener(t,i)})(s,"scroll",v=function(){f=t.offsetWidth,a=t.offsetHeight,(c=f!=h||a!=u)&&!l&&(l=A(p)),z()}),y(d,"scroll",v)))}),this.detach=function(e){n.detach(t,e)}};return n.detach=function(e,t){i(e,function(e){e&&(e.resizedAttached&&"function"==typeof t&&(e.resizedAttached.remove(t),e.resizedAttached.length())||e.resizeSensor&&(e.contains(e.resizeSensor)&&e.removeChild(e.resizeSensor),delete e.resizeSensor,delete e.resizedAttached))})},n});