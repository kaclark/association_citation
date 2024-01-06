<script type="text/javascript">
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var post_content = this.nextElementSibling;
    if (post_content.style.display === "block") {
      post_content.style.display = "none";
    } else {
      post_content.style.display = "block";
    }
  });
}
</script>
