function showContent(contentId) {
    // Hide all content divs
    var contentDivs = document.getElementsByClassName('main');
    for (var i = 0; i < contentDivs.length; i++) {
        contentDivs[i].style.display = 'none';
    }

    // Show the selected content div
    var selectedContent = document.getElementById(contentId);
    if (selectedContent) {
        selectedContent.style.display = 'block';
    }
};