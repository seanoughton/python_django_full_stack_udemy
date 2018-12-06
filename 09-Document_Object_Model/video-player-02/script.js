var supportsVideo = !!document.createElement('video').canPlayType;
if (supportsVideo) {
   // set up custom controls
   // ...
}

var videoContainer = document.getElementById('videoContainer');
var video = document.getElementById('video');
video.play()
var videoControls = document.getElementById('video-controls');

// Hide the default controls
video.controls = false;

// Display the user defined video controls
videoControls.style.display = 'block';

var playpause = document.getElementById('playpause');
var stop = document.getElementById('stop');
var mute = document.getElementById('mute');
var volinc = document.getElementById('volinc');
var voldec = document.getElementById('voldec');
var progress = document.getElementById('progress');
var progressBar = document.getElementById('progress-bar');
var fullscreen = document.getElementById('fs');
var fullScreenEnabled = !!(document.fullscreenEnabled || document.mozFullScreenEnabled || document.msFullscreenEnabled || document.webkitSupportsFullscreen || document.webkitFullscreenEnabled || document.createElement('video').webkitRequestFullScreen);

var isFullScreen = function() {
   return !!(document.fullScreen || document.webkitIsFullScreen || document.mozFullScreen || document.msFullscreenElement || document.fullscreenElement);
}

var handleFullscreen = function() {
   if (isFullScreen()) {
      if (document.exitFullscreen) document.exitFullscreen();
      else if (document.mozCancelFullScreen) document.mozCancelFullScreen();
      else if (document.webkitCancelFullScreen) document.webkitCancelFullScreen();
      else if (document.msExitFullscreen) document.msExitFullscreen();
      setFullscreenData(false);
   }
   else {
      if (videoContainer.requestFullscreen) videoContainer.requestFullscreen();
      else if (videoContainer.mozRequestFullScreen) videoContainer.mozRequestFullScreen();
      else if (videoContainer.webkitRequestFullScreen) videoContainer.webkitRequestFullScreen();
      else if (videoContainer.msRequestFullscreen) videoContainer.msRequestFullscreen();
      setFullscreenData(true);
   }
}

if (!fullScreenEnabled) {
   fullscreen.style.display = 'none';
}

// Event listeners for control buttons

playpause.addEventListener('click', function(e) {
   if (video.paused || video.ended) video.play();
   else video.pause();
});

stop.addEventListener('click', function(e) {
   video.pause();
   video.currentTime = 0;
   progress.value = 0;
});

mute.addEventListener('click', function(e) {
   video.muted = !video.muted;
});

var alterVolume = function(dir) {
   var currentVolume = Math.floor(video.volume * 10) / 10;
   if (dir === '+') {
      if (currentVolume < 1) video.volume += 0.1;
   }
   else if (dir === '-') {
      if (currentVolume > 0) video.volume -= 0.1;
   }
}

volinc.addEventListener('click', function(e) {
   alterVolume('+');
});
voldec.addEventListener('click', function(e) {
   alterVolume('-');
});

video.addEventListener('loadedmetadata', function() {
   progress.setAttribute('max', video.duration);
});

video.addEventListener('timeupdate', function() {
   if (!progress.getAttribute('max')) progress.setAttribute('max', video.duration);
   progress.value = video.currentTime;
   progressBar.style.width = Math.floor((video.currentTime / video.duration) * 100) + '%';
});

progress.addEventListener('click', function(e) {
   var pos = (e.pageX  - this.offsetLeft) / this.offsetWidth;
   video.currentTime = pos * video.duration;
});

fs.addEventListener('click', function(e) {
   handleFullscreen();
});
