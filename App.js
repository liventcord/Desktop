const icon = '/resources/icons/icon.png';

await Neutralino.window.setIcon(icon);

await Neutralino.window.open({
    url: 'https://leventcord.bsite.net/app',
    fullscreen: false,
    width: 800,
    height: 600,
    resizable: true
});
