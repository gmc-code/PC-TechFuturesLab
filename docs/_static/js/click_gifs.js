// Click-to-play GIFs.
// Any image with the class "clickgif" shows its first frame and a play button.
// Click (or press Enter / Space) to play it once; click again to stop early.
//
// In RST:
//   .. figure:: images/gifs/bounce.gif
//      :class: clickgif clickgif-ms-1200
//
// clickgif-ms-N sets how long it plays for, in milliseconds. Leave it out and
// the length of one run is read from the GIF file (or 3 seconds if that fails).
// Put GIFs inside an element with the class "clickgif-group" (for example a
// sphinx-design grid with :class-container: clickgif-group) and one click
// plays them all together.
(function () {
  "use strict";

  var css =
    ".clickgif-wrap{position:relative;display:inline-block;max-width:100%;cursor:pointer;line-height:0}" +
    ".clickgif-wrap canvas,.clickgif-wrap img{max-width:100%;height:auto}" +
    ".clickgif-wrap.is-stopped img{display:none}" +
    ".clickgif-wrap.is-playing canvas{display:none}" +
    ".clickgif-btn{position:absolute;right:6px;bottom:6px;border:2px solid #fff;" +
    "width:30px;height:30px;border-radius:50%;background:rgba(31,59,99,.85);color:#fff;" +
    "font:12px/26px sans-serif;text-align:center;padding-left:3px;box-sizing:border-box;" +
    "box-shadow:0 2px 8px rgba(0,0,0,.35);pointer-events:none;transition:opacity .2s}" +
    ".clickgif-wrap.is-playing .clickgif-btn,.clickgif-wrap.is-starting .clickgif-btn{opacity:0;transition:none}" +
    ".clickgif-wrap:focus{outline:3px solid #f9c80e;outline-offset:2px}";
  var style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  // Read the total time of one run through a GIF (sum of frame delays).
  function gifLength(bytes) {
    var d = new Uint8Array(bytes), p = 13, total = 0;
    if (d[10] & 0x80) p += 3 * (1 << ((d[10] & 7) + 1));
    while (p < d.length) {
      var b = d[p];
      if (b === 0x21) {
        if (d[p + 1] === 0xf9) total += (d[p + 4] | (d[p + 5] << 8)) * 10;
        p += 2;
        while (d[p]) p += d[p] + 1;
        p += 1;
      } else if (b === 0x2c) {
        var f = d[p + 9];
        p += 10;
        if (f & 0x80) p += 3 * (1 << ((f & 7) + 1));
        p += 1;
        while (d[p]) p += d[p] + 1;
        p += 1;
      } else break;
    }
    return total;
  }

  function setUp(img) {
    var src = img.getAttribute("src");
    var ms = 0;
    img.className.split(/\s+/).forEach(function (c) {
      var m = c.match(/^clickgif-ms-(\d+)$/);
      if (m) ms = parseInt(m[1], 10);
    });

    // Sphinx wraps sized images in a link to the full file; remove it so a
    // click plays the GIF instead of opening it.
    var link = img.parentNode;
    if (link && link.tagName === "A" && link.classList.contains("image-reference")) {
      link.parentNode.insertBefore(img, link);
      link.parentNode.removeChild(link);
    }

    var wrap = document.createElement("span");
    wrap.className = "clickgif-wrap is-stopped";
    wrap.setAttribute("role", "button");
    wrap.setAttribute("tabindex", "0");
    wrap.setAttribute("aria-label", "Play animation: " + (img.alt || "GIF"));
    img.parentNode.insertBefore(wrap, img);
    wrap.appendChild(img);

    var canvas = document.createElement("canvas");
    canvas.setAttribute("aria-hidden", "true");
    var btn = document.createElement("span");
    btn.className = "clickgif-btn";
    btn.textContent = "▶";
    wrap.appendChild(canvas);
    wrap.appendChild(btn);

    // Copy width set in RST (style or width attribute) onto the canvas.
    if (img.style.width) canvas.style.width = img.style.width;
    else if (img.getAttribute("width")) canvas.style.width = img.getAttribute("width") + "px";

    function drawPoster() {
      canvas.width = img.naturalWidth;
      canvas.height = img.naturalHeight;
      canvas.getContext("2d").drawImage(img, 0, 0);
    }
    if (img.complete && img.naturalWidth) drawPoster();
    else img.addEventListener("load", drawPoster, { once: true });

    if (!ms && window.fetch) {
      fetch(src).then(function (r) { return r.arrayBuffer(); })
        .then(function (buf) { ms = gifLength(buf) || 3000; })
        .catch(function () { ms = 3000; });
    }

    var timer = null;
    var playId = 0;
    function stop() {
      clearTimeout(timer);
      timer = null;
      playId++;  // cancels a play that is still loading
      wrap.classList.remove("is-playing", "is-starting");
      wrap.classList.add("is-stopped");
      wrap.setAttribute("aria-label", "Play animation: " + (img.alt || "GIF"));
    }
    function play() {
      var id = ++playId;
      var started = false;
      timer = -1;  // marks "playing" straight away, so a second click stops it
      // Hide the button now, but keep the still frame showing until the
      // fresh copy of the GIF has loaded. Otherwise the box shrinks to
      // nothing for a moment and the button jumps to the corner.
      wrap.classList.add("is-starting");
      wrap.setAttribute("aria-label", "Stop animation: " + (img.alt || "GIF"));
      function begin() {
        if (started || id !== playId) return;
        started = true;
        wrap.classList.remove("is-stopped", "is-starting");
        wrap.classList.add("is-playing");
        timer = setTimeout(stop, ms || 3000);
      }
      img.addEventListener("load", begin, { once: true });
      // A new address makes the browser start the GIF from frame 1.
      img.src = src.split("?")[0] + "?play=" + Date.now();
      setTimeout(begin, 1500);  // in case the load event never arrives
    }
    function toggle() { if (timer) stop(); else play(); }
    wrap._clickgif = { play: play, stop: stop, isPlaying: function () { return !!timer; } };

    // Inside a .clickgif-group, one click plays (or stops) every GIF in the
    // group together, so they can be compared side by side.
    function groupToggle() {
      var group = wrap.closest(".clickgif-group");
      if (!group) { toggle(); return; }
      var all = group.querySelectorAll(".clickgif-wrap");
      var anyPlaying = Array.prototype.some.call(all, function (w) {
        return w._clickgif && w._clickgif.isPlaying();
      });
      all.forEach(function (w) {
        if (!w._clickgif) return;
        if (anyPlaying) w._clickgif.stop(); else w._clickgif.play();
      });
    }

    wrap.addEventListener("click", groupToggle);
    wrap.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); groupToggle(); }
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("img.clickgif").forEach(setUp);
  });
})();
