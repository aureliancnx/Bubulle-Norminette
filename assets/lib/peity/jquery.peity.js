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
!function(S,e,L,x){var r=S.fn.peity=function(e,n){return i&&this.each(function(){var t=S(this),i=t.data("_peity");i?(e&&(i.type=e),S.extend(i.opts,n)):(i=new a(t,e,S.extend({},r.defaults[e],t.data("peity"),n)),t.change(function(){i.draw()}).data("_peity",i)),i.draw()}),this},a=function(t,i,e){this.$el=t,this.type=i,this.opts=e},t=a.prototype,N=t.svgElement=function(t,i){return S(e.createElementNS("http://www.w3.org/2000/svg",t)).attr(i)},i="createElementNS"in e&&N("svg",{})[0].createSVGRect;t.draw=function(){var t=this.opts;r.graphers[this.type].call(this,t),t.after&&t.after.call(this,t)},t.fill=function(){var e=this.opts.fill;return S.isFunction(e)?e:function(t,i){return e[i%e.length]}},t.prepare=function(t,i){return this.$svg||this.$el.hide().after(this.$svg=N("svg",{class:"peity"})),this.$svg.empty().data("peity",this).attr({height:i,width:t})},t.values=function(){return S.map(this.$el.text().split(this.opts.delimiter),function(t){return parseFloat(t)})},r.defaults={},r.graphers={},r.register=function(t,i,e){this.defaults[t]=i,this.graphers[t]=e},r.register("pie",{fill:["#ff9900","#fff4dd","#ffc66e"],radius:8},function(t){var i;t.delimiter||(i=this.$el.text().match(/[^0-9\.]/),t.delimiter=i?i[0]:",");var e,n,r=S.map(this.values(),function(t){return 0<t?t:0});"/"==t.delimiter&&(e=r[0],n=r[1],r=[e,L.max(0,n-e)]);for(var a=0,h=r.length,s=0;a<h;a++)s+=r[a];s||(h=2,r=[0,s=1]);var l=2*t.radius,p=this.prepare(t.width||l,t.height||l),o=p.width(),c=p.height(),f=o/2,u=c/2,d=L.min(f,u),g=t.innerRadius;"donut"!=this.type||g||(g=.5*d);for(var m=L.PI,v=this.fill(),y=this.scale=function(t,i){var e=t/s*m*2-m/2;return[i*L.cos(e)+f,i*L.sin(e)+u]},w=0,a=0;a<h;a++){var x,k,$,j,A,E,F=r[a],M=F/s;0!=M&&((j=1==M?g?N("path",{d:["M",f,k=u-d,"A",d,d,0,1,1,x=f-.01,k,"L",x,$=u-g,"A",g,g,0,1,0,f,$].join(" ")}):N("circle",{cx:f,cy:u,r:d}):(A=w+F,E=["M"].concat(y(w,d),"A",d,d,0,.5<M?1:0,1,y(A,d),"L"),g?E=E.concat(y(A,g),"A",g,g,0,.5<M?1:0,0,y(w,g)):E.push(f,u),w+=F,N("path",{d:E.join(" ")}))).attr("fill",v.call(this,F,a,r)),p.append(j))}}),r.register("donut",S.extend(!0,{},r.defaults.pie),function(t){r.graphers.pie.call(this,t)}),r.register("line",{delimiter:",",fill:"#c6d9fd",height:16,min:0,stroke:"#4d89f9",strokeWidth:1,width:32},function(t){var i=this.values();1==i.length&&i.push(i[0]);for(var e=L.max.apply(L,t.max==x?i:i.concat(t.max)),n=L.min.apply(L,t.min==x?i:i.concat(t.min)),r=this.prepare(t.width,t.height),a=t.strokeWidth,h=r.width(),s=r.height()-a,l=e-n,p=this.x=function(t){return t*(h/(i.length-1))},o=this.y=function(t){var i=s;return l&&(i-=(t-n)/l*s),i+a/2},c=o(L.max(n,0)),f=[0,c],u=0;u<i.length;u++)f.push(p(u),o(i[u]));f.push(h,c),t.fill&&r.append(N("polygon",{fill:t.fill,points:f.join(" ")})),a&&r.append(N("polyline",{fill:"none",points:f.slice(2,f.length-2).join(" "),stroke:t.stroke,"stroke-width":a,"stroke-linecap":"square"}))}),r.register("bar",{delimiter:",",fill:["#4D89F9"],height:16,min:0,padding:.1,width:32},function(t){for(var i=this.values(),e=L.max.apply(L,t.max==x?i:i.concat(t.max)),n=L.min.apply(L,t.min==x?i:i.concat(t.min)),r=this.prepare(t.width,t.height),a=r.width(),h=r.height(),s=e-n,l=t.padding,p=this.fill(),o=this.x=function(t){return t*a/i.length},c=this.y=function(t){return h-(s?(t-n)/s*h:1)},f=0;f<i.length;f++){var u,d=o(f+l),g=o(f+1-l)-d,m=i[f],v=c(m),y=v,w=v;s?m<0?y=c(L.min(e,0)):w=c(L.max(n,0)):u=1,0==(u=w-y)&&(u=1,0<e&&s&&y--),r.append(N("rect",{fill:p.call(this,m,f,i),x:d,y:y,width:g,height:u}))}})}(jQuery,document,Math);