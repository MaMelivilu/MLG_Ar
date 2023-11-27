
var interfaceConfig = {

    TOOLBAR_BUTTONS: [
        'microphone',
        'camera',
        'closedcaptions',
        'desktop',
        'fullscreen',
        'fodeviceselection',
        'hangup',                //SAlir
        'profile',
        'info',               //ver el link
        'chat',
        'recording',             //grabar
        'livestreaming',      //admin lo puede hacer
        'etherpad',
        'sharedvideo',        //admin lo puede hacer
        'settings',
        'raisehand',              //manito
        'videoquality',           //calidad de video
        'filmstrip',
        'invite',
        'feedback',
        'stats',
        'shortcuts',
        'tileview',
        'videobackgroundblur',
        'download',
        'help',
        'mute-everyone',    //administrador
        'e2ee',
        'toggleFilmStrip'
    ],

    SETTINGS_SECTIONS: [
        'devices',
        'language',
        'moderator',
        'profile',
        'calendar'
    ],
    SHOW_CHROME_EXTENSION_BANNER: false
};

const domain = 'meet.jit.si';
const options = {
    roomName: 'Iniciar Directo',
    width: 1920,
    height: 1080,
    parentNode: document.querySelector('#meet'),
    userInfo: {
        email: "admin@gmail.com",
        displayName: "",
    },
    noSsl: true,
    interfaceConfigOverwrite: interfaceConfig,
};
const api = new JitsiMeetExternalAPI(domain, options);

const jitsiMeet = new JitsiMeet({
    
    url: 'https://meet.jit.si/CLASSES_YA_2023',
  });
  jitsiMeet.on('ready', () => {
    
    document.querySelector('#share-screen').addEventListener('click', shareScreen);
  });
// Obtener el nombre de usuario de la cuenta de Google
const username = window.google.accounts.currentUser.displayName;

// Actualizar el texto del elemento
document.querySelector(".text").textContent = username;
