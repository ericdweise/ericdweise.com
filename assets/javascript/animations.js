$(document).ready(function()
{
    $('.expandable').on('click', function (e) {
    e.preventDefault();
    this.expand = !this.expand;
    // $(this).text(this.expand?"Click to collapse":"Click to read more");
    $(this).closest('.expandable').find('.small, .big').toggleClass('small big');
    $(this).css('display', this.expand ? 'block' : 'inline-block');
    });
});
