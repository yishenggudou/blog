$(document).ready(function () {
    $('.body').append('<div id="gitment"></div>');
    var gitment = new Gitment({
        owner: 'yishenggudou',
        repo: 'blog',
        oauth: {
            client_id: '1e32c775b8aae60b1bd8',
            client_secret: '63f331da2bb258d3dadd3eeab5bc2d57c92f3668',
        },
    });
    gitment.render('gitment');
});
