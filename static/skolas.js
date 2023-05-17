function resetSearch() {
    document.getElementById("search").value = "";
    document.getElementById("location").value = "";
    document.getElementsByTagName("form")[0].submit();
}