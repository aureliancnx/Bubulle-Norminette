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
"use strict";$(document).ready(function(){$(".show-sub + .br-menu-sub").slideDown(),$("#btnLeftMenu").on("click",function(){var s=$(".menu-item-label,.menu-item-arrow");return $("body").hasClass("collapsed-menu")?($("body").removeClass("collapsed-menu"),$(".show-sub + .br-menu-sub").slideDown(),$(".br-sideleft").one("transitionend",function(e){s.removeClass("op-lg-0-force"),s.removeClass("d-lg-none")})):($("body").addClass("collapsed-menu"),$(".show-sub + .br-menu-sub").slideUp(),s.addClass("op-lg-0-force"),$(".br-sideleft").one("transitionend",function(e){s.addClass("d-lg-none")})),!1}),$(document).on("mouseover",function(e){var s;e.stopPropagation(),$("body").hasClass("collapsed-menu")&&$("#btnLeftMenu").is(":visible")&&($(e.target).closest(".br-sideleft").length?($("body").addClass("expand-menu"),$(".show-sub + .br-menu-sub").slideDown(),(s=$(".menu-item-label,.menu-item-arrow")).removeClass("d-lg-none"),s.removeClass("op-lg-0-force")):($("body").removeClass("expand-menu"),$(".show-sub + .br-menu-sub").slideUp(),(s=$(".menu-item-label,.menu-item-arrow")).addClass("op-lg-0-force"),s.addClass("d-lg-none")))}),$(".br-menu-link").on("click",function(){var e=$(this).next(),s=$(this);if(e.hasClass("br-menu-sub"))return e.is(":visible")?(s.removeClass("show-sub"),e.slideUp()):($(".br-menu-link").each(function(){$(this).removeClass("show-sub")}),$(".br-menu-sub").each(function(){$(this).slideUp()}),s.addClass("show-sub"),e.slideDown()),!1}),$("#btnLeftMenuMobile").on("click",function(){return $("body").addClass("show-left"),!1}),$("#btnRightMenu").on("click",function(){return $("body").addClass("show-right"),!1}),$(document).on("click",function(e){e.stopPropagation(),$("body").hasClass("show-left")&&($(e.target).closest(".br-sideleft").length||$("body").removeClass("show-left")),$("body").hasClass("show-right")&&($(e.target).closest(".br-sideright").length||$("body").removeClass("show-right"))});setInterval(function(){var e=moment();$("#brDate").html(e.format("MMMM DD, YYYY")+" "+e.format("dddd").substring(0,3).toUpperCase()),$("#brTime").html(e.format("hh:mm:ss A"))},100);$().datepicker&&$(".form-control-datepicker").datepicker().on("change",function(e){console.log("Date changed: ",e.target.value)}),$(".overflow-y-auto").perfectScrollbar(),$(".datepicker").datepicker(),$(".switch-button").switchButton(),$(".peity-bar").peity("bar"),$("pre code").each(function(e,s){hljs.highlightBlock(s)}),$('[data-toggle="tooltip"]').tooltip(),$('[data-popover-color="default"]').popover(),$(document).on("click",function(e){$('[data-toggle="popover"],[data-original-title]').each(function(){$(this).is(e.target)||0!==$(this).has(e.target).length||0!==$(".popover").has(e.target).length||((($(this).popover("hide").data("bs.popover")||{}).inState||{}).click=!1)})}),$().select2&&($(".select2").select2({minimumResultsForSearch:1/0}),$(".select2-show-search").select2({minimumResultsForSearch:""}),$(".select2-tag").select2({tags:!0,tokenSeparators:[","," "]}))});