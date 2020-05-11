function tabLinkOnClick(e) {
    var clickedLink = $(e.target);
    var activeTab = $('#' + clickedLink.data('tab-id'));
    var tabGroup = clickedLink.data('tab-group');

    $('.tab[data-tab-group=' + tabGroup + ']').not(activeTab).hide();
    activeTab.fadeIn();

    clickedLink.removeClass('inactive');
    $('.tab-link[data-tab-group=' + tabGroup + ']').not(clickedLink).addClass('inactive');
}
$(function() {
    $('.tab-link').click(tabLinkOnClick);
});
