// Open links in a new tab:
//  - links to other websites (Sphinx gives them the classes "reference external")
//  - links that show a picture at full size (Sphinx gives them "image-reference")
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("a.reference.external, a.image-reference").forEach(function (link) {
    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener noreferrer");
  });
});
