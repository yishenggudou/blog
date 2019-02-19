$(document).ready(function () {
    $('.body').append('<hr style="margin-top: 72px;"/><div ><img style="display:block;margin: auto" width="200px" src="https://timger-blog.oss-cn-beijing.aliyuncs.com/68747470733a2f2f74696d6765722d313235313737313635342e636f732e61702d6265696a696e672e6d7971636c6f75642e636f6d2f576563686174494d47322e6a706567.jpeg"/> </div></div><div id="gitment"></div>');
    var gitment = new Gitment({
        id: window.location.pathname,
        owner: 'yishenggudou',
        repo: 'blog',
        oauth: {
            client_id: '1e32c775b8aae60b1bd8',
            client_secret: '63f331da2bb258d3dadd3eeab5bc2d57c92f3668',
        },
    });
    gitment.render('gitment');
});
$(document).ready(function () {
    $.getScript("https://www.googletagmanager.com/gtag/js?id=UA-115602552-1", function (data, textStatus, jqxhr) {
        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }

        gtag('js', new Date());
        gtag('config', 'UA-115602552-1');
    });
});